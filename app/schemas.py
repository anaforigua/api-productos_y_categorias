from typing import Optional
from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, example="Product Name")
    price: float = Field(..., gt=0, example=99.99)
    active: bool = Field(..., example=True)
    stock: int = Field(..., ge=0, example=10)
    category: str = Field(..., example="Product Category")
    
class Product(ProductCreate):
    id: int = Field(..., example=1)
    
class ProductUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, example="Product Name")
    price: float | None = Field(None, gt=0, example=99.99)
    active: bool | None = Field(None, example=True)
    stock: int | None = Field(None, ge=0, example=10)
    category: str | None = Field(None, example="Product Category")
    
    
# ==========================================
# ESQUEMAS PARA CATEGORÍAS
# ==========================================
class CategoryBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Nombre de la categoría")
    description: Optional[str] = Field(None, max_length=200, description="Descripción opcional")
    active: bool = Field(True, description="Estado de la categoría")

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    description: Optional[str] = Field(None, max_length=200)
    active: Optional[bool] = None

class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True