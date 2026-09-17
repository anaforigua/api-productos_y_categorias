(venv) PS C:\Users\sena\Desktop\api-productos_y_categorias> python -m pytest -v
====================== test session starts =======================
platform win32 -- Python 3.14.5, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\sena\Desktop\api-productos_y_categorias\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\sena\Desktop\api-productos_y_categorias
plugins: anyio-4.15.1
collected 25 items                                                

tests/test_categories.py::test_list_categories PASSED       [  4%]
tests/test_categories.py::test_get_existing_category PASSED [  8%]
tests/test_categories.py::test_get_non_existing_category PASSED [ 12%]
tests/test_categories.py::test_invalid_category_id PASSED   [ 16%]
tests/test_categories.py::test_create_category_valid PASSED [ 20%]
tests/test_categories.py::test_create_category_short_name PASSED [ 24%]
tests/test_categories.py::test_create_category_missing_name PASSED [ 28%]
tests/test_categories.py::test_update_existing_category PASSED [ 32%]
tests/test_categories.py::test_update_non_existing_category PASSED [ 36%]
tests/test_categories.py::test_delete_existing_category PASSED [ 40%]
tests/test_categories.py::test_delete_non_existing_category PASSED [ 44%]
tests/test_categories.py::test_filter_active_categories PASSED [ 48%]
tests/test_products.py::test_health PASSED                  [ 52%]
tests/test_products.py::test_get_products PASSED            [ 56%]
tests/test_products.py::test_get_existing_products PASSED   [ 60%]
tests/test_products.py::test_get_non_existing_product PASSED [ 64%]
tests/test_products.py::test_invalid_product_id PASSED      [ 68%]
tests/test_products.py::test_filter_active_products PASSED  [ 72%]
tests/test_products.py::test_filter_products_by_category PASSED [ 76%]
tests/test_products.py::test_create_product PASSED          [ 80%]
tests/test_products.py::test_create_product_negative_price PASSED [ 84%]
tests/test_products.py::test_update_product PASSED          [ 88%]
tests/test_products.py::test_update_price_patch PASSED      [ 92%]
tests/test_products.py::test_update_non_existing_product PASSED [ 96%]
tests/test_products.py::test_delete_product PASSED          [100%]

================ 25 passed, 16 warnings in 0.42s =================



(venv) PS C:\Users\sena\Desktop\api-productos_y_categorias> python -m pytest tests/test_products.py -v
====================== test session starts =======================
platform win32 -- Python 3.14.5, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\sena\Desktop\api-productos_y_categorias\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\sena\Desktop\api-productos_y_categorias
plugins: anyio-4.15.1
collected 13 items                                                

tests/test_products.py::test_health PASSED                  [  7%]
tests/test_products.py::test_get_products PASSED            [ 15%]
tests/test_products.py::test_get_existing_products PASSED   [ 23%]
tests/test_products.py::test_get_non_existing_product PASSED [ 30%]
tests/test_products.py::test_invalid_product_id PASSED      [ 38%]
tests/test_products.py::test_filter_active_products PASSED  [ 46%]
tests/test_products.py::test_filter_products_by_category PASSED [ 53%]
tests/test_products.py::test_create_product PASSED          [ 61%]
tests/test_products.py::test_create_product_negative_price PASSED [ 69%]
tests/test_products.py::test_update_product PASSED          [ 76%]
tests/test_products.py::test_update_price_patch PASSED      [ 84%]
tests/test_products.py::test_update_non_existing_product PASSED [ 92%]
tests/test_products.py::test_delete_product PASSED          [100%]
================ 13 passed, 16 warnings in 0.30s =================


(venv) PS C:\Users\sena\Desktop\api-productos_y_categorias> python -m pytest tests/test_categories.py -v
====================== test session starts =======================
platform win32 -- Python 3.14.5, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\sena\Desktop\api-productos_y_categorias\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\sena\Desktop\api-productos_y_categorias
plugins: anyio-4.15.1
collected 12 items                                                

tests/test_categories.py::test_list_categories PASSED       [  8%]
tests/test_categories.py::test_get_existing_category PASSED [ 16%]
tests/test_categories.py::test_get_non_existing_category PASSED [ 25%]
tests/test_categories.py::test_invalid_category_id PASSED   [ 33%]
tests/test_categories.py::test_create_category_valid PASSED [ 41%]
tests/test_categories.py::test_create_category_short_name PASSED [ 50%]
tests/test_categories.py::test_create_category_missing_name PASSED [ 58%]
tests/test_categories.py::test_update_existing_category PASSED [ 66%]
tests/test_categories.py::test_update_non_existing_category PASSED [ 75%]
tests/test_categories.py::test_delete_existing_category PASSED [ 83%]
tests/test_categories.py::test_delete_non_existing_category PASSED [ 91%]
tests/test_categories.py::test_filter_active_categories PASSED [100%]
================ 12 passed, 16 warnings in 0.30s =================
