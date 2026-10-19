from src.models.campaign_metric import campaign_metric


class metric_controller:
    def __init__(self):
        self.metrics = []

# Método para registrar una nueva metrica y calcular el ROAS
    def register_metric(self, id, campaign_name, investment, clicks, conversion, revenue_generated):
        new_metric = campaign_metric(id, campaign_name, investment, clicks, conversion)
        new_metric.calculate_ROAS(revenue_generated)
        self.metrics.append(new_metric)

        return new_metric.to_dict()

# Método para obtener todas las metricas registradas
    def get_all(self):
        return [current_metric.to_dict() for current_metric in self.metrics]