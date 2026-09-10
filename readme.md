# API de Productos y Categorías — FastAPI

API REST desarrollada con **FastAPI** para la gestión de **productos y categorías**.

El proyecto utiliza almacenamiento en memoria y validaciones mediante **Pydantic**. Cuenta además con una suite de pruebas automatizadas desarrollada con **pytest**, utilizando `TestClient` de FastAPI para validar el comportamiento de los endpoints.

Las pruebas contemplan casos positivos, casos negativos, validaciones de datos, consultas, filtros, creación, actualización y eliminación de recursos.

---

# 1. Tecnologías utilizadas

* Python 3
* FastAPI
* Pydantic
* Uvicorn
* Pytest
* HTTPX
* FastAPI TestClient

---

# 2. Estructura del proyecto

```text
api-productos_y_categorias/
│
├── app/
│   ├── main.py
│   ├── database.py
│   └── schemas.py
│
├── tests/
│   ├── test_categories.py
│   └── test_products.py
│
├── requirements.txt
├── README.md
└── venv/
```

> La carpeta `venv` corresponde al entorno virtual local. Se recomienda incluirla en `.gitignore` y no subirla al repositorio.

---

# 3. Configuración del proyecto

## 3.1 Ubicarse en la raíz del proyecto

Antes de ejecutar cualquier comando, la terminal debe estar ubicada en la carpeta principal del proyecto.

La raíz debe contener elementos como:

```text
requirements.txt
app/
tests/
```

En Git Bash, por ejemplo:

```bash
cd /c/Users/TU_USUARIO/OneDrive/Desktop/api-productos_y_categorias
```

También se puede navegar manualmente hasta la carpeta y abrir Git Bash allí.

> No se recomienda colocar una ruta específica de otro computador en el README. Cada usuario debe utilizar su propia ruta local.

---

# 4. Crear el entorno virtual

El entorno virtual permite instalar las dependencias del proyecto de manera aislada.

Desde la raíz del proyecto ejecutar:

```bash
python -m venv venv
```

Esto crea la carpeta:

```text
venv/
```

---

# 5. Activar el entorno virtual

## Windows — Git Bash

Ejecutar:

```bash
source venv/Scripts/activate
```

Si la activación fue correcta, aparecerá:

```text
(venv)
```

al inicio de la línea de comandos.

Ejemplo:

```text
(venv) CLAUDIA@DESKTOP-6B2VMP4 MINGW64 ~/OneDrive/Desktop/api-productos_y_categorias
```

En la ejecución real del proyecto, el entorno virtual se encontraba activo antes de ejecutar las pruebas.

---

## Windows — CMD

Si se utiliza el símbolo del sistema de Windows:

```cmd
venv\Scripts\activate
```

El resultado esperado es que aparezca:

```text
(venv)
```

---

# 6. Instalar las dependencias

