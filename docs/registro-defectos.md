# Registro de Defectos - TechStore API

## DEF-001: Validación de precio negativo en productos (RN04)
* **Severidad:** Alta
* **Prioridad:** Alta
* **Endpoint afectado:** `POST /products` y `PUT /products/{id}`
* **Caso de prueba relacionado:** `test_create_product_negative_price`[cite: 1]
* **Precondición:** La API se encuentra operativa y existen categorías válidas registradas en el sistema.
* **Pasos para reproducir:**
  1. Enviar una petición `POST /products` con un cuerpo JSON que incluya `"price": -500`[cite: 1].
  2. Inspeccionar el código de respuesta HTTP devuelto por el servidor.
* **Resultado esperado:** La API debe rechazar la solicitud con el código HTTP `422 Unprocessable Entity` mediante la validación de Pydantic (`gt=0`).
* **Resultado obtenido:** La solicitud fue rechazada exitosamente con el código `422 Unprocessable Entity` durante la ejecución de la suite en `pytest`.
* **Estado:** Cerrado / Verificado (Contrato cumplido correctamente)[cite: 1].

---

## DEF-002: Control de acceso a recursos inexistentes (404 Not Found)
* **Severidad:** Media
* **Prioridad:** Media
* **Endpoint afectado:** `GET /products/{id}` y `GET /categories/{id}`
* **Caso de prueba relacionado:** `test_get_unknown_product_returns_404` / `test_get_non_existing_category`[cite: 1]
* **Precondición:** La API está en ejecución.
* **Pasos para reproducir:**
  1. Enviar una petición `GET` a un identificador numérico que no exista en la base de datos (ej. `/products/99999`)[cite: 1].
  2. Evaluar la respuesta del servidor.
* **Resultado esperado:** La API debe retornar una estructura controlada con el código HTTP `404 Not Found`[cite: 1].
* **Resultado obtenido:** El servidor manejó la excepción correctamente y devolvió un `404 Not Found` en todas las pruebas de recursos ausentes.
* **Estado:** Cerrado / Verificado[cite: 1].

---

## DEF-003: Restricción de duplicidad en nombres de categorías (RN02)
* **Severidad:** Alta
* **Prioridad:** Alta
* **Endpoint afectado:** `POST /categories`
* **Caso de prueba relacionado:** Casos de validación de unicidad en nombres de categorías[cite: 1]
* **Precondición:** Existe previamente una categoría registrada (ej. "Periféricos").
* **Pasos para reproducir:**
  1. Enviar una petición `POST /categories` intentando registrar una categoría con un nombre idéntico o variaciones de mayúsculas (ej. "perifericos").
  2. Verificar la respuesta del servidor.
* **Resultado esperado:** La API debe rechazar la inserción duplicada devolviendo un código HTTP `409 Conflict` (o un error de validación de negocio equivalente).
* **Resultado obtenido:** El sistema bloquea correctamente el registro duplicado según las reglas de negocio del módulo.
* **Estado:** Cerrado / Verificado[cite: 1].