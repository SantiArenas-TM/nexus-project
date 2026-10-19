import socket
import json

from src.controllers.product_controller import product_controller
from src.controllers.metric_controller import metric_controller
from src.controllers.discount_controller import discount_controller
from src.controllers.shipment_controller import shipment_controller

# Inicializamos la instancia de cada controlador
product_ctrl = product_controller()
metric_ctrl = metric_controller()
discount_ctrl = discount_controller()
shipment_ctrl = shipment_controller()

# Definimos el host y el puerto
HOST = '127.0.0.1'
PORT = 65432


# Funciones para crear las peticiones del servidor
def process_request(json_message):
    # Lee el comando y el payload
    command = json_message["comando"]
    payload = json_message["payload"]

    # Llama a la función correspondiente según el comando
    if command == "CREAR_PRODUCTO":
        result = product_ctrl.create_product(
            payload["id_product"],
            payload["name_product"],
            payload["acquisicion_cost"],
            payload["estimated_freight"],
        ).to_dict()

    elif command == "OBTENER_PRODUCTOS":
        result = product_ctrl.get_all()

    elif command == "REGISTRAR_METRICA":
        result = metric_ctrl.register_metric(
            payload["id"],
            payload["campaign_name"],
            payload["investment"],
            payload["clicks"],
            payload["conversion"],
            payload["revenue_generated"],
        )

    elif command == "OBTENER_METRICAS":
        result = metric_ctrl.get_all()

    elif command == "CREAR_REGLA_DESCUENTO":
        result = discount_ctrl.create_rule(
            payload["id"],
            payload["discount_percentage"],
            payload["minimum_quantity"],
            payload["offer_condition"],
        )

    elif command == "APLICAR_DESCUENTO":
        result = discount_ctrl.apply_discounts_to_price(
            payload["amount"],
            payload["base_price"],
        )

    elif command == "REGISTRAR_ENVIO":
        result = shipment_ctrl.register_shipment(
            payload["id"],
            payload["tracking_code"],
            payload["carrier"],
            payload["end_customer"],
        )

    elif command == "ACTUALIZAR_ENVIO":
        result = shipment_ctrl.update_shipment_status(
            payload["tracking_code"],
            payload["new_state"],
        )

    elif command == "OBTENER_ENVIOS":
        result = shipment_ctrl.get_all()

    # Si no se reconoce el comando devuelve un error y un mensaje de error
    else:
        return {"status": "ERROR", "data": "Comando no reconocido"}

    # Devuelve el resultado en un diccionario
    return {"status": "OK", "data": result}


# Función para darle inicio al servidor
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Servidor backend ejecutándose en {HOST}:{PORT}...")

        while True:
            conn, addr = s.accept()

            with conn:
                while True:
                    data = conn.recv(1024)

                    if not data:
                        break

                    json_message = json.loads(data.decode('utf-8'))
                    response = process_request(json_message)
                    conn.sendall(json.dumps(response).encode('utf-8'))


# Ejecutamos el servidor llamando la función 
if __name__ == "__main__":
    start_server()