# Restricciones

## Identificación del concepto

**Tipo de planificación:** Restricciones del usuario

Las restricciones representan condiciones que el itinerario debe respetar al momento de seleccionar actividades, lugares, recorridos y medios de transporte.

Dentro de TravelAI, las restricciones funcionan como condiciones que pueden limitar, modificar o descartar determinadas propuestas.

Una recomendación puede ser interesante para el usuario, pero si no cumple una restricción explícita, no debe formar parte del itinerario final.

---

## Tipos de restricciones

Las restricciones pueden clasificarse en:

* tiempo;
* cantidad de actividades;
* presupuesto;
* transporte;
* distancia;
* horarios;
* movilidad;
* alimentación;
* accesibilidad;
* preferencias de planificación;
* disponibilidad;
* características del grupo.

---

## Restricciones de tiempo

El usuario puede establecer:

* cantidad de días;
* cantidad de horas disponibles por día;
* horario de inicio;
* horario límite para finalizar actividades;
* tiempo máximo destinado a una actividad;
* tiempo máximo de desplazamiento.

El itinerario debe respetar el tiempo disponible y evitar actividades que no puedan realizarse dentro del período indicado.

---

## Cantidad máxima de actividades

El usuario puede establecer una cantidad máxima de actividades por día.

Por ejemplo:

> “No queremos hacer más de 3 actividades por día.”

En este caso, el sistema debe considerar como máximo tres actividades principales para esa jornada.

No se deben agregar actividades adicionales únicamente para completar espacios libres.

---

## Cantidad mínima de actividades

En algunos casos el usuario puede indicar una cantidad mínima de actividades por día.

Esta condición debe utilizarse únicamente cuando haya suficientes propuestas compatibles con:

* intereses;
* presupuesto;
* tiempo;
* distancia;
* disponibilidad.

La cantidad mínima no debe provocar que se incluyan actividades poco relevantes o incompatibles con otras restricciones.

---

## Restricciones de desplazamiento

El usuario puede indicar preferencias o límites relacionados con los desplazamientos.

Por ejemplo:

* preferir caminar;
* evitar caminar largas distancias;
* utilizar transporte público;
* evitar transporte público;
* utilizar taxi o aplicaciones;
* minimizar los traslados;
* limitar el tiempo de viaje.

Cuando el usuario prefiera caminar, se deben priorizar actividades cercanas entre sí.

---

## Restricciones de distancia

Se puede establecer una distancia máxima aceptable entre actividades.

Si existen varias propuestas similares, se debe priorizar aquella que requiera menor desplazamiento.

La distancia debe evaluarse considerando el medio de transporte utilizado.

Una distancia que resulta adecuada caminando puede no ser conveniente si el usuario tiene un límite estricto de tiempo.

---

## Restricciones de horarios

El usuario puede establecer:

* horario de inicio del día;
* horario de finalización;
* actividades preferidas por la mañana;
* actividades preferidas por la tarde;
* actividades preferidas por la noche;
* horarios en los que no desea realizar actividades.

Las actividades deben seleccionarse de manera que sus horarios sean compatibles entre sí.

---

## Restricciones de presupuesto

El presupuesto funciona también como una restricción.

Si el usuario establece un monto máximo, el itinerario debe mantenerse dentro de ese límite.

Cuando una actividad supera el presupuesto disponible, se puede:

1. buscar una alternativa más económica;
2. reemplazarla por una actividad gratuita;
3. eliminarla si no existe una alternativa adecuada.

No se debe recomendar una actividad que contradiga explícitamente el presupuesto máximo del usuario.

---

## Restricciones de alimentación

El usuario puede establecer condiciones relacionadas con la alimentación.

Por ejemplo:

* vegetarianismo;
* veganismo;
* intolerancias;
* alergias;
* preferencias alimentarias;
* evitar determinados ingredientes;
* preferencias por determinados tipos de gastronomía.

Estas condiciones deben utilizarse como filtros al seleccionar propuestas gastronómicas.

