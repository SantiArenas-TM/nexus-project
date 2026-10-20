"""Pruebas unitarias básicas para cálculos de precios y descuentos."""

import pytest      

from src.models.product import product
from src.models.discount_rule import discount_rule
from src.models.campaign_metric import campaign_metric
from src.controllers.discount_controller import discount_controller


def test_suggested_price_uses_30_percent_margin():
    """Un costo total de 70 debe producir un precio sugerido de 100."""
    item = product(1, "Producto demo", 50, 20)
    assert item.CALCULAR_PRECIO() == 100
    assert item.netMargin == pytest.approx(30)


def test_suggested_price_rejects_zero_total_cost():
    """El cálculo no debe aceptar costos totales iguales a cero."""
    item = product(1, "Producto sin costo", 0, 0)
    with pytest.raises(ValueError):
        item.CALCULAR_PRECIO()


def test_discount_applies_when_minimum_quantity_is_reached():
    """Aplica un 10 % al precio de 200 cuando se compran al menos 5 unidades."""
    rule = discount_rule(1, 10, 5, "Compra al por mayor")
    assert rule.apply_discount(5, 200) == 180


def test_discount_does_not_apply_below_minimum_quantity():
    """Mantiene el precio base cuando no se alcanza la cantidad mínima."""
    rule = discount_rule(1, 10, 5, "Compra al por mayor")
    assert rule.apply_discount(4, 200) == 200


def test_discount_controller_applies_rules_in_sequence():
    """Dos descuentos sucesivos del 10 % convierten 100 en 81."""
    controller = discount_controller()
    controller.create_rule(1, 10, 1, "Primera regla")
    controller.create_rule(2, 10, 1, "Segunda regla")
    assert controller.apply_discounts_to_price(1, 100) == pytest.approx(81)


def test_roas_is_revenue_divided_by_investment():
    """Ingresos de 500 e inversión de 100 deben dar un ROAS de 5."""
    metric = campaign_metric(1, "Campaña demo", 100, 20, 5)
    assert metric.calculate_ROAS(500) == 5


def test_roas_rejects_zero_investment():
    """El ROAS no se puede calcular con inversión cero."""
    metric = campaign_metric(1, "Campaña demo", 0, 20, 5)
    with pytest.raises(ValueError):
        metric.calculate_ROAS(500)
