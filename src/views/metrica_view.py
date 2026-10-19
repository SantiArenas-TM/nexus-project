"""Console view for Facebook Ads campaign metrics (RF-01)."""

from datetime import datetime

from src.views.input_helpers import (
    format_money, print_title, read_date, read_float, read_int,
    read_option, read_text, read_unique_id, request_data,
)


def fetch_metrics(client):
    """Return the list of campaign metrics, or None if the request failed."""
    success, metrics = request_data(client, "OBTENER_METRICAS")
    return metrics if success else None


def _registration_date(metric):
    """The backend sends date_consultation as 'YYYY-MM-DD HH:MM:SS.ffffff'."""
    return datetime.strptime(metric["date_consultation"][:10], "%Y-%m-%d").date()


def _print_metrics_table(metrics):
    print(
        f"\n{'ID':<5}{'Campaña':<24}{'Inversión':>12}{'Clics':>8}"
        f"{'Conv.':>7}{'ROAS':>8}  {'Fecha'}"
    )
    print("-" * 78)
    for metric in metrics:
        print(
            f"{metric['id']:<5}{metric['campaign_name'][:22]:<24}"
            f"{format_money(metric['investment']):>12}{metric['clicks']:>8}"
            f"{metric['conversion']:>7}{metric['roas']:>8.2f}  {metric['date_consultation'][:10]}"
        )


def _print_summary(metrics):
    """Consolidated indicators calculated from the returned records."""
    total_investment = sum(metric["investment"] for metric in metrics)
    total_clicks = sum(metric["clicks"] for metric in metrics)
    total_conversions = sum(metric["conversion"] for metric in metrics)
    # The backend only returns ROAS (revenue / investment), so revenue is rebuilt from it.
    estimated_revenue = sum(metric["roas"] * metric["investment"] for metric in metrics)

    consolidated_roas = estimated_revenue / total_investment
    roi_percent = (estimated_revenue - total_investment) / total_investment * 100
    cpa_text = (
        format_money(total_investment / total_conversions) if total_conversions else "N/A"
    )

    print("\n--- Indicadores consolidados ---")
    print(f"Campañas:                {len(metrics)}")
    print(f"Inversión total:         {format_money(total_investment)}")
    print(f"Ingresos estimados:      {format_money(estimated_revenue)}")
    print(f"ROAS consolidado:        {consolidated_roas:.2f}")
    print(f"ROI:                     {roi_percent:.1f}%")
    print(f"Clics / Conversiones:    {total_clicks} / {total_conversions}")
    print(f"Costo por adquisición:   {cpa_text}")


def _show_metrics(metrics, empty_message):
    if not metrics:
        print(f"\n{empty_message}")
        return
    _print_metrics_table(metrics)
    _print_summary(metrics)


def _register_metric(client):
    print_title("REGISTRAR MÉTRICA DE CAMPAÑA")
    metrics = fetch_metrics(client)
    if metrics is None:
        return

    existing_ids = {metric["id"] for metric in metrics}
    metric_id = read_unique_id("ID de la métrica: ", existing_ids)
    campaign_name = read_text("Nombre de la campaña: ")
    investment = read_float("Inversión publicitaria: ", minimum=0, allow_minimum=False)
    clicks = read_int("Clics: ", minimum=0)
    conversions = read_int(f"Conversiones/ventas (0-{clicks}): ", minimum=0, maximum=clicks)
    revenue_generated = read_float("Ingresos generados: ", minimum=0)

    payload = {
        "id": metric_id,
        "campaign_name": campaign_name,
        "investment": investment,
        "clicks": clicks,
        "conversion": conversions,
        "revenue_generated": revenue_generated,
    }
    success, created = request_data(client, "REGISTRAR_METRICA", payload)
    if success:
        print(f"\n✓ Métrica registrada. ROAS calculado: {created['roas']:.2f}")


def _list_metrics(client):
    print_title("MÉTRICAS DE CAMPAÑAS")
    metrics = fetch_metrics(client)
    if metrics is not None:
        _show_metrics(metrics, "No hay métricas registradas.")


def _filter_by_campaign(client):
    print_title("FILTRAR POR CAMPAÑA")
    metrics = fetch_metrics(client)
    if metrics is None:
        return
    text = read_text("Nombre (o parte del nombre) de la campaña: ").lower()
    matches = [metric for metric in metrics if text in metric["campaign_name"].lower()]
    _show_metrics(matches, "Ninguna campaña coincide con ese nombre.")


def _filter_by_dates(client):
    print_title("FILTRAR POR RANGO DE FECHAS")
    metrics = fetch_metrics(client)
    if metrics is None:
        return
    start_date = read_date("Fecha inicial (AAAA-MM-DD): ")
    end_date = read_date("Fecha final   (AAAA-MM-DD): ")
    while end_date < start_date:
        print("  ✗ La fecha final no puede ser anterior a la inicial.")
        end_date = read_date("Fecha final   (AAAA-MM-DD): ")

    matches = [m for m in metrics if start_date <= _registration_date(m) <= end_date]
    _show_metrics(
        matches,
        "No hay registros en ese rango de fechas. Pruebe con un rango distinto.",
    )


def show_metric_menu(client):
    actions = {
        "1": _register_metric,
        "2": _list_metrics,
        "3": _filter_by_campaign,
        "4": _filter_by_dates,
    }
    while True:
        print_title("MÉTRICAS DE CAMPAÑAS")
        print("1. Registrar métrica de campaña")
        print("2. Ver todas las métricas")
        print("3. Filtrar por campaña")
        print("4. Filtrar por rango de fechas")
        print("0. Volver al menú principal")
        option = read_option("Seleccione una opción: ", ["0", "1", "2", "3", "4"])
        if option == "0":
            return
        actions[option](client)