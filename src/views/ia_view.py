"""Console view for AI landing page generation."""

from src.views.input_helpers import print_title, read_text, request_data


def show_ai_landing(client):
    print_title("GENERAR LANDING CON IA")
    product_name = read_text("Nombre del producto: ", max_length=40)
    main_benefit = read_text("Beneficio principal: ", max_length=100)
    price = read_text("Precio (ejemplo: 59.900 COP): ", max_length=20)

    payload = {
        "product_name": product_name,
        "main_benefit": main_benefit,
        "price": price,
    }

    print("\nGenerando texto con IA, esto puede tardar unos segundos...")
    success, landing = request_data(client, "GENERAR_LANDING_IA", payload)
    if success:
        print_title("LANDING GENERADA")
        print(landing)