\# Taller 5 · Diagrama de clases

  

\- \*\*Entrega:\*\* en el \*\*repositorio del equipo en GitHub\*\*, diligenciando el enunciado con los puntos 2, 3 y 4 y subiendo el diagrama al repositorio \*(imagen exportada o fuente PlantUML/draw.io)\*.

\- \*\*Requisito previo:\*\* diagrama de casos de uso del Taller 4.

\- Herramienta: draw.io, PlantUML, StarUML o Visual Paradigm.

  

\---

  

\## 1. Guía mínima

  

\*\*Diagrama de clases:\*\* vista estructural del sistema. Muestra qué cosas existen en el dominio, qué datos guardan, qué saben hacer y cómo se relacionan. No muestra orden ni tiempo: eso es de los diagramas de secuencia.

  

\### Clase

  

\`\`\`bash

┌──────────────────────┐

│ Turno │ ← nombre: sustantivo singular, del vocabulario del dominio

├──────────────────────┤

│ - fecha: Fecha │ ← atributos: visibilidad nombre: tipo

│ - estado: EstadoTurno│

├──────────────────────┤

│ + cancelar(): void │ ← métodos: visibilidad nombre(parámetros): retorno

└──────────────────────┘

-   **Visibilidad:** `+` pública, `-` privada, `#` protegida, `~` de paquete. Los atributos van privados por defecto.
-   En el **modelo de dominio** se pueden omitir los métodos: importan los conceptos, sus datos y sus relaciones.
-   Una clase **no es una pantalla, una tabla ni un botón**. `PantallaLogin` o `BotonGuardar` no son conceptos del dominio.

### Relaciones

| Relación    | Notación                                  | Se lee                           | Ejemplo                  |
| ----------- | ----------------------------------------- | -------------------------------- | ------------------------ |
| Asociación  | línea simple                              | "A se relaciona con B"           | Cliente — Turno          |
| Agregación  | rombo vacío en el todo                    | "A tiene B, pero B existe sin A" | Barbería ◇— Barbero      |
| Composición | rombo lleno en el todo                    | "B es parte de A y muere con A"  | Factura ◆— LíneaFactura  |
| Herencia    | flecha con triángulo vacío hacia el padre | "B es un tipo de A"              | Usuario ◁— Administrador |
| Dependencia | flecha punteada                           | "A usa a B de paso"              | Reporte ⇢ Turno          |

-   Ante la duda entre agregación y composición: si al borrar el todo **las partes no tienen sentido solas**, es composición.
-   Herencia solo si el hijo **es un** padre y comparte su comportamiento. Si solo comparten un campo, no es herencia.

### Multiplicidad

Se escribe en cada extremo de la relación: cuántos objetos de ese lado se relacionan con **uno** del otro.

| Notación | Significa       |
| -------- | --------------- |
| 1        | exactamente uno |
| 0..1     | cero o uno      |
| * o 0..* | cero o muchos   |
| 1..*     | uno o muchos    |

-   `Cliente 1 —— 0..* Turno`: un cliente tiene cero o muchos turnos; cada turno es de exactamente un cliente.
-   Una relación sin multiplicidad está incompleta.

### Navegabilidad

-   Flecha abierta en un extremo: desde A se llega a B, pero no al revés.
-   En el modelo de dominio se puede dejar sin flecha *(bidirecional)*; se decide en el diseño.

### Cómo encontrar las clases

1.  Subrayar los **sustantivos** del catálogo de requisitos y de las descripciones de los casos de uso.
2.  Descartar sinónimos, atributos disfrazados *(el "nombre" no es una clase)*, actores que no guardan datos y cosas fuera del alcance.
3.  Lo que queda son **clases candidatas**. Los **verbos** entre ellas sugieren relaciones.

## 2\. Clases candidatas

