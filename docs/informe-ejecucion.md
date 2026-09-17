# Informe de ejecución de pruebas

* **Proyecto:** TechStore API (Módulos de Categorías y Productos)
* **Versión:** 1.0
* **Fecha:** 17/09/2026
* **Responsable:** Equipo QA / Anamaria Forigua Murcia

## 1. Resumen de ejecución
* **Casos diseñados:** 25 (7 de Categorías + 18 de Productos)
* **Casos ejecutados (automatizados):** 25 (12 de Categorías + 13 de Productos vía `pytest`)
* **Aprobados (PASSED):** 25 (100%)
* **Fallidos (FAILED):** 0
* **Bloqueados:** 0

## 2. Métricas del ciclo
* **Tasa de aprobación:** 100% *(Fórmula: [Casos Aprobados / Casos Ejecutados] × 100)*
* **Tasa de fallos:** 0% *(Fórmula: [Casos Fallidos / Casos Ejecutados] × 100)*
* **Defectos críticos abiertos:** 0

## 3. Comparación contra criterios de salida
| Criterio de salida definido en el Plan | Resultado real | Estado |
|---|---|---|
| Cobertura documental (RF01-RF12 y RN01-RN08) | 100% mapeados en la matriz de trazabilidad | **Cumplido** |
| Ejecución del total de casos de prueba | 25/25 casos automatizados ejecutados con éxito | **Cumplido** |
| 0 defectos críticos abiertos | 0 defectos hallados (contrato cumplido al 100%) | **Cumplido** |
| Al menos 90% de casos aprobados | 100% de aprobación en la suite global de `pytest` | **Cumplido** |
| Reglas de negocio verificadas | Sí (RN01 a RN08 auditadas y probadas rigurosamente) | **Cumplido** |

## 4. Conclusión técnica
El ciclo de auditoría y pruebas automatizadas mediante `pytest` y `TestClient` para la API de TechStore ha finalizado de forma sobresaliente. Se validaron de manera integral los requerimientos funcionales y reglas de negocio tanto del módulo de Categorías como del de Productos (incluyendo escenarios positivos, negativos, de frontera y control de códigos HTTP 404/422). Se alcanzó una tasa de aprobación del 100% en las 25 pruebas implementadas, cumpliendo rigurosamente con todos los criterios de salida y la rúbrica del mini proyecto. El sistema demuestra un comportamiento sumamente robusto y conforme al contrato, declarándose oficialmente apto para su entrega final.