from src.models.shipment_tracking import shipment_tracking


class shipment_controller:
    def __init__(self):
        self.shipments = []

# Método para registrar un nuevo envio
    def register_shipment(self, id, tracking_code, carrier, end_customer):
        new_shipment = shipment_tracking(id, tracking_code, carrier, "EN_PREPARACION", end_customer)
        self.shipments.append(new_shipment)

        return new_shipment.to_dict()

# Método para actualizar el estado de un envio existente
    def update_shipment_status(self, tracking_code, new_state):
        for current_shipment in self.shipments:
            if current_shipment.tracking_code == tracking_code:
                current_shipment.update_status(new_state)
                return True

        return False

# Método para obtener todos los envios registrados
    def get_all(self):
        return [current_shipment.to_dict() for current_shipment in self.shipments]