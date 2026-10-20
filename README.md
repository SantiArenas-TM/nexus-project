# Nexus - Software para optimización de tareas de Dropshipping

Nexus es una aplicación académica en Python que reúne funciones para administrar productos y calcular precios sugeridos, crear descuentos por cantidad, registrar métricas de campañas publicitarias y hacer seguimiento de envíos.

## Arquitectura

El proyecto sigue una separación inspirada en **MVC**:

- `src/models/`: entidades y reglas de negocio (`product`, `discount_rule`, `campaign_metric`, `shipment_tracking`).
- `src/controllers/`: administra las entidades en memoria y expone operaciones de creación, consulta y actualización.
- `src/views/`: interfaz de consola, validación de entradas y presentación de resultados.
- `src/client/`: cliente TCP que envía comandos JSON al servidor.
- `src/server/`: servidor TCP que interpreta los comandos, llama a los controladores y responde en JSON.
- `src/main.py`: aplicación FastAPI independiente con una ruta básica de comprobación.

**Comunicación:** el cliente y el servidor TCP usan por defecto `127.0.0.1:65432`. Cada petición contiene `comando` y `payload`; la respuesta contiene `status` y `data`.

> Nota: los controladores guardan los datos en memoria. Al detener el servidor, los registros creados se pierden; todavía no hay una base de datos persistente.

## Requisitos

- Python `3.14` o superior, según `pyproject.toml`.
- [`uv`](https://docs.astral.sh/uv/) instalado.
- Git (opcional, para clonar el repositorio).

## Instalación

Desde la carpeta raíz del repositorio:

```bash
uv sync
```

Este comando crea/actualiza el entorno virtual y sincroniza las dependencias definidas en `pyproject.toml` y `uv.lock`.

Si el proyecto no se ha descargado todavía:

```bash
git clone <URL_DEL_REPOSITORIO>
cd nexus-project-main
uv sync
```

Reemplaza `<URL_DEL_REPOSITORIO>` por la dirección real del repositorio del equipo.

## Ejecutar el servidor y el cliente

Abre **dos terminales** en la raíz del proyecto.

**Terminal 1 — servidor TCP:**

```bash
uv run python -m src.server.main_server
```

Deberías ver un mensaje indicando que el servidor está escuchando en `127.0.0.1:65432`.

**Terminal 2 — cliente de consola:**

```bash
uv run python -m src.client.main_client
```

Usa los menús para administrar productos, métricas, descuentos y envíos. Inicia siempre el servidor antes que el cliente.

Para cambiar el host o puerto del servidor al que se conecta el cliente, configura `NEXUS_HOST` y `NEXUS_PORT` en el entorno antes de ejecutar el cliente. El servidor, por su parte, actualmente define `HOST` y `PORT` en `src/server/main_server.py`, por lo que deben coincidir.

## Ejecutar la API FastAPI opcional

`src/main.py` define una API FastAPI mínima, distinta del servidor TCP principal:

```bash
uv run uvicorn src.main:app --reload
```

Luego visita `http://127.0.0.1:8000/`. La ruta raíz devuelve un JSON con el mensaje `nexus`.

## Pruebas

Las pruebas unitarias de reglas de precios y descuentos están en `tests/`. Ejecuta:

```bash
uv run pytest
```

Las pruebas no necesitan iniciar el servidor TCP porque prueban directamente los modelos y controladores.

## Reglas de cálculo verificadas

- **Precio sugerido:** costo total dividido por `1 - margen deseado`. El margen predeterminado es 30%; por ejemplo, con costo total de 70, el precio sugerido es 100.
- **Margen neto por unidad:** precio sugerido menos costo total.
- **ROAS:** ingresos generados divididos por inversión publicitaria; la inversión debe ser mayor que cero.
- **Descuento por cantidad:** cada regla se aplica cuando la cantidad alcanza el mínimo configurado. Si hay varias reglas, el controlador las aplica en secuencia sobre el precio resultante de la regla anterior.

## Estructura principal

```text
src/
├── client/main_client.py
├── controllers/
├── models/
├── server/main_server.py
├── views/
└── main.py
tests/
```
