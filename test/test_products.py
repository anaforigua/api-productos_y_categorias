from fastapi import FastAPI, HTTPException, status
from fastapi.testclient import TestClient
import pytest
from app.main import app
from app.database import products_db

client = TestClient(app)

INITIAL_PRODUCTS = products_db.copy()

@pytest.fixture(autouse=True)
def reset_products_db():
    products_db.clear()
    products_db.extend(INITIAL_PRODUCTS)

def test_health():
    endpoint = "/health"
    response = client.get(endpoint)
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
    
def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    
def test_get_existing_products():
    response = client.get("/products/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "name" in data
    
def test_get_non_existing_product():
    response = client.get("/products/9999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Product not found"
    
def test_invalid_product_id():
    response = client.get("/products/abc")
    assert response.status_code == 422
    assert "detail" in response.json()
    
def test_filter_active_products():
    response = client.get("/products?active=true")
    assert response.status_code == 200
    data = response.json()
    assert all(product["active"] is True for product in data)
   
def test_filter_products_by_category():
    response = client.get("/products?category=electronics")
    assert response.status_code == 200
    data = response.json()
    assert all(product["category"] == "electronics" for product in data)

def test_create_product():
    new_product = {
        "name": "New Product",
        "category": "electronics",
        "price": 100.0,
        "stock": 10,
        "active": True
    }
    response = client.post("/products", json=new_product)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == new_product["name"]
    assert data["category"] == new_product["category"]
    assert data["active"] == new_product["active"]
    assert data["price"] == new_product["price"]
    assert data["stock"] == new_product["stock"]
    
def test_create_product_negative_price():
    new_product = {
        "name": "New Product",
        "category": "electronics",
        "price": -10,
        "stock": 5,
        "active": True
    }
    response = client.post("/products", json=new_product)
    assert response.status_code == 422
    data = response.json()
    assert "detail" in data
    # Verificamos que el error corresponda al campo price sin restringir la cadena exacta del mensaje
    assert any(
        error["loc"][-1] == "price" 
        for error in data["detail"]
    )
    
def test_update_product():
    updated_product = {
        "name": "Updated Product",
        "category": "electronics",
        "price": 50.0,
        "stock": 10,
        "active": False
    }
    response = client.put("/products/1", json=updated_product)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == updated_product["name"]
    assert data["category"] == updated_product["category"]
    assert data["active"] == updated_product["active"]
    assert data["price"] == updated_product["price"]
    assert data["stock"] == updated_product["stock"]
    
def test_update_price_patch():
    updated_price = {
        "price": 75.0
    }
    response = client.patch("/products/1", json=updated_price)
    assert response.status_code == 200
    data = response.json()
    assert data["price"] == updated_price["price"]
    
def test_update_non_existing_product():
    updated_product = {
        "name": "Updated Product",
        "category": "electronics",
        "price": 50.0,
        "stock": 10,
        "active": False
    }
    response = client.put("/products/999", json=updated_product)
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Product not found"
    
def test_delete_product():
    response = client.delete("/products/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1