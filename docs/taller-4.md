# Taller 4 · Casos de uso

## 1. Actores y casos

**Actores**

| Actor | Tipo | Principal o secundario | Objetivo en el sistema |
| --- | --- | --- | --- |
| Dropshipper | Humano | Principal | Gestionar métricas, calcular precios de venta y generar contenidos publicitarios para su negocio. |
| Proveedor de IA | Sistema externo | Secundario | Generar los borradores de texto estructurado para las landing pages y copys. |

**Casos de uso**

| ID | Nombre | Actor principal | RF que cubre |
| --- | --- | --- | --- |
| CU-01 | Consultar métricas de campañas de Facebook Ads | Dropshipper | RF-01 |
| CU-02 | Generar Landing Page con IA | Dropshipper | RF-02 |
| CU-03 | Calcular costos, márgenes y precios | Dropshipper | RF-03 |
| CU-04 | Aplicar automatización de descuentos | Dropshipper | RF-04 |
| CU-05 | Rastrear envíos de productos | Dropshipper | RF-05 |
| CU-06 | Exportar reporte de rentabilidad | Dropshipper | RF-03 |

---

## 2. Diagrama de casos de uso

**Imagen o enlace al diagrama:** `![Diagrama de Casos de Uso](./diagrama-casos-de-uso.png)`

**Justificación de las relaciones:**
- **CU-03 `«extend»` CU-06:** Al ejecutar *Calcular costos, márgenes y precios* (CU-03), el usuario puede opcionalmente *Exportar un reporte de rentabilidad* (CU-06) si requiere un informe descargable del cálculo realizado.

---

## 3. Casos críticos

| Caso | Por qué es crítico *(valor / frecuencia / riesgo técnico)* |
| --- | --- |
| **CU-03** Calcular costos, márgenes y precios | **Valor y frecuencia elevosa:** Es la herramienta de uso diario indispensable para que el dropshipper determine si un producto es rentable antes de pautar; requiere lógica de cálculo de punta a punta y persistencia. |
| **CU-01** Consultar métricas de campañas de Facebook Ads | **Riesgo técnico y valor:** Consume datos de campañas, procesa agregaciones financieras en tiempo real y persiste históricos para la toma de decisiones publicitarias. |
| **CU-02** Generar Landing Page con IA | **Caso de IA y diferenciador principal:** Integra la comunicación con el modelo externo de IA para transformar datos de producto en una landing optimizada para ventas. |

---

## 4. Descripción detallada de los casos críticos

### Caso Crítico 1: CU-03 Calcular costos, márgenes y precios

| Campo | Contenido |
| --- | --- |
| **ID y nombre** | CU-03 Calcular costos, márgenes y precios |
| **Actor principal** | Dropshipper |
| **Actores secundarios** | — |
| **Requisitos que cubre** | RF-03, RNF-02, RNF-03 |
| **Precondiciones** | El dropshipper ha ingresado a la sección de la calculadora en la plataforma. |
| **Disparador** | El dropshipper ingresa los costos del producto y presiona la opción de calcular. |
| **Frecuencia** | Múltiples veces al día (frecuencia alta al evaluar nuevos productos). |

**Flujo principal**
1. El dropshipper ingresa el costo de adquisición del producto, costo estimado de envío y porcentaje de comisión o plataforma.
2. El sistema valida que todos los montos ingresados sean numéricos y superiores a cero.
3. El sistema calcula automáticamente el precio de venta sugerido, el margen de ganancia neto y el punto de equilibrio.
4. El sistema muestra en pantalla el desglose financiero en tiempo real.
5. El sistema guarda la consulta realizada en el historial del usuario.

**Flujos alternos**
- **3a.** El dropshipper ajusta manualmente el precio de venta deseado: el sistema recalcula el margen proyectado en tiempo real y vuelve al paso 4.

**Excepciones**
- **2a.** El dropshipper ingresa un valor negativo, cero o texto no numérico: el sistema muestra un mensaje de alerta indicando que no se pueden procesar valores inválidos y detiene el proceso hasta que se corrijan los datos.

**Postcondiciones**
- **Éxito:** El cálculo de costos y precios queda registrado en la base de datos y visible para el usuario.
- **Garantía mínima:** Ningún cálculo erróneo con valores negativos o divisiones por cero es procesado o guardado.

---

### Caso Crítico 2: CU-01 Consultar métricas de campañas de Facebook Ads

