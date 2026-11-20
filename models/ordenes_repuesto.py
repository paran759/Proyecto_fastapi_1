from sqlalchemy import Colum, Integer, Float, ForeignKey, primary_key
from sqlalchemy.orm import relationship
from core.database import Base

class OrdenRepuesto(Base):
    __tablename__ = "ordenes_repuestos" 

    # Columnas y datos que tendra la tabla
    id = Column(Integer, primary_key=True)
    orden_id = Column(Integer, ForeignKey("mecanicos.id"), nullable=True)
    repuesto_id = Column(Integer, unique=True, ForeignKey("ordenes.id"), nullable=False)

    cantidad = Column(Integer, nullable=False, default=1)
    precio_unidad = Column(Float, nullable=False)

    orden = relationship("Orden", back_populates="repuestos_usados")
    repuesto = relationship ("Mecanico", back_populates="")

