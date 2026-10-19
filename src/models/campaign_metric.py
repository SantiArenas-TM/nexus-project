from datetime import datetime


class campaign_metric:
    def __init__(self, id, campaign_name, investment, clicks, conversion):
        self.id = id
        self.campaign_name = campaign_name
        self.investment = investment
        self.clicks = clicks
        self.conversion = conversion
        self.roas = 0.0
        self.date_consultation = datetime.now()

# Método para calculat los ROAS
    def calculate_ROAS(self, revenue_generated):
        if self.investment <= 0:
            raise ValueError("La inversión debe ser mayor a cero")

        self.roas = round(revenue_generated / self.investment, 2)

        return self.roas

# Método para devolver un diccionario del resultado de la consulta
    def to_dict(self):
        return {
            "id": self.id,
            "campaign_name": self.campaign_name,
            "investment": self.investment,
            "clicks": self.clicks,
            "conversion": self.conversion,
            "roas": self.roas,
            "date_consultation": str(self.date_consultation),
        }