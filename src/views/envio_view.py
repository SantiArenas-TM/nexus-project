"""Console view for shipment tracking (RF-05)."""

from src.views.input_helpers import (
    print_title, read_from_menu, read_option, read_text,
    read_tracking_code, read_unique_id, request_data,
)

# The backend only defines "EN_PREPARACION" (initial state, set on registration).
# The other states are a proposal of the frontend; the backend stores any text.
SHIPMENT_STATUSES = {
    "EN_PREPARACION": "En preparación",
    "EN_TRANSITO": "En tránsito",
    "ENTREGADO": "Entregado",
    "DEVUELTO": "Devuelto",
}


def fetch_shipments(client):
    """Return the list of shipments, or None if the request failed."""
    success, shipments = request_data(client, "OBTENER_ENVIOS")
    return shipments if success else None


def _status_label(status):
    return SHIPMENT_STATUSES.get(status, status)


def _find_by_tracking_code(shipments, tracking_code):
    for shipment in shipments:
        if shipment["tracking_code"].upper() == tracking_code.upper():
            return shipment
    return None


def _print_shipments_table(shipments):
    if not shipments:
        print("\nNo hay envíos para mostrar.")
        return
    print(f"\n{'ID':<5}{'Código':<16}{'Transportadora':<20}{'Cliente':<24}{'Estado'}")
    print("-" * 80)
    for shipment in shipments:
        print(
            f"{shipment['id']:<5}{shipment['tracking_code']:<16}"
            f"{shipment['carrier'][:18]:<20}{shipment['end_customer'][:22]:<24}"
            f"{_status_label(shipment['shipping_status'])}"
        )


def _register_shipment(client):
    print_title("REGISTRAR ENVÍO")
    shipments = fetch_shipments(client)
    if shipments is None:
        return

    shipment_id = read_unique_id("ID del envío: ", {s["id"] for s in shipments})
    tracking_code = read_tracking_code(
        "Código de seguimiento: ", taken_codes=[s["tracking_code"] for s in shipments]
    )
    carrier = read_text("Transportadora: ", max_length=40)
    end_customer = read_text("Cliente final: ")

    payload = {
        "id": shipment_id,
        "tracking_code": tracking_code,
        "carrier": carrier,
        "end_customer": end_customer,
    }
    success, created = request_data(client, "REGISTRAR_ENVIO", payload)
    if success:
        print(f"\n✓ Envío registrado con código {created['tracking_code']}.")
        print(f"  Estado inicial: {_status_label(created['shipping_status'])}")


def _list_shipments(client):
    print_title("LISTA DE ENVÍOS")
    shipments = fetch_shipments(client)
    if shipments is not None:
        _print_shipments_table(shipments)


def _track_shipment(client):
    print_title("RASTREAR ENVÍO")
    shipments = fetch_shipments(client)
    if shipments is None:
        return
    if not shipments:
        print("\nNo hay envíos registrados.")
        return
    tracking_code = read_tracking_code("Código de seguimiento: ")
    shipment = _find_by_tracking_code(shipments, tracking_code)
    if shipment is None:
        print(f"\nNo existe un envío con el código {tracking_code}.")
        return
    print(f"\nCódigo:         {shipment['tracking_code']}")
    print(f"Transportadora: {shipment['carrier']}")
    print(f"Cliente final:  {shipment['end_customer']}")
    print(f"Estado:         {_status_label(shipment['shipping_status'])}")


def _filter_by_status(client):
    print_title("ENVÍOS POR ESTADO")
    shipments = fetch_shipments(client)
    if shipments is None:
        return
    status = read_from_menu("Filtrar por estado:", SHIPMENT_STATUSES)
    matches = [s for s in shipments if s["shipping_status"] == status]
    _print_shipments_table(matches)


def _update_status(client):
    print_title("ACTUALIZAR ESTADO DE UN ENVÍO")
    shipments = fetch_shipments(client)
    if shipments is None:
        return
    if not shipments:
        print("\nNo hay envíos registrados.")
        return
    tracking_code = read_tracking_code("Código de seguimiento: ")
    shipment = _find_by_tracking_code(shipments, tracking_code)
    if shipment is None:
        print(f"\nNo existe un envío con el código {tracking_code}.")
        return

    print(f"Estado actual: {_status_label(shipment['shipping_status'])}")
    new_state = read_from_menu("Nuevo estado:", SHIPMENT_STATUSES)
    if new_state == shipment["shipping_status"]:
        print("\nEl envío ya tiene ese estado. No se realizó ningún cambio.")
        return

    payload = {"tracking_code": shipment["tracking_code"], "new_state": new_state}
    success, updated = request_data(client, "ACTUALIZAR_ENVIO", payload)
    if not success:
        return
    if updated is True:
        print(f"\n✓ Estado actualizado a: {_status_label(new_state)}.")
    else:
        print("\nEl servidor no encontró ese código de seguimiento.")


def show_shipment_menu(client):
    actions = {
        "1": _register_shipment,
        "2": _list_shipments,
        "3": _track_shipment,
        "4": _filter_by_status,
        "5": _update_status,
    }
    while True:
        print_title("SEGUIMIENTO DE ENVÍOS")
        print("1. Registrar envío")
        print("2. Ver todos los envíos")
        print("3. Rastrear envío por código")
        print("4. Ver envíos por estado")
        print("5. Actualizar estado de un envío")
        print("0. Volver al menú principal")
        option = read_option("Seleccione una opción: ", ["0", "1", "2", "3", "4", "5"])
        if option == "0":
            return
        actions[option](client)