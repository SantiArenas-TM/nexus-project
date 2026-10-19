class discount_rule:
    def __init__(self, id, discount_percentage, minimum_quantity, offer_condition):
        self.id = id
        self.discount_percentage = discount_percentage
        self.minimum_quantity = minimum_quantity
        self.offer_condition = offer_condition

# Método para aplicar los descuentos por cantidad
    def apply_discount(self, amount, base_price):
        if amount >= self.minimum_quantity:
            final_price = base_price - (base_price * self.discount_percentage / 100)
            return round(final_price, 2)

        return base_price

# Método para retornar los resultados en un diccionario
    def to_dict(self):
        return {
            "id": self.id,
            "discount_percentage": self.discount_percentage,
            "minimum_quantity": self.minimum_quantity,
            "offer_condition": self.offer_condition,
        }