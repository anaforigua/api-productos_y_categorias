# Plan de Pruebas - TechStore API

## 1. Información general

* **Proyecto:** TechStore API (Módulos de Categorías y Productos)

* **Versión:** 1.0

* **Tecnologías:** Python, FastAPI, Pydantic, pytest, TestClient

* **Responsable de pruebas:** Anamaria Forigua Murcia / Equipo QA

* **Fecha:** Septiembre de 2026

## 2. Objetivo

Realizar una auditoría funcional completa de la API de TechStore, verificando que el comportamiento implementado cumpla rigurosamente con el contrato funcional, los requerimientos (RF01-RF12) y las reglas de negocio (RN01-RN08) a través de casos de prueba positivos, negativos, de frontera y automatización con `pytest`.

## 3. Alcance

### Incluido

* **Módulo de Categorías (Etapa A):** Auditoría de RF01 a RF04 y RN01 a RN02 (Creación, listado y consulta por ID de categorías).

* **Módulo de Productos (Etapa B):** Auditoría de RF05 a RF12 y RN03 a RN08 (CRUD completo de productos y validaciones asociadas).

* Verificación de códigos de respuesta HTTP correctos (`201`, `200`, `204`, `404`, `422`, `409`).

* Verificación de la estructura de respuestas JSON y manejo robusto de recursos inexistentes.

* Automatización de una suite representativa de al menos 15 casos mediante `pytest` y `TestClient`.

### Fuera de alcance

* Autenticación de usuarios y control de roles avanzados.

* Pruebas de rendimiento, carga o estrés.

* Seguridad especializada (pentesting, vulnerabilidades OWASP).

* Interfaz gráfica de usuario (UI) y despliegue en producción.

## 4. Reglas de Negocio y Validación a Auditar

El sistema debe hacer cumplir estrictamente las siguientes reglas del dominio TechStore:

| **ID**   | **Regla de Negocio / Validación**                                                               | **Respuesta HTTP Esperada**          |
| -------- | ----------------------------------------------------------------------------------------------- | ------------------------------------ |
| **RN01** | El nombre de categoría es obligatorio y debe tener entre 3 y 60 caracteres. <br>                | `422 Unprocessable Entity`<br>       |
| **RN02** | El nombre de categoría no puede repetirse ignorando mayúsculas/minúsculas. <br>                 | `409 Conflict`<br>                   |
| **RN03** | El nombre de producto es obligatorio y debe tener entre 3 y 80 caracteres. <br>                 | `422 Unprocessable Entity`<br>       |
| **RN04** | El precio del producto debe ser estrictamente mayor que 0 (`price > 0`). <br>                   | `422 Unprocessable Entity`<br>       |
| **RN05** | El stock del producto debe ser mayor o igual que 0 (`stock >= 0`). <br>                         | `422 Unprocessable Entity`<br>       |
| **RN06** | El `category_id` enviado al crear un producto debe corresponder a una categoría existente. <br> | `404 Not Found`<br>                  |
| **RN07** | Un producto puede tener stock igual a 0 (stock crítico de inventario). <br>                     | Debe aceptarse (`201 Created`) <br>  |
| **RN08** | Al actualizar un producto se mantienen las mismas validaciones de creación. <br>                | `422` o `404` según corresponda <br> |

## 5. Riesgos y Priorización

Evaluación de riesgos técnicos para priorizar los esfuerzos de aseguramiento de calidad:

| **ID** | **Riesgo**                                                                                         | **Probabilidad** | **Impacto** | **Prioridad** |
| ------ | -------------------------------------------------------------------------------------------------- | ---------------- | ----------- | ------------- |
| R01    | Permitir crear o actualizar un producto con precio negativo o igual a 0 (RN04) <br>                | Alta             | Alto        | Crítica <br>  |
| R02    | Permitir asociar un producto a un `category_id` inexistente (RN06) <br>                            | Media            | Alto        | Alta <br>     |
| R03    | Permitir registrar categorías duplicadas cambiando solo capitalización (RN02) <br>                 | Media            | Alto        | Alta <br>     |
| R04    | Consultar recursos inexistentes (productos/categorías) y no retornar un código 404 controlado <br> | Alta             | Medio       | Alta <br>     |
| R05    | Incumplir las restricciones de longitud en nombres de productos o categorías (RN01, RN03) <br>     | Media            | Medio       | Media <br>    |

## 6. Estrategia de Pruebas

Se empleará un enfoque híbrido que combina:

* **Diseño funcional estructurado:** Creación de 25 casos de prueba totales (7 para Categorías y 18 para Productos) distribuidos en escenarios positivos, negativos y de frontera.

* **Automatización con pytest:** Implementación de fixtures reutilizables con reseteo de estado y ejecución de al menos 15 casos automatizados obligatorios (5 positivos, 5 negativos, 3 de frontera, 1 de recurso inexistente y 1 de actualización/eliminación).

## 7. Ambiente y Herramientas

* **Sistema operativo:** Windows / Linux / macOS

* **Lenguaje:** Python 3.x

* **Framework Backend:** FastAPI & Pydantic v2

* **Servidor local:** Uvicorn

* **Framework de pruebas:** pytest

* **Cliente de integración:** FastAPI TestClient (Starlette)

* **Persistencia:** Almacenamiento en memoria / diccionarios base estructurados

> **Regla de oro de QA:** Jamás ejecutar pruebas destructivas o de limpieza masiva sobre entornos o bases de datos productivas.

## 8. Datos de Prueba Base

* **Categoría válida:** `name="Periféricos"`

* **Categoría duplicada (para probar RN02):** `name="perifericos"` o `"PERIFÉRICOS"`

* **Producto válido:** `name="Mouse inalámbrico"`, `price=120000`, `stock=5`, `category_id=1`

* **Producto frontera (Stock 0):** `name="Monitor"`, `price=850000`, `stock=0`, `category_id=1`

* **Valores inválidos:** Precio `-1000`, Stock `-1`, ID de recurso `99999`

## 9. Criterios de Entrada

El ciclo de pruebas formales iniciará cuando:

1. La API inicie correctamente sin errores de compilación.

2. Los endpoints del contrato (`/categories` y `/products`) se encuentren implementados.

3. Las dependencias de testing (`pytest`, `TestClient`) estén configuradas en el entorno virtual.

## 10. Criterios de Suspensión y Reanudación

* **Suspensión:** Se paralizará la ejecución si la API presenta fallos críticos de inicio, la base de datos en memoria no responde o existe un bloqueo sistémico que impida ejecutar los endpoints esenciales.

* **Reanudación:** Se continuará una vez el código fuente defectuoso sea corregido y verificado el levantamiento del servicio.

## 11. Criterios de Salida

La auditoría se considerará aprobada y finalizada si se cumple lo siguiente:

* Cobertura documental del 100% en la matriz de trazabilidad para RF01-RF12 y RN01-RN08.

* Ejecución del 100% de los casos críticos planificados.

* Cero (0) defectos críticos abiertos sin resolver.

* Al menos el 90% de aprobación en la suite global de pruebas automatizadas en `pytest`.
