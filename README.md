# Ficha de equipo y dominio — Sesión 1

Plantilla de la **actividad de cierre de la Clase 1**. Se diligencia en clase, en equipo, y se entrega al final de la sesión.

- **Equipos:** de 2 a 3 integrantes, fijos durante todo el curso.
- **Entrega:** una ficha por equipo.
- **Cada equipo elige un dominio distinto.**

---

## 1. Identificación del equipo

| Campo | Respuesta |
|---|---|
| Nombre del equipo | _Nexus_ |
| Fecha | _14/09/2026_ |

| # | Integrante | Correo | Rol / responsabilidad |
| --- | --- | --- | --- |
| 1 | _Santiago Arenas Rios_ | _santiagoarenitas@gmail.com_ | Coordinación _Lider_ |
| 2 | _Julian Andres Arebelaez Rios_ | _arbelaezjulianandres@gmail.com_ | _Desarrollador_ |
| 3 | _David Giraldo Henriet_ | _davidgiraldohenriet@gmail.com_ | _Administrativo_ |

> El rol no es definitivo: se ajusta en la bitácora de gestión. Lo que sí queda fijo hoy es **quién coordina**.

---

## 2. Dominio propuesto

**Dominio:** _Software para optimización de tareas para el Dropshipping_

**Problema que se quiere resolver** _Se va a resolver el problema de que los vendedores pueden hacer sus tareas diarías más rápidamente y con una mejor optimización, como visualización de métricas de rendimiento de las campañas de en Facebook ADS, Creación de Landing Pages, Optimización de creativos de los productos, calculadora de precios y demás cálculos que requiere cada producto, ETC..._


**Cómo se hace hoy sin software** _Hoy en día se hace manualmente, ingresando a la página a la página de administrador de anuncios, los creativos se hacen manualmente editandolos con CapCut, los calculos de precios, promociones se hacen en excel manuelmanete, en si, todo le toca a uno ir a mirarlo manualmente según la tarea que deba de hacer_


---

## 3. Usuarios del sistema

| Tipo de usuario | Qué necesita hacer en el sistema | ¿Tenemos acceso para entrevistarlo? |
| --- | --- | --- |
| _Contador_ | _Hacer los calculos de precios_ |  Sí — _Compañero de Clase_ |
| _Editor_ | _Creación de Landings Page_ | No — _No tenemos uno cercano_ |

> Al menos **un usuario real y accesible** es obligatorio: en la Clase 3 hay que hacerle una sesión de elicitación de verdad.

---

## 4. Capacidad del equipo

**¿Por qué este equipo puede levantar requisitos de este dominio?** _(acceso a usuarios reales, alguien trabaja o trabajó ahí, experiencia previa con el proceso, etc.)_

_Mi compañero de clase Santaigo Arenas, tiene una expericia previa en el ambitó del Dropshipping, y el resto del equipo lo está estudiando para poder ejercerlo_

---

## 5. Alcance tentativo

**Tres cosas que el sistema sí debe hacer**:

1. _Visualización de métricas de rendimiento de las campañas de Facebook ADS_
2. _Creación de Landing Pages_
3. _Calculadora de costos por producto_

**Tres cosas que el sistema no va a hacer**:

1. _Gestión de inventario_
2. _Pagos en línea_
3. _Domicilios o Envíos_

---

## 6. Autoverificación

- [✅] Hay **usuarios reales accesibles** para entrevistar en la Clase 3.
- [✅] El dominio da para **10 requisitos funcionales y 5 no funcionales** sin inventarlos.
- [✅] Los **tres casos críticos** se ven implementables end-to-end en seis semanas.
- [✅] El proyecto **no fue desarrollado** en otra asignatura ni se está reciclando.
- [✅] No es demasiado grande _(una red social completa)_ ni demasiado pequeño _(una calculadora)_.
- [❌] El sistema **maneja datos personales**: Sí / No. Si es Sí, aplica la Ley 1581 de 2012 en el numeral 10 de la Nota 1.

---

## Ejemplo diligenciado

Referencia de nivel de detalle esperado. **No se puede usar este dominio.**

- **Dominio:** Optimización de tareas diarias del Dropshipping.
- **Problema:** Los vendedores de Dropshipping pierden mucho tiempo haciendo tareas manuales, como revisar métricas de campañas, crear landing pages y calcular precios de productos. Esto reduce su eficiencia y rentabilidad.
- **Hoy:** Se hace todo manualmente, ingresando a diferentes plataformas, editando creativos con herramientas externas y realizando cálculos en hojas de cálculo.
- **Usuarios:** 
  - Contador: necesita hacer cálculos de precios.
  - Editor: necesita crear landing pages.
- **Capacidad del equipo:** Uno de los integrantes tiene experiencia previa en Dropshipping, y el resto del equipo está estudiando el tema para poder contribuir efectivamente.
- **Sí hace:** 
  - Visualización de métricas de rendimiento de campañas de Facebook ADS.
  - Creación de landing pages.
  - Calculadora de costos por producto.
- **No hace:** pagos en línea, domicilios, inventario de productos.

---

## Flujo del Proyecto

```bash
UI → Controlador → ServicioIA «interfaz» → AdaptadorProveedor → API del modelo → AdaptadorSimulado → respuesta fija (pruebas)
```