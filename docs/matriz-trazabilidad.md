# Matriz de Trazabilidad

# Matriz de Trazabilidad de Requisitos y Casos de Prueba

| ID Requisito / Regla | Descripción Corta                                 | Caso(s) de Prueba Asociado(s)      | Estado de Cobertura |
| -------------------- | ------------------------------------------------- | ---------------------------------- | ------------------- |
| **RF01**             | Crear categoría válida                            | CP-CAT-01                          | Cubierto            |
| **RF02**             | Listar categorías                                 | CP-CAT-02                          | Cubierto            |
| **RF03**             | Consultar categoría por ID                        | CP-CAT-03                          | Cubierto            |
| **RF04**             | 404 al consultar categoría inexistente            | CP-CAT-04                          | Cubierto            |
| **RF05**             | Crear producto válido                             | CP-PROD-01                         | Cubierto            |
| **RF06**             | Listar productos                                  | CP-PROD-02                         | Cubierto            |
| **RF07**             | Consultar producto por ID                         | CP-PROD-03                         | Cubierto            |
| **RF08**             | 404 al consultar producto inexistente             | CP-PROD-04                         | Cubierto            |
| **RF09**             | Actualizar producto válido                        | CP-PROD-05                         | Cubierto            |
| **RF10**             | 404 al actualizar producto inexistente            | CP-PROD-06                         | Cubierto            |
| **RF11**             | Eliminar producto existente                       | CP-PROD-07                         | Cubierto            |
| **RF12**             | 404 al eliminar producto inexistente              | CP-PROD-08                         | Cubierto            |
| **RN01**             | Nombre de categoría obligatorio y 3-60 caracteres | CP-CAT-05, CP-CAT-06               | Cubierto            |
| **RN02**             | Nombre de categoría único (case-insensitive)      | CP-CAT-07                          | Cubierto            |
| **RN03**             | Nombre de producto obligatorio y 3-80 caracteres  | CP-PROD-09, CP-PROD-10             | Cubierto            |
| **RN04**             | Precio de producto estrictamente > 0              | CP-PROD-11, CP-PROD-12, CP-PROD-13 | Cubierto            |
| **RN05**             | Stock de producto >= 0                            | CP-PROD-14, CP-PROD-15             | Cubierto            |
| **RN06**             | `category_id` debe existir al crear               | CP-PROD-16                         | Cubierto            |
| **RN07**             | Stock igual a 0 es aceptado                       | CP-PROD-14                         | Cubierto            |
| **RN08**             | Validaciones al actualizar producto               | CP-PROD-17, CP-PROD-18             | Cubierto            |