La información específica sobre ingredientes, disponibilidad de opciones y menús debe verificarse mediante fuentes actualizadas cuando sea necesario.

---

## Restricciones relacionadas con el grupo

Las características del grupo pueden modificar la selección de actividades.

El sistema puede considerar:

* cantidad de personas;
* adultos;
* niños;
* adultos mayores;
* viajes en pareja;
* grupos de amigos;
* grupos familiares.

Una actividad adecuada para una persona puede no ser apropiada para un grupo determinado.

---

## Restricciones de accesibilidad

Cuando el usuario indique necesidades de accesibilidad, se deben considerar características como:

* acceso para personas con movilidad reducida;
* presencia de escaleras;
* disponibilidad de ascensores;
* accesibilidad del transporte;
* distancia caminando;
* duración del recorrido;
* facilidad de acceso.

La información específica sobre accesibilidad debe verificarse mediante fuentes actualizadas cuando sea relevante.

---

## Restricciones de intensidad

Algunos usuarios pueden querer limitar la intensidad de las actividades.

Se pueden considerar preferencias como:

* ritmo tranquilo;
* ritmo moderado;
* ritmo intenso;
* evitar caminatas largas;
* evitar actividades físicamente exigentes;
* priorizar actividades de descanso.

Las actividades deben seleccionarse de acuerdo con el ritmo general solicitado.

---

## Restricciones de transporte

El usuario puede indicar medios de transporte preferidos o no deseados.

Por ejemplo:

* caminar siempre que sea posible;
* utilizar transporte público;
* utilizar vehículo;
* utilizar taxi;
* evitar taxis;
* evitar transporte público;
* evitar determinados medios de transporte.

Estas condiciones deben cruzarse con distancia, tiempo y presupuesto.

---

## Restricciones de temporada y clima

Algunas actividades dependen de:

* clima;
* temperatura;
* precipitaciones;
* estación del año;
* condiciones del lugar;
* disponibilidad temporal.

Las actividades al aire libre deben evaluarse considerando las condiciones previstas para la fecha del viaje.

Si las condiciones no son adecuadas, se puede buscar una alternativa de interior.

---

## Restricciones de disponibilidad

Una actividad puede ser compatible con las preferencias del usuario pero no estar disponible.

Por ejemplo:

* museo cerrado;
* restaurante sin disponibilidad;
* excursión sin cupos;
* evento no realizado ese día;
* actividad fuera de temporada.

Cuando una actividad no esté disponible, debe ser descartada o reemplazada.

La disponibilidad debe obtenerse mediante información actualizada.

---

## Restricciones explícitas e implícitas

### Restricciones explícitas

Son aquellas indicadas directamente por el usuario.

Ejemplos:

* “No quiero gastar más de determinado monto.”
* “No quiero usar transporte público.”
* “No quiero hacer más de tres actividades por día.”
* “Prefiero caminar.”
* “No quiero hacer actividades de noche.”

Estas restricciones deben tener prioridad.

### Restricciones implícitas

Son condiciones que pueden inferirse del contexto de planificación.

Por ejemplo, si una actividad termina muy tarde y la siguiente comienza temprano, puede existir una incompatibilidad temporal.

Las restricciones implícitas deben utilizarse con cautela y nunca deberían contradecir una preferencia explícita del usuario.

---

## Restricciones duras y blandas

### Restricciones duras

Son condiciones que deben cumplirse obligatoriamente.

Ejemplos:

* presupuesto máximo;
* actividad cerrada;
* alergia alimentaria;
* cantidad máxima de actividades;
* horario límite;
* medio de transporte prohibido.

Si una propuesta viola una restricción dura, debe descartarse.

### Restricciones blandas

Son preferencias que conviene cumplir, pero pueden flexibilizarse cuando sea necesario.

Ejemplos:

* preferir caminar;
* preferir determinadas zonas;
* preferir actividades gratuitas;
* preferir comenzar temprano;
* preferir determinados tipos de gastronomía.

