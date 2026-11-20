from pydantic import BaseModel, Field, from_attributes 
from mecanico import Mecanico

class MecanicoCreate(BaseModel):
    documento: str = Field(..., min_length=5, max_length=15, description="Documento de identidad del mecánico")
    nombre: str = Field(..., min_length=3, max_length=100, description="Nombre completo del mecánico")
    especialidad: str = Field(..., min_length=3, max_length=50, description="Especialidad del mecánico")

class MecanicoResponde(BaseModel):
    id: int = Field(..., description="ID del mecánico a actualizar")

    class Config:
        from_attributes = True
