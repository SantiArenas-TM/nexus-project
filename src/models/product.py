class product:
    def __init__(self, id_product, name_product, acquisicion_cost, estimated_freight):
        self.id_product = id_product
        self.nameProduct = name_product
        self.acquisicion_cost = acquisicion_cost 
        self.estimated_freight = estimated_freight
        self.suggested_price = 0.0
        self.netMargin = 0.0

# Método para calcular el precio y manejar el error de precios dejados en ceros
    def CALCULAR_PRECIO(self, desired_margin_percentage=0.30):
        total_cost = self.acquisicion_cost + self.estimated_freight

        if total_cost <= 0:
            raise ValueError("El valor de los costos debe ser mayor a cero")

        self.suggested_price = total_cost / (1 - desired_margin_percentage)
        self.netMargin = self.suggested_price - total_cost

        return round(self.suggested_price, 2)

# Este método sirve para devolver en un diccionario los precios que se calcularon
    def to_dict(self):
        return {
            "id_product": self.id_product,
            "name_product": self.name_product,
            "acquisicion_cost": self.acquisicion_cost,
            "estimated_freight": self.estimated_freight,
            "suggested_price": self.suggested_price,
            "netMargin": self.netMargin,
    }