Con el entorno virtual activado, instalar las dependencias definidas en `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

Para comprobar las dependencias instaladas:

```bash
python -m pip list
```

---

# 7. Ejecución de la API

Desde la raíz del proyecto y con el entorno virtual activo:

```bash
python -m uvicorn app.main:app --reload
```

La API quedará disponible normalmente en:

```text
http://127.0.0.1:8000
```

La opción:

```text
--reload
```

permite que Uvicorn reinicie automáticamente la aplicación cuando se detectan cambios durante el desarrollo.

---

# 8. Documentación de la API

FastAPI proporciona documentación interactiva automáticamente.

## Swagger UI

Abrir en el navegador:

```text
http://127.0.0.1:8000/docs
```

Desde Swagger se pueden consultar y ejecutar los endpoints de la API.

## ReDoc

También está disponible:

```text
http://127.0.0.1:8000/redoc
```

---

# 9. Pruebas automatizadas

Las pruebas automatizadas se encuentran en:

```text
tests/
```

Archivos:

```text
tests/test_categories.py
tests/test_products.py
```

Las pruebas utilizan:

```python
from fastapi.testclient import TestClient
```

para realizar solicitudes HTTP directamente sobre la aplicación FastAPI.

---

# 10. Ejecutar todas las pruebas

Para ejecutar toda la suite:

```bash
python -m pytest -v
```

El parámetro `-v` muestra de manera detallada cada prueba ejecutada.

---

# 11. Ejecutar pruebas de categorías

Para ejecutar únicamente las pruebas de categorías:

```bash
python -m pytest tests/test_categories.py -v
```

Esta suite contiene **12 casos de prueba**.

---

# 12. Ejecutar pruebas de productos

Para ejecutar únicamente las pruebas de productos:

```bash
python -m pytest tests/test_products.py -v
```

Esta suite contiene **13 casos de prueba**.

---

# 13. Matriz de casos de prueba — Categorías

| ID   | Caso de prueba                      | Endpoint / Validación            | Resultado |
| ---- | ----------------------------------- | -------------------------------- | --------- |
| CA01 | Listar categorías                   | `GET /categories`                | PASS      |
| CA02 | Obtener categoría existente         | `GET /categories/1`              | PASS      |
| CA03 | Obtener categoría inexistente       | `GET /categories/999` → `404`    | PASS      |
| CA04 | Validar ID de categoría inválido    | `GET /categories/abc` → `422`    | PASS      |
| CA05 | Crear categoría válida              | `POST /categories` → `201`       | PASS      |
| CA06 | Crear categoría con nombre inválido | `POST /categories` → `422`       | PASS      |
| CA07 | Crear categoría sin nombre          | `POST /categories` → `422`       | PASS      |
| CA08 | Actualizar categoría existente      | `PATCH /categories/1` → `200`    | PASS      |
| CA09 | Actualizar categoría inexistente    | `PATCH /categories/999` → `404`  | PASS      |
| CA10 | Eliminar categoría existente        | `DELETE /categories/1` → `204`   | PASS      |
| CA11 | Eliminar categoría inexistente      | `DELETE /categories/999` → `404` | PASS      |
| CA12 | Filtrar categorías activas          | `GET /categories?active=true`    | PASS      |

La suite real de categorías ejecutó los 12 casos y todos finalizaron como `PASSED`.

---

# 14. Matriz de casos de prueba — Productos

| ID   | Caso de prueba                     | Endpoint / Validación                | Resultado |
| ---- | ---------------------------------- | ------------------------------------ | --------- |
| PR01 | Verificar estado de la API         | `GET /health` → `200`                | PASS      |
| PR02 | Listar productos                   | `GET /products` → `200`              | PASS      |
| PR03 | Obtener producto existente         | `GET /products/1` → `200`            | PASS      |
| PR04 | Obtener producto inexistente       | `GET /products/9999` → `404`         | PASS      |
| PR05 | Validar ID de producto inválido    | `GET /products/abc` → `422`          | PASS      |
| PR06 | Filtrar productos activos          | `GET /products?active=true`          | PASS      |
| PR07 | Filtrar productos por categoría    | `GET /products?category=electronics` | PASS      |
| PR08 | Crear producto válido              | `POST /products` → `201`             | PASS      |
| PR09 | Crear producto con precio negativo | `POST /products` → `422`             | PASS      |
| PR10 | Actualizar producto                | `PUT /products/1` → `200`            | PASS      |
| PR11 | Actualizar únicamente el precio    | `PATCH /products/1` → `200`          | PASS      |
| PR12 | Actualizar producto inexistente    | `PUT /products/999` → `404`          | PASS      |
| PR13 | Eliminar producto                  | `DELETE /products/1` → `200`         | PASS      |

La suite real de productos ejecutó los 13 casos y todos finalizaron como `PASSED`.

---

# 15. Evidencia de ejecución — Pruebas de categorías

La siguiente evidencia corresponde directamente a la ejecución realizada en la consola.

```text
CLAUDIA@DESKTOP-6B2VMP4 MINGW64 ~/OneDrive/Desktop/api-productos_y_categorias (main)
$ python -m pytest tests/test_categories.py -v
============================= test session starts =============================
platform win32 -- Python 3.14.5, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\CLAUDIA\OneDrive\Desktop\api-productos_y_categorias\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\CLAUDIA\OneDrive\Desktop\api-productos_y_categorias
plugins: anyio-4.14.1
collecting 0 items                                                          collected 12 items

