"""Console view for quantity discount rules (RF-04)."""

from src.views.input_helpers import (
    format_money, print_title, read_float, read_from_menu, read_int,
    read_option, read_text, request_data,
)
from src.views.producto_view import (
    KEY_ID, KEY_NAME, KEY_PRICE, fetch_products, find_product_by_id,
    print_products_table, total_cost_of,
)

MAX_QUANTITY = 10000


def _create_rule(client):
    print_title("CREAR REGLA DE DESCUENTO")
    rule_id = read_int("ID de la regla: ", minimum=1)
    discount_percentage = read_float(
        "Porcentaje de descuento (0-100): ", minimum=0, maximum=100, allow_minimum=False
    )
    minimum_quantity = read_int(
        f"Cantidad mínima para aplicar (1-{MAX_QUANTITY}): ", minimum=1, maximum=MAX_QUANTITY
    )
    offer_condition = read_text("Condición de la oferta (ej. Compra al por mayor): ", max_length=100)

    payload = {
        "id": rule_id,
        "discount_percentage": discount_percentage,
        "minimum_quantity": minimum_quantity,
        "offer_condition": offer_condition,
    }
    success, rule = request_data(client, "CREAR_REGLA_DESCUENTO", payload)
    if success:
        print("\n✓ Regla creada:")
        print(f"  ID {rule['id']}: {rule['discount_percentage']:g}% de descuento "
              f"desde {rule['minimum_quantity']} unidad(es).")
        print(f"  Condición: {rule['offer_condition']}")


def _ask_base_price(client):
    """Return (base_price, total_cost). total_cost is None for a manual price.

    Returns (None, None) when the user cancels or a request fails.
    """
    source = read_from_menu(
        "¿De dónde tomar el precio base?",
        {"catalog": "Usar el precio sugerido de un producto", "manual": "Escribir el precio"},
    )
    if source == "manual":
        return read_float("Precio base por unidad: ", minimum=0, allow_minimum=False), None

    products = fetch_products(client)
    if products is None:
        return None, None
    if not products:
        print("\nNo hay productos registrados. Registre uno en la calculadora de productos.")
        return None, None
    print_products_table(products)

    while True:
        product_id = read_int("\nID del producto (0 para cancelar): ", minimum=0)
        if product_id == 0:
            return None, None
        product = find_product_by_id(products, product_id)
        if product is not None:
            print(f"Producto: {product[KEY_NAME]} - precio sugerido {format_money(product[KEY_PRICE])}")
            return product[KEY_PRICE], total_cost_of(product)
        print(f"  ✗ No existe un producto con ID {product_id}.")


def _apply_discounts(client):
    print_title("SIMULAR DESCUENTOS POR CANTIDAD")
    base_price, total_cost = _ask_base_price(client)
    if base_price is None:
        return
    quantity = read_int(f"Cantidad de unidades (1-{MAX_QUANTITY}): ", minimum=1, maximum=MAX_QUANTITY)

    payload = {"amount": quantity, "base_price": base_price}
    success, final_price = request_data(client, "APLICAR_DESCUENTO", payload)
    if not success:
        return
    if isinstance(final_price, bool) or not isinstance(final_price, (int, float)):
        print("\n[ERROR] El servidor devolvió un valor inesperado.")
        return

    print(f"\nPrecio unitario original:      {format_money(base_price)}")
    print(f"Precio unitario con descuento: {format_money(final_price)}")
    print(f"Ahorro por unidad:             {format_money(base_price - final_price)}")
    print(f"Total a cobrar ({quantity} u.):".ljust(31) + format_money(final_price * quantity))

    if final_price >= base_price:
        print("\nNinguna regla aplica para esa cantidad (o aún no hay reglas creadas).")
    if total_cost is not None and final_price < total_cost:
        print(f"⚠ El precio con descuento queda por debajo del costo total ({format_money(total_cost)}): "
              "se vendería a pérdida.")


def show_discount_menu(client):
    actions = {
        "1": _create_rule,
        "2": _apply_discounts,
    }
    while True:
        print_title("DESCUENTOS POR CANTIDAD")
        print("1. Crear regla de descuento")
        print("2. Simular descuento sobre un precio")
        print("0. Volver al menú principal")
        option = read_option("Seleccione una opción: ", ["0", "1", "2"])
        if option == "0":
            return
        actions[option](client)