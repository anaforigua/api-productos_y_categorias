from fastapi import FastAPI, HTTPException, status
from fastapi.testclient import TestClient
import pytest
from app.main import app
from app.database import products_db, categories_db

client = TestClient(app)

INITIAL_CATEGORIES = categories_db.copy()

@pytest.fixture(autouse=True)
def reset_categories_db():
    categories_db.clear()
    categories_db.extend(INITIAL_CATEGORIES)

def test_list_categories():
    response = client.get("/categories")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_existing_category():
    response = client.get("/categories/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_get_non_existing_category():
    response = client.get("/categories/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Category not found"

def test_invalid_category_id():
    response = client.get("/categories/abc")
    assert response.status_code == 422

def test_create_category_valid():
    new_cat = {"name": "Hogar", "description": "Artículos para el hogar", "active": True}
    response = client.post("/categories", json=new_cat)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Hogar"
    assert "id" in data

def test_create_category_short_name():
    new_cat = {"name": "Hi", "description": "Muy corto"}
    response = client.post("/categories", json=new_cat)
    assert response.status_code == 422

def test_create_category_missing_name():
    new_cat = {"description": "Sin nombre"}
    response = client.post("/categories", json=new_cat)
    assert response.status_code == 422

def test_update_existing_category():
    update_data = {"name": "Computadores Actualizados"}
    response = client.patch("/categories/1", json=update_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Computadores Actualizados"

def test_update_non_existing_category():
    response = client.patch("/categories/999", json={"name": "Nada"})
    assert response.status_code == 404

def test_delete_existing_category():
    response = client.delete("/categories/1")
    assert response.status_code == 204

def test_delete_non_existing_category():
    response = client.delete("/categories/999")
    assert response.status_code == 404

def test_filter_active_categories():
    response = client.get("/categories?active=true")
    assert response.status_code == 200
    data = response.json()
    assert all(c["active"] is True for c in data)