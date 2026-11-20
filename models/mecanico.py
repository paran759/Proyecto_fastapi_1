from sqlalchemy import Column, Integer, String, Float
from core.database import Base
from sqlalchemy.arm import relationship

class Mecanico(Base):
    __tablename__ = "mecanicos" #Crea la tabla en la BD y se llamara "mecanicos"

    # Columnas y datos que tendra la tabla
    id = Column(Integer, primary_key=True) #identificador unico de cada empleado // incrementa solo // es una llave primaria
    documento = Column(String(15), unique=True, nullable=False) #Valor unico de cada mecanico // "nullable" lo hace obligatorio
    nombre = Column(String(100), nullable=False) 
    especialidad = Column(String(50))
    activo = Column(Boolean, default=True)# Valor booleano

    ordenes = relationship("Orden", back_populates="mecanico")#"relationship" Conecta varias tablas // back_populates = muchos a muchos