tests/test_categories.py::test_list_categories PASSED                    [  8%]
tests/test_categories.py::test_get_existing_category PASSED              [ 16%]
tests/test_categories.py::test_get_non_existing_category PASSED           [ 25%]
tests/test_categories.py::test_invalid_category_id PASSED                [ 33%]
tests/test_categories.py::test_create_category_valid PASSED              [ 41%]
tests/test_categories.py::test_create_category_short_name PASSED          [ 50%]
tests/test_categories.py::test_create_category_missing_name PASSED        [ 58%]
tests/test_categories.py::test_update_existing_category PASSED            [ 66%]
tests/test_categories.py::test_update_non_existing_category PASSED        [ 75%]
tests/test_categories.py::test_delete_existing_category PASSED            [ 83%]
tests/test_categories.py::test_delete_non_existing_category PASSED         [ 91%]
tests/test_categories.py::test_filter_active_categories PASSED            [100%]

======================= 12 passed, 14 warnings in 1.16s =======================
```

## La consola original reporta exactamente **12 pruebas aprobadas y 14 warnings**.

# 16. Evidencia de ejecución — Pruebas de productos

La siguiente evidencia corresponde directamente a la ejecución realizada en la consola.

```text
CLAUDIA@DESKTOP-6B2VMP4 MINGW64 ~/OneDrive/Desktop/api-productos_y_categorias (main)
$ python -m pytest tests/test_products.py -v
============================= test session starts =============================
platform win32 -- Python 3.14.5, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\CLAUDIA\OneDrive\Desktop\api-productos_y_categorias\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\CLAUDIA\OneDrive\Desktop\api-productos_y_categorias
plugins: anyio-4.14.1
collecting 0 items                                                          collected 13 items

tests/test_products.py::test_health PASSED                               [  7%]
tests/test_products.py::test_get_products PASSED                         [ 15%]
tests/test_products.py::test_get_existing_products PASSED                [ 23%]
tests/test_products.py::test_get_non_existing_product PASSED             [ 30%]
tests/test_products.py::test_invalid_product_id PASSED                   [ 38%]
tests/test_products.py::test_filter_active_products PASSED               [ 46%]
tests/test_products.py::test_filter_products_by_category PASSED          [ 53%]
tests/test_products.py::test_create_product PASSED                       [ 61%]
tests/test_products.py::test_create_product_negative_price PASSED        [ 69%]
tests/test_products.py::test_update_product PASSED                       [ 76%]
tests/test_products.py::test_update_price_patch PASSED                   [ 84%]
tests/test_products.py::test_update_non_existing_product PASSED           [ 92%]
tests/test_products.py::test_delete_product PASSED                       [100%]

