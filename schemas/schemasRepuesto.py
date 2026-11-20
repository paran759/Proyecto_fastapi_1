from pydantic import BaseModel, Field, from_attributes 
from repuesto import Repuesto

class RepuestoCreate(BaseModel):
    codigo_sku: str = Field(..., min_length=5, max_length=20, description="Código SKU del repuesto")
    nombre: str = Field(..., min_length=3, max_length=100, description="Nombre completo del repuesto")
    precio_compra: float = Field(..., gt=0, description="Precio de compra del repuesto")
    precio_venta: float = Field(..., gt=0, description="Precio de venta del repuesto")
    stock: int = Field(..., ge=0, description="Cantidad disponible en inventario")

class RepuestoResponse(BaseModel):
    id: int = Field(..., description="ID del repuesto a actualizar")

    class Config:
        from_attributes = True
    