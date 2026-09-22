# Presupuesto

## Identificación del concepto

**Tipo de planificación:** Presupuesto y restricciones económicas

El presupuesto representa el monto disponible que el usuario está dispuesto a destinar al viaje.

Dentro de TravelAI, el presupuesto permite adaptar las recomendaciones y el itinerario según la capacidad de gasto del usuario, priorizando actividades, gastronomía, transporte y alojamiento compatibles con sus posibilidades económicas.

---

## Perfil de presupuesto del viajero

El usuario puede indicar su presupuesto de diferentes formas:

* presupuesto bajo;
* presupuesto medio;
* presupuesto alto;
* monto máximo disponible;
* monto aproximado por día;
* monto aproximado por persona;
* monto total para el grupo.

Cuando el usuario no proporciona un monto exacto, se puede utilizar una categoría de presupuesto para orientar la selección de actividades.

---

## Categorías generales de presupuesto

### Presupuesto bajo

El objetivo es minimizar los gastos manteniendo una experiencia turística satisfactoria.

Se pueden priorizar:

* actividades gratuitas;
* parques;
* plazas;
* recorridos a pie;
* espacios públicos;
* museos gratuitos o de bajo costo;
* transporte público;
* gastronomía económica;
* mercados;
* actividades autoguiadas.

Se deben evitar actividades de alto costo salvo que sean especialmente relevantes para los intereses del usuario.

### Presupuesto medio

Permite combinar actividades gratuitas con actividades pagas.

Se pueden incluir:

* museos;
* visitas guiadas;
* restaurantes de precio moderado;
* actividades culturales;
* excursiones;
* transporte público;
* taxis o aplicaciones de transporte cuando sean necesarios;
* experiencias gastronómicas.

El sistema debe buscar un equilibrio entre costo y valor para el usuario.

### Presupuesto alto

Permite mayor flexibilidad en la selección de actividades y servicios.

Se pueden considerar:

* restaurantes de mayor precio;
* experiencias gastronómicas;
* visitas privadas;
* excursiones;
* actividades especializadas;
* transporte privado;
* experiencias exclusivas.

Aun con un presupuesto alto, las recomendaciones deben mantenerse relacionadas con los intereses y restricciones del usuario.

---

## Presupuesto total y presupuesto diario

El presupuesto puede expresarse como:

**Presupuesto total del viaje**

Es el monto máximo disponible para todo el viaje.

**Presupuesto diario**

Es el monto aproximado que el usuario está dispuesto a gastar por día.

Cuando se dispone del presupuesto total, puede estimarse un límite diario:

**Presupuesto diario = Presupuesto total / cantidad de días**

Este valor sirve como referencia para distribuir los gastos a lo largo del itinerario.

---

## Presupuesto por persona y por grupo

Es importante distinguir entre:

* presupuesto individual;
* presupuesto por persona;
* presupuesto total del grupo.

Por ejemplo, un presupuesto de una determinada cantidad por persona no representa lo mismo que ese mismo monto disponible para un grupo completo.

Cuando la información no sea clara, el sistema debe interpretar el presupuesto según el contexto proporcionado por el usuario y evitar asumir cantidades innecesarias.

---

## Componentes del presupuesto

El gasto total de un viaje puede dividirse en diferentes categorías:

* transporte;
* alimentación;
* actividades;
* entradas;
* excursiones;
* compras;
* experiencias adicionales.

Si el usuario no solicita incluir alojamiento o transporte de larga distancia, el sistema puede concentrarse en los gastos relacionados con el itinerario diario.

---

## Presupuesto para actividades

Las actividades pueden clasificarse según su costo.

### Gratuitas

Ejemplos:

* parques;
* plazas;
* monumentos;
* recorridos urbanos;
* paseos;
* espacios públicos;
* actividades al aire libre de acceso libre.

### Bajo costo

Ejemplos:

* museos económicos;
* visitas guiadas básicas;
* actividades recreativas;
* transporte público;
* propuestas gastronómicas económicas.

### Costo medio

Ejemplos:

* restaurantes de precio moderado;
* excursiones;
* experiencias culturales;
* actividades recreativas especializadas.

### Alto costo

Ejemplos:

* restaurantes de alta gama;
* excursiones privadas;
* experiencias exclusivas;
* actividades especializadas;
* transporte privado.

---

## Presupuesto y gastronomía

La gastronomía puede representar una parte importante del gasto diario.

Según el presupuesto, se pueden priorizar:

**Presupuesto bajo:**

* mercados;
* cafeterías económicas;
* comida rápida;
* restaurantes económicos;
* comidas para llevar.

**Presupuesto medio:**

* restaurantes de precio moderado;
* gastronomía regional;
* cafeterías;
* bares;
* experiencias gastronómicas puntuales.

**Presupuesto alto:**

* restaurantes de alta gama;
* experiencias gastronómicas;
* restaurantes especializados;
* propuestas gastronómicas exclusivas.

No es necesario que todas las comidas tengan el mismo nivel de gasto.

Puede resultar conveniente combinar comidas económicas con una experiencia gastronómica de mayor costo.

---

## Presupuesto y transporte

El transporte debe evaluarse según:

* distancia;
* frecuencia;
* cantidad de personas;
* tiempo disponible;
* comodidad;
* costo.

Para presupuestos bajos se puede priorizar:

* caminata;
* transporte público;
* combinación de recorridos cercanos.

Para presupuestos medios se puede combinar transporte público con taxis o aplicaciones cuando resulte conveniente.

