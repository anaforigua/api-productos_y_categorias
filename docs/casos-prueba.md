# Catálogo de Casos de Prueba de Productos (`docs/casos-prueba.md`)

* **CP-PROD-01: Crear producto válido**

  * **Requisito:** RF05
  * **Tipo:** Positiva
  * **Prioridad:** Alta
  * **Datos:**

    ```json
    {
      "name": "Mouse inalámbrico",
      "price": 120000,
      "stock": 5,
      "category_id": 1
    }
    ```
  * **Resultado esperado:** HTTP `201 Created` y retorno del objeto creado con ID asignado.

* **CP-PROD-02: Listar productos**

  * **Requisito:** RF06
  * **Tipo:** Positiva
  * **Prioridad:** Alta
  * **Resultado esperado:** HTTP `200 OK` y una lista con los productos registrados.

* **CP-PROD-03: Consultar producto existente por ID**

  * **Requisito:** RF07
  * **Tipo:** Positiva
  * **Prioridad:** Alta
  * **Resultado esperado:** HTTP `200 OK` y el detalle del producto solicitado.

* **CP-PROD-04: Consultar producto inexistente**

  * **Requisito:** RF08
  * **Tipo:** Negativa
  * **Prioridad:** Media
  * **Datos:** ID `99999`
  * **Resultado esperado:** HTTP `404 Not Found`.

* **CP-PROD-05: Actualizar producto válido**

  * **Requisito:** RF09
  * **Tipo:** Positiva
  * **Prioridad:** Alta
  * **Resultado esperado:** HTTP `200 OK` con los datos actualizados del producto.

* **CP-PROD-06: Actualizar producto inexistente**

  * **Requisito:** RF10
  * **Tipo:** Negativa
  * **Prioridad:** Media
  * **Datos:** ID `99999`
  * **Resultado esperado:** HTTP `404 Not Found`.

* **CP-PROD-07: Eliminar producto existente**

  * **Requisito:** RF11
  * **Tipo:** Positiva
  * **Prioridad:** Alta
  * **Resultado esperado:** HTTP `204 No Content`.

* **CP-PROD-08: Eliminar producto inexistente**

  * **Requisito:** RF12
  * **Tipo:** Negativa
  * **Prioridad:** Media
  * **Datos:** ID `99999`
  * **Resultado esperado:** HTTP `404 Not Found`.

* **CP-PROD-09: Nombre de producto menor a 3 caracteres**

  * **Requisito:** RN03
  * **Tipo:** Frontera / Negativa
  * **Prioridad:** Alta
  * **Datos:**

    ```json
    {
      "name": "Te"
    }
    ```
  * **Resultado esperado:** HTTP `422 Unprocessable Entity`.

* **CP-PROD-10: Nombre de producto exactamente de 3 caracteres**

  * **Requisito:** RN03
  * **Tipo:** Frontera / Positiva
  * **Prioridad:** Alta
  * **Datos:**

    ```json
    {
      "name": "Hub"
    }
    ```
  * **Resultado esperado:** HTTP `201 Created`.

* **CP-PROD-11: Precio de producto igual a 0**

  * **Requisito:** RN04
  * **Tipo:** Frontera / Negativa
  * **Prioridad:** Alta
  * **Datos:**

    ```json
    {
      "price": 0
    }
    ```
  * **Resultado esperado:** HTTP `422 Unprocessable Entity`.

* **CP-PROD-12: Precio de producto negativo**

  * **Requisito:** RN04
  * **Tipo:** Negativa
  * **Prioridad:** Alta
  * **Datos:**

    ```json
    {
      "price": -1000
    }
    ```
  * **Resultado esperado:** HTTP `422 Unprocessable Entity`.

* **CP-PROD-13: Precio mínimo positivo**

  * **Requisito:** RN04
  * **Tipo:** Frontera / Positiva
  * **Prioridad:** Alta
  * **Datos:**

    ```json
    {
      "price": 0.01
    }
    ```

    O valor mínimo válido.
  * **Resultado esperado:** HTTP `201 Created`.

* **CP-PROD-14: Stock de producto igual a 0**

  * **Requisito:** RN05 / RN07
  * **Tipo:** Frontera / Positiva
  * **Prioridad:** Media
  * **Datos:**

    ```json
    {
      "stock": 0
    }
    ```

    Ejemplo: Monitor.
  * **Resultado esperado:** HTTP `201 Created` (debe aceptarse).

* **CP-PROD-15: Stock de producto negativo**

  * **Requisito:** RN05
  * **Tipo:** Negativa
  * **Prioridad:** Alta
  * **Datos:**

    ```json
    {
      "stock": -1
    }
    ```
  * **Resultado esperado:** HTTP `422 Unprocessable Entity`.

* **CP-PROD-16: Categoría inexistente al crear producto**

  * **Requisito:** RN06
  * **Tipo:** Negativa
  * **Prioridad:** Alta
  * **Datos:**

    ```json
    {
      "category_id": 99999
    }
    ```
  * **Resultado esperado:** HTTP `404 Not Found`.

* **CP-PROD-17: Precio inválido al actualizar producto**

  * **Requisito:** RN08
  * **Tipo:** Negativa
  * **Prioridad:** Alta
  * **Datos:**

    ```json
    {
      "price": -50
    }
    ```
  * **Resultado esperado:** HTTP `422 Unprocessable Entity`.

* **CP-PROD-18: Categoría inexistente al actualizar producto**

  * **Requisito:** RN08 / RN06
  * **Tipo:** Negativa
  * **Prioridad:** Alta
  * **Datos:**

    ```json
    {
      "category_id": 99999
    }
    ```
  * **Resultado esperado:** HTTP `404 Not Found` (o `422` según la implementación).