======================= 13 passed, 14 warnings in 1.31s =======================
```

## La consola original reporta exactamente **13 pruebas aprobadas y 14 warnings**.

# 17. Resultado general de las pruebas

| Suite      | Casos ejecutados |   PASS |  FAIL | Warnings |
| ---------- | ---------------: | -----: | ----: | -------: |
| Categorías |               12 |     12 |     0 |       14 |
| Productos  |               13 |     13 |     0 |       14 |
| **TOTAL**  |           **25** | **25** | **0** |   **28** |

## Resultado

**25/25 pruebas aprobadas.**

```text
PASS: 25
FAIL: 0
```

Esto significa que todos los casos de prueba ejecutados cumplieron las condiciones definidas en los tests.

---

# 18. ¿Qué se está validando como QA?

La suite no solamente comprueba que los endpoints funcionen con información correcta.

También comprueba diferentes tipos de escenarios.

## 18.1 Pruebas positivas

Verifican que el sistema funcione correctamente cuando recibe datos válidos.

Ejemplos:

```text
Crear categoría válida
Crear producto válido
Consultar producto existente
Actualizar producto existente
```

---

## 18.2 Pruebas negativas

Verifican que el sistema controle correctamente situaciones incorrectas.

Ejemplos:

```text
Consultar un producto inexistente
Consultar una categoría inexistente
Actualizar un recurso inexistente
Eliminar un recurso inexistente
```

---

## 18.3 Pruebas de validación

Comprueban que la API rechace información que no cumple las reglas establecidas.

Ejemplos:

```text
ID = "abc"
Precio = -10
Nombre de categoría demasiado corto
Campo obligatorio ausente
```

---

## 18.4 Pruebas de filtros

Se verifica que los parámetros de consulta funcionen correctamente.

Ejemplos:

```text
GET /products?active=true
GET /products?category=electronics
GET /categories?active=true
```

Los tests comprueban además que todos los elementos devueltos cumplan el filtro solicitado.

---

# 19. Aislamiento de las pruebas

Los tests utilizan fixtures para restaurar la información inicial de las bases de datos en memoria.

En categorías se utiliza:

```python
@pytest.fixture(autouse=True)
def reset_categories_db():
    categories_db.clear()
    categories_db.extend(INITIAL_CATEGORIES)
```

En productos:

```python
@pytest.fixture(autouse=True)
def reset_products_db():
    products_db.clear()
    products_db.extend(INITIAL_PRODUCTS)
```

Esto permite que una prueba no dependa de los cambios realizados por una prueba anterior.

Desde el punto de vista de QA, esto ayuda a mantener las pruebas **aisladas y repetibles**.

---

# 20. Warnings encontrados

Las pruebas finalizaron correctamente, pero pytest reportó warnings.

Estos warnings **no hicieron fallar las pruebas**.

Entre ellos se encuentra una advertencia relacionada con el uso de `httpx` mediante `starlette.testclient`.

También aparecen advertencias de Pydantic relacionadas con:

```text
Field(..., example="...")
```

y configuraciones antiguas como:

```text
orm_mode
```

Pydantic indica que:

```text
orm_mode
```

ha sido renombrado a:

```text
from_attributes
```

Estas advertencias aparecen durante la ejecución tanto de categorías como de productos.

## Importante

El resultado:

```text
12 passed, 14 warnings
```

significa:

```text
12 pruebas → correctas
14 warnings → advertencias
0 failures → ningún fallo
```

No debe interpretarse como:

```text
12 pruebas y 14 errores
```

---

# 21. Conclusión QA

La ejecución realizada sobre la API permitió validar **25 casos de prueba automatizados**:

* 12 correspondientes a categorías.
* 13 correspondientes a productos.
* 25 pruebas aprobadas.
* 0 pruebas fallidas.

Los casos cubren operaciones CRUD, consultas, filtros, validaciones de entrada y manejo de recursos inexistentes.

El resultado obtenido fue:

```text
25 passed
0 failed
```

Por lo tanto, con base en los casos automatizados ejecutados, la funcionalidad evaluada presenta un resultado satisfactorio.

Sin embargo, los **warnings detectados deben registrarse como deuda técnica**, especialmente los relacionados con cambios de configuración de Pydantic y la integración de `httpx` con Starlette.

---

# 22. Comandos principales

### Crear entorno virtual

```bash
python -m venv venv
```

### Activar en Git Bash

```bash
source venv/Scripts/activate
```

### Activar en CMD

```cmd
venv\Scripts\activate
```

### Instalar dependencias

```bash
python -m pip install -r requirements.txt
```

### Ejecutar API

```bash
python -m uvicorn app.main:app --reload
```

### Ejecutar todas las pruebas

```bash
python -m pytest -v
```

### Ejecutar categorías

```bash
python -m pytest tests/test_categories.py -v
```

### Ejecutar productos

```bash
python -m pytest tests/test_products.py -v
```

### Desactivar entorno virtual

```bash
deactivate
```