Para presupuestos altos puede considerarse transporte privado cuando reduzca significativamente los tiempos de traslado.

---

## Presupuesto y actividades gratuitas

Las actividades gratuitas son especialmente importantes cuando el usuario tiene restricciones económicas.

Se pueden utilizar para complementar actividades pagas y equilibrar el costo diario.

Por ejemplo:

* actividad cultural paga + parque gratuito;
* museo + recorrido a pie;
* excursión + paseo gratuito;
* restaurante + recorrido urbano.

Esto permite mantener variedad sin superar el presupuesto disponible.

---

## Presupuesto y cantidad de actividades

Una mayor cantidad de actividades no necesariamente implica una mejor experiencia.

El sistema debe priorizar:

* relevancia;
* calidad;
* proximidad;
* costo;
* duración;
* interés del usuario.

Cuando el presupuesto sea limitado, se deben seleccionar las actividades de mayor valor para el usuario en lugar de intentar maximizar la cantidad de actividades.

---

## Presupuesto y prioridades

Cuando no sea posible incluir todas las actividades deseadas, se deben priorizar aquellas que:

1. coincidan con los intereses principales;
2. tengan alta relevancia para el destino;
3. sean compatibles con las restricciones;
4. tengan una buena relación entre costo y valor;
5. encajen adecuadamente en el itinerario.

Las actividades secundarias pueden reemplazarse por alternativas gratuitas o de menor costo.

---

## Presupuesto y combinación de intereses

El presupuesto puede utilizarse para equilibrar diferentes intereses.

Por ejemplo:

**Cultura + gastronomía**

Se puede combinar un museo de costo moderado con una comida económica.

**Historia + naturaleza**

Se puede combinar un sitio histórico pago con un parque o recorrido gratuito.

**Gastronomía + cultura**

Se puede reservar una parte del presupuesto para una experiencia gastronómica y complementar con actividades culturales gratuitas.

**Naturaleza + familia**

Se pueden priorizar parques y espacios naturales de acceso libre junto con alguna actividad recreativa paga.

---

## Reglas generales de planificación económica

### Regla 1: respetar el presupuesto máximo

El costo estimado del itinerario no debe superar el presupuesto máximo indicado por el usuario.

Si no es posible cumplir todos los intereses dentro del presupuesto, se deben priorizar las actividades más relevantes.

### Regla 2: priorizar valor sobre cantidad

El sistema no debe intentar agregar actividades únicamente para llenar el día.

Una actividad de mayor relevancia puede ser preferible a varias actividades de menor interés.

### Regla 3: combinar actividades pagas y gratuitas

La combinación permite mantener variedad y controlar el gasto.

### Regla 4: considerar el costo de los desplazamientos

Una actividad económica puede dejar de ser conveniente si requiere un traslado costoso.

Por lo tanto, el costo debe analizarse considerando:

**actividad + transporte necesario**

### Regla 5: evitar gastos innecesarios

Cuando existan alternativas similares, se puede priorizar la opción de menor costo si mantiene un nivel de interés equivalente.

### Regla 6: distribuir el gasto

Cuando el usuario tiene un presupuesto limitado, conviene evitar concentrar todos los gastos en un único día.

Se puede distribuir el presupuesto entre diferentes jornadas.

### Regla 7: considerar el tamaño del grupo

El costo total puede aumentar según la cantidad de personas.

Las actividades con entradas individuales deben multiplicarse por la cantidad correspondiente de viajeros.

### Regla 8: contemplar costos adicionales

Además del precio principal pueden existir:

* entradas;
* transporte;
* reservas;
* servicios adicionales;
* cargos;
* propinas;
* equipamiento;
* consumos mínimos.

Cuando estos valores sean relevantes, deben considerarse en la estimación.

---

## Criterios para seleccionar alternativas

Cuando una actividad exceda el presupuesto, el sistema puede buscar alternativas:

* gratuita;
* de menor costo;
* ubicada más cerca;
* disponible en otro horario;
* similar en tipo de experiencia;
* compatible con otro interés del usuario.

El reemplazo debe mantener, en lo posible, la intención original del usuario.

Por ejemplo, si el usuario quiere una actividad cultural pero su presupuesto no permite una determinada experiencia, se puede buscar otra actividad cultural gratuita o de menor costo.

---

## Relación entre presupuesto y restricciones

El presupuesto debe analizarse junto con otras restricciones.

Algunas restricciones pueden aumentar el costo del viaje, como:

* evitar transporte público;
* requerir transporte privado;
* elegir restaurantes específicos;
* limitar los desplazamientos;
* realizar excursiones;
* viajar con un grupo numeroso.

Por este motivo, el presupuesto no debe evaluarse de manera aislada.

---

## Priorización según presupuesto

Cuando existen varias actividades posibles, se puede utilizar una prioridad basada en:

**Relevancia para el usuario + compatibilidad con el presupuesto + proximidad + duración**

Una actividad con alta relevancia y costo moderado puede tener mayor prioridad que una actividad poco relevante aunque sea gratuita.

---

## Información dinámica

La siguiente información debe obtenerse mediante APIs o fuentes externas actualizadas:

* precios de entradas;
* precios de restaurantes;
* precios de transporte;
* costos de excursiones;
* promociones;
* descuentos;
* disponibilidad;
* costos adicionales;
* tarifas actualizadas;
* precios según fecha;
* precios según cantidad de personas.

Los precios y costos pueden cambiar con el tiempo y no deben considerarse valores permanentes dentro del archivo RAG.