Si no es posible cumplir una restricción blanda, el sistema puede buscar una alternativa razonable.

---

## Prioridad de las restricciones

Cuando existen varias restricciones, se debe priorizar de la siguiente manera:

1. restricciones de seguridad;
2. restricciones de salud o alimentación indicadas por el usuario;
3. restricciones explícitas;
4. presupuesto máximo;
5. disponibilidad;
6. tiempo;
7. transporte;
8. distancia;
9. preferencias generales.

Las restricciones pueden interactuar entre sí, por lo que una propuesta debe evaluarse considerando el conjunto completo de condiciones.

---

## Conflictos entre restricciones

En algunos casos pueden existir restricciones incompatibles.

Por ejemplo:

* presupuesto muy bajo + actividades exclusivamente pagas;
* evitar transporte + actividades muy alejadas;
* pocas horas disponibles + gran cantidad de actividades;
* máximo de tres actividades + necesidad de visitar muchos lugares.

Cuando esto ocurra, el sistema debe priorizar las restricciones más importantes y buscar una solución viable.

No debe ignorar silenciosamente una restricción explícita.

---

## Resolución de conflictos

Cuando varias restricciones entran en conflicto, el sistema puede:

1. eliminar actividades incompatibles;
2. buscar alternativas;
3. agrupar actividades cercanas;
4. modificar el orden del recorrido;
5. reducir desplazamientos;
6. reemplazar actividades pagas por alternativas gratuitas;
7. reducir la cantidad de actividades;
8. redistribuir actividades entre diferentes días.

Si ninguna combinación permite cumplir todas las restricciones, el sistema debe indicarlo claramente.

---

## Restricciones y planificación diaria

Cada día del itinerario debe evaluarse individualmente.

Para cada actividad se debe comprobar:

* horario;
* duración;
* costo;
* distancia;
* medio de transporte;
* compatibilidad con otras actividades;
* disponibilidad;
* relación con los intereses;
* restricciones aplicables.

Una actividad que cumple las condiciones individualmente puede generar un conflicto al combinarse con otras actividades del mismo día.

---

## Restricciones y proximidad

Cuando el usuario prefiera caminar o minimizar traslados, se deben agrupar actividades cercanas.

Por ejemplo:

**Actividad A → Actividad B → Actividad C**

puede ser preferible cuando las tres se encuentran en una misma zona.

Esto permite:

* reducir tiempos;
* reducir costos;
* facilitar los recorridos;
* aumentar el tiempo disponible para las actividades.

---

## Restricciones y flexibilidad

No todas las restricciones tienen el mismo nivel de rigidez.

El sistema debe diferenciar entre:

**Obligatorio**

La condición debe cumplirse.

**Preferido**

La condición debería cumplirse siempre que sea posible.

**Opcional**

La condición puede utilizarse como criterio adicional de selección.

Esta diferenciación permite generar itinerarios más realistas.

---

## Criterios para validar un itinerario

Antes de presentar el itinerario final, se debe comprobar:

* cantidad de días correcta;
* cantidad máxima de actividades respetada;
* presupuesto respetado;
* horarios compatibles;
* desplazamientos razonables;
* medios de transporte compatibles;
* restricciones alimentarias respetadas;
* actividades disponibles;
* condiciones climáticas adecuadas cuando corresponda;
* actividades relacionadas con los intereses del usuario.

Si una condición importante no se cumple, el itinerario debe modificarse antes de ser presentado.

---

## Información dinámica

La siguiente información debe obtenerse mediante APIs o fuentes externas actualizadas:

* horarios;
* disponibilidad;
* precios;
* tiempo de traslado;
* distancias;
* condiciones climáticas;
* estado de actividades;
* accesibilidad;
* disponibilidad de transporte;
* eventos temporales.

Esta información puede cambiar con el tiempo y no debe considerarse conocimiento permanente dentro del archivo RAG.
