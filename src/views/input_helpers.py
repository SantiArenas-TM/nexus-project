"""Shared input validation and output helpers for all console views."""

import math
import re
from datetime import datetime

MAX_TEXT_LENGTH = 60
TRACKING_CODE_PATTERN = re.compile(r"^[A-Za-z0-9-]{4,30}$")


def print_title(title):
    print("\n" + "=" * 50)
    print(f" {title}")
    print("=" * 50)


def read_text(prompt, allow_empty=False, max_length=MAX_TEXT_LENGTH):
    """Ask for text; reject empty values (unless allowed) and overly long ones."""
    while True:
        value = input(prompt).strip()
        if not value and not allow_empty:
            print("  ✗ Este campo no puede estar vacío.")
        elif len(value) > max_length:
            print(f"  ✗ Máximo {max_length} caracteres.")
        else:
            return value


def read_int(prompt, minimum=None, maximum=None):
    """Ask for an integer within optional bounds."""
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("  ✗ Este campo no puede estar vacío.")
            continue
        try:
            value = int(raw)
        except ValueError:
            print("  ✗ Ingrese un número entero válido (sin letras ni decimales).")
            continue
        if minimum is not None and value < minimum:
            print(f"  ✗ El valor mínimo permitido es {minimum}.")
        elif maximum is not None and value > maximum:
            print(f"  ✗ El valor máximo permitido es {maximum}.")
        else:
            return value


def read_float(prompt, minimum=0.0, maximum=None, allow_minimum=True):
    """Ask for a decimal number. Accepts comma or dot as decimal separator."""
    while True:
        raw = input(prompt).strip().replace(",", ".")
        if not raw:
            print("  ✗ Este campo no puede estar vacío.")
            continue
        try:
            value = float(raw)
        except ValueError:
            print("  ✗ Ingrese un número válido (ejemplo: 12.50).")
            continue
        if not math.isfinite(value):
            print("  ✗ Ingrese un número válido.")
        elif value < minimum or (value == minimum and not allow_minimum):
            comparison = "mayor o igual a" if allow_minimum else "mayor que"
            print(f"  ✗ El valor debe ser {comparison} {minimum:g}.")
        elif maximum is not None and value > maximum:
            print(f"  ✗ El valor máximo permitido es {maximum:g}.")
        else:
            return value


def read_unique_id(prompt, existing_ids):
    """Ask for a positive integer ID that is not already in use."""
    while True:
        value = read_int(prompt, minimum=1)
        if value in existing_ids:
            print(f"  ✗ El ID {value} ya existe. Ingrese uno distinto.")
        else:
            return value


def read_tracking_code(prompt, taken_codes=None):
    """Ask for a tracking code (letters, digits and hyphens). Returns it in uppercase."""
    taken = {code.upper() for code in (taken_codes or [])}
    while True:
        value = input(prompt).strip()
        if not value:
            print("  ✗ Este campo no puede estar vacío.")
        elif not TRACKING_CODE_PATTERN.match(value):
            print("  ✗ Use de 4 a 30 caracteres: letras, números y guiones (sin espacios).")
        elif value.upper() in taken:
            print("  ✗ Ese código de seguimiento ya está registrado.")
        else:
            return value.upper()


def read_date(prompt):
    """Ask for a date in YYYY-MM-DD format and return a datetime.date."""
    while True:
        raw = input(prompt).strip()
        try:
            return datetime.strptime(raw, "%Y-%m-%d").date()
        except ValueError:
            print("  ✗ Fecha inválida. Use el formato AAAA-MM-DD (ejemplo: 2026-10-19).")


def read_option(prompt, valid_options):
    """Ask until the user types one of the valid options."""
    valid = [str(option).lower() for option in valid_options]
    while True:
        value = input(prompt).strip().lower()
        if value in valid:
            return value
        print(f"  ✗ Opción inválida. Elija una de: {', '.join(valid)}.")


def read_from_menu(title, options):
    """Show a numbered menu built from {value: label} and return the chosen value."""
    values = list(options.keys())
    print(title)
    for number, value in enumerate(values, start=1):
        print(f"  {number}. {options[value]}")
    choice = read_int("Seleccione una opción: ", minimum=1, maximum=len(values))
    return values[choice - 1]


def confirm(prompt):
    return read_option(f"{prompt} (s/n): ", ["s", "n"]) == "s"


def format_money(amount):
    return f"${amount:,.2f}"


def request_data(client, command, payload=None):
    """Send a command to the backend.

    Returns (True, data) when the backend answers OK, or (False, None) after
    printing the error. A tuple is used because valid data can be falsy
    (an empty list, 0.0 or False).
    """
    response = client.send_command(command, payload)

    if not isinstance(response, dict) or response.get("status") != "OK":
        message = response.get("data") if isinstance(response, dict) else None
        print(f"\n[ERROR] {message or 'Respuesta inválida del servidor.'}")
        return False, None
    return True, response.get("data")