| Campo | Contenido |
| --- | --- |
| **ID y nombre** | CU-01 Consultar métricas de campañas de Facebook Ads |
| **Actor principal** | Dropshipper |
| **Actores secundarios** | — |
| **Requisitos que cubre** | RF-01, RNF-02, RNF-03 |
| **Precondiciones** | Existen registros de campañas publucitarias en la plataforma. |
| **Disparador** | El dropshipper selecciona el rango de fechas a consultar en el panel central. |
| **Frecuencia** | Varias veces al día. |

**Flujo principal**
1. El dropshipper selecciona el rango de fechas y solicita la consulta de métricas.
2. El sistema recupera los registros de inversión publicitaria, clics, ventas y costo por adquisición (CPA) almacenados.
3. El sistema calcula los indicadores consolidados de ROAS (Retorno de la Inversión Publicitaria) y ROI.
4. El sistema presenta el panel centralizado con los gráficos y métricas consolidadas.
5. El sistema guarda el filtro de consulta aplicado para la sesión actual del usuario.

**Flujos alternos**
- **1a.** El dropshipper aplica un filtro específico por campaña: el sistema filtra los datos exclusivamente para esa campaña y continúa en el paso 2.

**Excepciones**
- **2a.** No existen datos para el rango de fechas seleccionado: el sistema notifica que no hay registros disponibles y sugiere cambiar el rango de fechas.

**Postcondiciones**
- **Éxito:** El panel presenta las métricas consolidadas en tiempo real.
- **Garantía mínima:** Se visualizan únicamente los datos correspondientes a las campañas del usuario autenticado.

---

### Caso Crítico 3: CU-02 Generar Landing Page con IA

| Campo | Contenido |
| --- | --- |
| **ID y nombre** | CU-02 Generar Landing Page con IA |
| **Actor principal** | Dropshipper |
| **Actores secundarios** | Proveedor de IA |
| **Requisitos que cubre** | RF-02, RNF-01, RNF-02 |
| **Precondiciones** | El dropshipper dispone de la información básica de un producto. |
| **Disparador** | El dropshipper completa el formulario de solicitud de landing y presiona generar. |
| **Frecuencia** | Diaria (según la cantidad de lanzamientos de productos). |

**Flujo principal**
1. El dropshipper ingresa el nombre del producto, costo, público objetivo y beneficio principal.
2. El sistema valida los datos y envía la solicitud estructurada al Proveedor de IA sin incluir información sensible ni datos personales.
3. El Proveedor de IA genera el contenido estructurado (títulos, beneficios, llamados a la acción) y lo retorna al sistema.
4. El sistema procesa la respuesta, construye la vista previa de la Landing Page y se la muestra al dropshipper.
5. El dropshipper aprueba la estructura y el sistema guarda la Landing Page en su catálogo activo.

**Flujos alternos**
- **5a.** El dropshipper edita el texto directamente en el previsualizador: el sistema actualiza la plantilla localmente y continúa en el paso 5.

**Excepciones**
- **3a.** Ocurre un tiempo de espera agotado (timeout > 10s), error HTTP 429 de cuota agotada o respuesta malformada del Proveedor de IA: el sistema notifica al usuario que el servicio de IA no está disponible momentáneamente, carga de forma predeterminada una plantilla de landing gratuita base sin costo adicional y permite continuar la edición manual.

**Postcondiciones**
- **Éxito:** La Landing Page queda guardada y lista para su publicación.
- **Garantía mínima:** Cumplimiento del RNF-01 (ningún dato personal o sensible del cliente o usuario es enviado al Proveedor de IA).

---

## 5. Trazabilidad

**Matriz de trazabilidad**

| Requisito | Fuente | Caso de uso |
| --- | --- | --- |
| RF-01 | Catálogo de Requisitos | CU-01 Consultar métricas de campañas de Facebook Ads |
| RF-02 | Catálogo de Requisitos | CU-02 Generar Landing Page con IA |
| RF-03 | Catálogo de Requisitos | CU-03 Calcular costos, márgenes y precios |
| RF-03 | Catálogo de Requisitos | CU-06 Exportar reporte de rentabilidad |
| RF-04 | Catálogo de Requisitos | CU-04 Aplicar automatización de descuentos |
| RF-05 | Catálogo de Requisitos | CU-05 Rastrear envíos de productos |

**Huecos detectados:**

| Hueco | Cuál | Qué se hace |
| --- | --- | --- |
| RF sin caso de uso | Ninguno | Todos los RF del catálogo tienen al menos un caso de uso asociado. |
| Caso de uso sin RF | CU-06 | El caso de uso se apoya y cubre la salida de información del requisito RF-03. |