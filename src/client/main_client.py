"""Console client entry point for Nexus.

Start the backend first (from the project root):
    python -m src.server.main_server

Then run the client (from the project root):
    python -m src.client.main_client
"""

import json
import os
import socket

from src.views.input_helpers import print_title, read_option
from src.views.producto_view import show_product_menu
from src.views.metrica_view import show_metric_menu
from src.views.descuento_view import show_discount_menu
from src.views.envio_view import show_shipment_menu
from src.views.ia_view import show_ai_landing

DEFAULT_HOST = os.getenv("NEXUS_HOST", "127.0.0.1")
DEFAULT_PORT = int(os.getenv("NEXUS_PORT", "65432"))
TIMEOUT_SECONDS = 60
BUFFER_SIZE = 4096
# The backend reads every request with a single recv(1024).
SERVER_MAX_REQUEST_BYTES = 1024


class ApiClient:
    """Talks to the Nexus backend over a plain TCP socket.

    Request:  {"comando": "OBTENER_PRODUCTOS", "payload": {...}}
    Response: {"status": "OK" | "ERROR", "data": ...}

    The backend does not end messages with a newline, so the response is
    read until the received bytes form a complete JSON document.
    """

    def __init__(self, host=DEFAULT_HOST, port=DEFAULT_PORT, timeout=TIMEOUT_SECONDS):
        self.host = host
        self.port = port
        self.timeout = timeout
        self._socket = None

    def connect(self):
        self._socket = socket.create_connection((self.host, self.port), self.timeout)

    def close(self):
        if self._socket is not None:
            try:
                self._socket.close()
            except OSError:
                pass
        self._socket = None

    def is_server_available(self):
        """Try to open the connection. Returns True when the backend answers."""
        try:
            if self._socket is None:
                self.connect()
            return True
        except OSError:
            self._socket = None
            return False

    def send_command(self, command, payload=None):
        """Send one command and return the backend response as a dict.

        Connection problems never raise: they come back as
        {"status": "ERROR", "data": "<message in Spanish>"} so the views can
        treat every failure in the same way.
        """
        message = json.dumps({"comando": command, "payload": payload or {}}).encode("utf-8")
        if len(message) > SERVER_MAX_REQUEST_BYTES:
            return self._error("La solicitud es demasiado grande para el servidor. Acorte los textos.")

        try:
            self._send(message)
        except OSError:
            self.close()
            return self._error(
                f"No se pudo conectar con el servidor en {self.host}:{self.port}. "
                "Verifique que el backend esté encendido."
            )
        return self._receive()

    # ------------------------------------------------------------------ helpers
    def _send(self, message):
        """Send bytes, reconnecting once if the old connection is dead."""
        for attempt in range(2):
            try:
                if self._socket is None:
                    self.connect()
                self._socket.sendall(message)
                return
            except OSError:
                self.close()
                if attempt == 1:
                    raise

    def _receive(self):
        buffer = b""
        while True:
            try:
                chunk = self._socket.recv(BUFFER_SIZE)
            except TimeoutError:
                self.close()
                return self._error("El servidor no respondió a tiempo.")
            except OSError:
                self.close()
                return self._error("Se perdió la conexión con el servidor.")

            if not chunk:
                self.close()
                return self._error(
                    "El servidor cerró la conexión sin responder "
                    "(posible error interno del backend)."
                )

            buffer += chunk
            try:
                return json.loads(buffer.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError):
                continue  # message not complete yet, keep reading

    @staticmethod
    def _error(message):
        return {"status": "ERROR", "data": message}


def main():
    client = ApiClient()
    if not client.is_server_available():
        print(f"\n[ERROR] No se pudo conectar con el servidor en {client.host}:{client.port}.")
        print("Inicie el backend con:  python -m src.server.main_server")
        return

    menu_actions = {
        "1": show_product_menu,
        "2": show_metric_menu,
        "3": show_discount_menu,
        "4": show_shipment_menu,
        "5": show_ai_landing,
    }

    try:
        while True:
            print_title("NEXUS - MENÚ PRINCIPAL")
            print("1. Calculadora de productos")
            print("2. Métricas de campañas")
            print("3. Descuentos por cantidad")
            print("4. Seguimiento de envíos")
            print("5. Generar landing con IA")
            print("0. Salir")
            option = read_option("Seleccione una opción: ", ["0", "1", "2", "3", "4", "5"])

            if option == "0":
                print("\n¡Hasta pronto!")
                break
            menu_actions[option](client)
    except (KeyboardInterrupt, EOFError):
        print("\n\nSesión finalizada.")
    finally:
        client.close()


if __name__ == "__main__":
    main()