| Clase candidata  | Fuente (RF o caso de uso) | ¿Se queda? | Por qué                                                                                                       |
| ---------------- | ------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------- |
| Dropshipper      | RF-01, CU-01              | Sí         | Es el usuario principal del sistema; guarda datos de cuenta, perfil y autenticación.                          |
| MetricaCampana   | RF-01, CU-01              | Sí         | Almacena los indicadores de Facebook Ads (inversión, clics, conversiones, ROAS, fecha).                       |
| Producto         | RF-03, CU-03              | Sí         | Entidad central que almacena costos de adquisición, flete, precio sugerido y margen neto.                     |
| LandingPageIA    | RF-02, CU-02              | Sí         | Entidad que guarda el resultado generado por el modelo de IA (título, copy, plantilla, estado).               |
| SeguimientoEnvio | RF-05, CU-05              | Sí         | Registra el estado de rastreo, transportadora, código de seguimiento y cliente final.                         |
| ReglaDescuento   | RF-04, CU-04              | Sí         | Procesa y almacena las reglas y ofertas por cantidad parametrizadas desde la plantilla cargada.               |
| PlantillaExcel   | RF-04, CU-04              | No         | Es un archivo/medio de entrada de datos para la configuración, no una entidad del dominio.                    |
| FacebookAPI      | RF-01, CU-01              | No         | Corresponde a un servicio/cliente de integración externo, no a un concepto del dominio.                       |
| ProveedorIA      | RF-02, CU-02              | No         | Es un actor/servicio externo que procesa solicitudes; la entidad del dominio es el resultado (LandingPageIA). |

-   **Mínimo 6 clases** que se quedan.
-   Toda clase lleva fuente. Una clase que no sale de ningún requisito o caso de uso no está en el alcance.

## 3\. Diagrama de clases del dominio

Un solo diagrama con:

-   **Mínimo 6 clases**, con atributos y tipos.
-   **Mínimo 5 relaciones**, cada una con multiplicidad en los dos extremos.
-   Al menos **una composición o agregación** y, si el dominio lo justifica, una **herencia**.

## 4\. Trazabilidad y dudas

**Columna de clase de la matriz**

| Requisito | Caso de uso | Clase(s)                      |
| --------- | ----------- | ----------------------------- |
| RF-01     | CU-01       | Dropshipper, MetricaCampana   |
| RF-02     | CU-02       | Producto, LandingPageIA       |
| RF-03     | CU-03       | Dropshipper, Producto         |
| RF-04     | CU-04       | Producto, ReglaDescuento      |
| RF-05     | CU-05       | Dropshipper, SeguimientoEnvio |

-   Cada caso crítico debe apoyarse en al menos una clase del diagrama.

**Dudas para la siguiente clase** *(lo que el equipo no pudo resolver solo)*:

-   **Manejo de estados y reintentos en la persistencia con APIs de IA:** ¿Es recomendable que la clase `LandingPageIA` registre internamente los estados intermedios del procesamiento del modelo (ej. *Pendiente*, *Generado*, *Fallido por Timeout/Cuota*) para manejar reintentos, o es mejor separar el control de reintentos a nivel de servicios del sistema sin reflejarlo en la entidad del dominio?

## Ejemplo diligenciado

**2\. Candidatas**

| Clase candidata | Fuente          | ¿Se queda? | Por qué                                                                   |
| --------------- | --------------- | ---------- | ------------------------------------------------------------------------- |
| Cliente         | RF-01           | Sí         | Reserva y tiene turnos                                                    |
| Turno           | RF-01, CU-01    | Sí         | Concepto central del dominio                                              |
| Barbero         | RF-02           | Sí         | Atiende turnos; tiene agenda                                              |
| Agenda          | P1 (entrevista) | No         | Es la lista de turnos de un barbero en un día: una consulta, no una clase |
| CierreCaja      | RF-05           | Sí         | Guarda el total del día                                                   |
| Teléfono        | RF-01           | No         | Es un atributo de Cliente                                                 |

**3\. Diagrama** *(extracto en PlantUML)*

**4\. Trazabilidad:** RF-01 → CU-01 Reservar turno → Cliente, Turno, Barbero. RF-02 → CU-02 Marcar no asistido → Turno *(estado)*.