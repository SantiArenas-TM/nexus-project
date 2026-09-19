# Taller  2· Metodología y tablero

Enunciado del **Taller 2**. Se trabaja en clase, en equipo, y se entrega al final de la sesión.

- **Entrega:** un documento por equipo con los puntos 1, 2, 3 y 5, más el **enlace al tablero** del punto 4 con el docente invitado.
- **Nota:** cuenta dentro de los Talleres 1 a 6 *(60% del Seguimiento)*. **No es recuperable**: se califica con la asistencia y el trabajo hecho en la sesión.
- **Requisito previo:** ficha de dominio aprobada en el primer taller. Si quedó con ajustes, se resuelven en los primeros 5 minutos.
- Lo que se produce aquí se reutiliza: la justificación pasa al **numeral 5** de la Nota 1 y el tablero con su acta abren la **bitácora de gestión**.

---

## 1. Caracterización del dominio

Ubicar el proyecto en cada factor **con un dato concreto del dominio**, no con una opinión. Una celda que dice "medio" sin evidencia no cuenta.

| Factor | Valoración *(ágil ← → plan)* | Evidencia del dominio |
| --- | --- | --- |
| Tamaño | *ágil* | *Equipo pequeño conformado por 3 desarroladores* |
| Criticidad | *ágil* | *Criticidad baja-media; fallas imprevistas generan molestias en la usabilidad y posibles pequeñas pérdidas económicas recuperables para el usuario |
| Dinamismo de los requisitos | *ágil* | *Requisitos altamente dinámicos y cambiantes debido a la evolución constante de las herramientas e IA en el mercado del e-commerce* |
| Personal *(experiencia del equipo)* | *plan* | *Equipo nivel Junior. Requiere disciplina y guía estructural* |
| Cultura *(del cliente u organización)* | *ágil* | *Cultura con alta toleracia con el riesgo de errores y al fracaso* |
| Acceso al cliente | *ágil* | *El cliente puede esta disponible diariamente y a timepo completo para solucionar todo dudas y validaciones sobre el software* |
| Regulación | *plan* | *No maneja tratamiento de datos personales sensibles ni normativas estrictas de regulaciones legales complejas* |

---

## 2. Selección y justificación

**Metodología elegida:** *Scrum*

**Justificación** *(un párrafo que cite al menos tres factores del punto 1)*:

*Elegimos Scrum porque nos permite iterar rápidamente en ciclos cortos (Sprints) para responder a los cambios constantes del usuario final y corregir errores a tiempo. Además, nos ayuda a organizar mejor nuestro flujo de trabajo, mantener tareas claras a corto plazo y realizar una supervisión constante sobre la evolución del código entre los tres integrantes del equipo*

**Alternativas descartadas** *(mínimo dos)*:

| Alternativa | Por qué no encaja en este dominio |
| --- | --- |
| *Cascada* | *Exige requisitos fijos e inmutables desde la fase inicial, lo cual no se adapta a la alta volatilidad de las funciones que requiere una plataforma para dropshippers ni al aprendizaje continuo del equipo* |
| *Kanban* | *Aunque gestiona el flujo de trabajo continuo, no proporciona la estructura estricta de tiempo (Sprints) ni los roles definidos que necesitamos para mantener el control y supervisión regular del avance* |

> "Porque es la más usada" o "porque es flexible" no son justificaciones: no dicen nada del dominio.

---

## 3. Adaptación

Explicar cómo se organiza el equipo **dentro** de ellas.

| Campo | Respuesta |
| --- | --- |
| Duración de la iteración *(o "flujo continuo")* | *2 Semanas* |
| Eventos o reuniones y cuándo se hacen | *Sprint Planning: Al inicio de cada Sprint (cada 2 semanas). Daily Standup: Diario (reuniones breves de seguimiento y sync de avances). Sprint Review & Retrospective: Al finalizar cada Sprint (cada 2 semanas), coincidiendo con las sesiones presenciales de clase.* |
| Cómo se llega a la primera entrega | *La primera entrega presentará el Producto Mínimo Viable (MVP) enfocado en la estructura base de la plataforma web, el módulo de cálculo de precios y métricas publicitarias esenciales* |

**Roles asignados** *(ajustar los nombres a la metodología elegida)*:

| Integrante | Rol | Qué hace en la práctica |
| --- | --- | --- |
| *Julián Andrés Arbeláez Rios* | *Product Owner* | *Define y prioriza el backlog del producto según las necesidades de los dropshippers, valida los requisitos y acepta las entregas.* |
| *Santiago Arenas Ríos* | *Scrum Master* | *Remueve bloqueos del equipo, facilita los eventos/reuniones de Scrum y vela por el cumplimiento del flujo de trabajo acordado.* |
| *David Giraldo Henriet* | *Desarrollador* | *Implementa la lógica, frontend, backend e integración con APIs/IA para la plataforma.* |

