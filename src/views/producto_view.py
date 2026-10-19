"""Console view for the product price calculator (RF-03)."""

from src.views.input_helpers import (
    format_money, print_title, read_float, read_int, read_option,
    read_text, read_unique_id, request_data,
)

# Keys returned by product.to_dict() in the backend.
KEY_ID = "ID"
KEY_NAME = "NOMBRE"
KEY_COST = "COSTO_ADQUISICION"
KEY_FREIGHT = "FLETE_ESTIMADO"
KEY_PRICE = "PRECIO_SUGERIDO"
KEY_MARGIN = "MARGEN_NETO"

# Margin used by the backend in CALCULAR_PRECIO (desired_margin_percentage=0.30).
BACKEND_MARGIN_PERCENT = 30


def fetch_products(client):
    """Return the list of products, or None if the request failed."""
    success, products = request_data(client, "OBTENER_PRODUCTOS")
    return products if success else None


def find_product_by_id(products, product_id):
    for product in products:
        if product[KEY_ID] == product_id:
            return product
    return None


def total_cost_of(product):
    return product[KEY_COST] + product[KEY_FREIGHT]


def print_products_table(products):
    if not products:
        print("\nNo hay productos registrados.")
        return
    print(
        f"\n{'ID':<6}{'Nombre':<26}{'Costo':>12}{'Flete':>12}"
        f"{'Costo total':>14}{'Precio sug.':>14}{'Margen neto':>14}"
    )
    print("-" * 98)
    for product in products:
        print(
            f"{product[KEY_ID]:<6}{product[KEY_NAME][:24]:<26}"
            f"{format_money(product[KEY_COST]):>12}{format_money(product[KEY_FREIGHT]):>12}"
            f"{format_money(total_cost_of(product)):>14}"
            f"{format_money(product[KEY_PRICE]):>14}{format_money(product[KEY_MARGIN]):>14}"
        )


def _print_product_detail(product):
    print(f"\nProducto:                {product[KEY_NAME]} (ID {product[KEY_ID]})")
    print(f"Costo de adquisición:    {format_money(product[KEY_COST])}")
    print(f"Flete estimado:          {format_money(product[KEY_FREIGHT])}")
    print(f"Costo total:             {format_money(total_cost_of(product))}")
    print(f"Precio de venta sugerido:{format_money(product[KEY_PRICE]):>14}"
          f"  (margen del {BACKEND_MARGIN_PERCENT}%)")
    print(f"Margen neto por unidad:  {format_money(product[KEY_MARGIN])}")


def _create_product(client):
    print_title("REGISTRAR PRODUCTO")
    products = fetch_products(client)
    if products is None:
        return

    existing_ids = {product[KEY_ID] for product in products}
    id_product = read_unique_id("ID del producto: ", existing_ids)
    name_product = read_text("Nombre del producto: ")
    acquisition_cost = read_float("Costo de adquisición: ", minimum=0, allow_minimum=False)
    estimated_freight = read_float("Flete estimado: ", minimum=0, allow_minimum=False)

    # The payload keys must match exactly what main_server.py reads
    # (the backend spells "acquisicion_cost" this way).
    payload = {
        "id_product": id_product,
        "name_product": name_product,
        "acquisicion_cost": acquisition_cost,
        "estimated_freight": estimated_freight,
    }
    success, created = request_data(client, "CREAR_PRODUCTO", payload)
    if success:
        print("\n✓ Producto registrado. Cálculo del sistema:")
        _print_product_detail(created)


def _list_products(client):
    print_title("LISTA DE PRODUCTOS")
    products = fetch_products(client)
    if products is not None:
        print_products_table(products)


def _search_product(client):
    print_title("BUSCAR PRODUCTO")
    products = fetch_products(client)
    if products is None:
        return
    if not products:
        print("\nNo hay productos registrados.")
        return
    product_id = read_int("ID del producto: ", minimum=1)
    product = find_product_by_id(products, product_id)
    if product is None:
        print(f"\nNo existe un producto con ID {product_id}.")
    else:
        _print_product_detail(product)


def _simulate_price(client):
    """Recalculate the margin for a price chosen by the user (all done locally)."""
    print_title("SIMULAR PRECIO DE VENTA")
    products = fetch_products(client)
    if products is None:
        return
    if not products:
        print("\nNo hay productos registrados.")
        return
    print_products_table(products)

    product = None
    while product is None:
        product_id = read_int("\nID del producto (0 para cancelar): ", minimum=0)
        if product_id == 0:
            return
        product = find_product_by_id(products, product_id)
        if product is None:
            print(f"  ✗ No existe un producto con ID {product_id}.")

    desired_price = read_float("Precio de venta deseado: ", minimum=0, allow_minimum=False)
    total_cost = total_cost_of(product)
    profit = desired_price - total_cost
    margin_percent = profit / desired_price * 100

    print(f"\nCosto total (punto de equilibrio): {format_money(total_cost)}")
    print(f"Ganancia por unidad:               {format_money(profit)}")
    print(f"Margen proyectado:                 {margin_percent:.1f}%")
    if profit <= 0:
        print("⚠ Con este precio no hay ganancia: se vendería a pérdida o sin margen.")


def show_product_menu(client):
    actions = {
        "1": _create_product,
        "2": _list_products,
        "3": _search_product,
        "4": _simulate_price,
    }
    while True:
        print_title("CALCULADORA DE PRODUCTOS")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Buscar producto por ID")
        print("4. Simular precio de venta")
        print("0. Volver al menú principal")
        option = read_option("Seleccione una opción: ", ["0", "1", "2", "3", "4"])
        if option == "0":
            return
        actions[option](client)