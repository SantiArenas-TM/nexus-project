from src.models.product import product


class product_controller:
    def __init__(self):
        self.products = []

# Método para crear un nuevo producto
    def create_product(self, id_product, name_product, acquisicion_cost, estimated_freight):
        new_product = product(id_product, name_product, acquisicion_cost, estimated_freight)
        new_product.CALCULAR_PRECIO()
        self.products.append(new_product)

        return new_product

# Método para obtener todos los productos
    def get_all(self):
        return [current_product.to_dict() for current_product in self.products]

# Método para obtener un producto por su id
    def find_by_id(self, id_product):
        for current_product in self.products:
            if current_product.id_product == id_product:
                return current_product

        return None