**Definición de Hecho** *(mínimo tres condiciones verificables para que una tarjeta pase a Hecho)*:

1. *El código de la funcionalidad ha sido subido y fusionado en el repositorio de GitHub.*
2. *La tarea cuenta con pruebas locales que verifican su correcto funcionamiento y la ausencia de errores críticos.*
3. *El incremento ha sido revisado y verificado por todos los integrantes del equipo (notificando y corrigiendo posibles mejoras antes del despliegue).*

---

## 4. Tablero y backlog inicial

Crear el tablero en **GitHub Projects**, Trello o Jira e **invitar al docente**.

**Mínimos del tablero:**

- Columnas: *Backlog · Por hacer · En progreso · En revisión · Hecho* *(o equivalentes, justificadas)*.
- **Límite de WIP** declarado en *En progreso*.
- **Mínimo 10 tarjetas** con el trabajo hasta la Nota 1 *(Clase 4)*. Los requisitos del producto todavía no existen: el backlog de hoy es de **tareas del proyecto** *(preparar la entrevista, redactar el problema, catalogar RF y RNF, armar la sustentación…)*.
- Cada tarjeta con **responsable, estimación** *(horas o puntos)* y **fecha límite**.
- **Todos los integrantes** con al menos una tarjeta asignada.

**Enlace al tablero:** *https://github.com/users/SantiArenas-TM/projects/1*

**Método de estimación usado:** *Por horas dependiendo del tiempo de cada uno*

---

## 5. Primera acta

Primera entrada de la bitácora de gestión.

| Campo | Respuesta |
| --- | --- |
| Fecha | *14/09/2026* |
| Asistentes | *Julián Andrés Arbeláez, Santiago Arenas Ríos, David Giraldo Henriet.* |
| Decisiones tomadas | *1. Adopción del marco de trabajo Scrum con Sprints de 2 semanas. 2. Uso de GitHub Projects como herramienta oficial para el tablero y gestión del Backlog. 3. Elección de Python como lenguaje base para el desarrollo del backend y la lógica de la plataforma.* |
| Compromisos *(quién, qué)* | *• Julián Arbeláez (PO): Redactar y priorizar las primeras historias de usuario en el Backlog de GitHub Projects. • Santiago Arenas (SM): Configurar la estructura del tablero en GitHub Projects y establecer el flujo de ramas en el repositorio. • David Giraldo (Dev): Inicializar la arquitectura base del proyecto en Python y preparar el entorno de desarrollo local.* |
| Bloqueos o riesgos | *Sprint Planning 1 y definición detallada del primer incremento* |

## Ejemplo diligenciado

Referencia de nivel de detalle. Mismo dominio del ejemplo de la ficha: **no se puede usar.**

**1. Caracterización** *(barbería de barrio con tres sillas)*

| Factor | Valoración | Evidencia |
| --- | --- | --- |
| Tamaño | Ágil | Equipo de 3; un solo interesado con poder de decisión *(el dueño)* |
| Criticidad | Ágil | Si el sistema falla se vuelve al cuaderno; no hay riesgo físico ni pérdida grave |
| Dinamismo | Ágil | El dueño no sabe si quiere reservas por WhatsApp o por web hasta ver una pantalla |
| Personal | Intermedio | Nadie ha trabajado con Scrum; dos integrantes han hecho proyectos web |
| Cultura | Ágil | El dueño acepta ver avances parciales y opinar |
| Acceso al cliente | Ágil | El tío de un integrante; disponible los lunes |
| Regulación | Plan *(leve)* | Maneja nombres y teléfonos: Ley 1581 de 2012, sin norma sectorial |

**2. Selección:** Scrum. Los requisitos van a cambiar cuando el dueño vea las primeras pantallas *(dinamismo)*, un fallo es recuperable *(criticidad)* y hay acceso semanal al dueño para las Review *(acceso al cliente)*. Descartamos **cascada** porque obliga a cerrar requisitos que el dueño aún no conoce, y **Kanban** porque el trabajo sí se puede planificar en bloques y necesitamos un compromiso semanal ligado a las fechas de entrega.

**3. Adaptación:** Sprint de dos semanas. Planning el lunes por videollamada, Review con el dueño el lunes siguiente, Retro al final de la segunda clase de la semana. Daily por chat del equipo, tres preguntas por escrito. DoD: revisado por otro integrante, subido al repositorio, enlazado en la tarjeta.

**4. Tablero:** GitHub Projects, WIP de 3 en *En progreso*. 12 tarjetas estimadas en horas, entre ellas *Preparar guion de entrevista (2 h)*, *Entrevistar al dueño (1 h)*, *Redactar problema y alcance (3 h)*, *Catalogar RF (4 h)*, *Ensayar sustentación (2 h)*.

**5. Acta:** se decide Scrum con Sprint semanal; compromiso de agendar la entrevista con el dueño antes de la primera entrega.