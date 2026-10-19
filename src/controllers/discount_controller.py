from src.models.discount_rule import discount_rule


class discount_controller:
    def __init__(self):
        self.rules = []

# Método para crear reglas de descuento 
    def create_rule(self, id, discount_percentage, minimum_quantity, offer_condition):
        new_rule = discount_rule(id, discount_percentage, minimum_quantity, offer_condition)
        self.rules.append(new_rule)

        return new_rule.to_dict()

# Método para aplicar las reglas de descuento
    def apply_discounts_to_price(self, amount, base_price):
        final_price = base_price

        for current_rule in self.rules:
            final_price = current_rule.apply_discount(amount, final_price)

        return final_price