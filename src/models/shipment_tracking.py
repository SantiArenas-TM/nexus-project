class shipment_tracking:
    def __init__(self, id, tracking_code, carrier, shipping_status, end_customer):
        self.id = id
        self.tracking_code = tracking_code
        self.carrier = carrier
        self.shipping_status = shipping_status
        self.end_customer = end_customer

# Método para actualizar el estaod del envío
    def update_status(self, new_state):
        self.shipping_status = new_state

# Método para convertir el resultado en un diccionario
    def to_dict(self):
        return {
            "id": self.id,
            "tracking_code": self.tracking_code,
            "carrier": self.carrier,
            "shipping_status": self.shipping_status,
            "end_customer": self.end_customer,
        }