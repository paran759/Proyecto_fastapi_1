from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base

class OrdenRepuesto(Base):
    __tablename__ = "ordenes_repuestos" 

    # Columnas y datos que tendra la tabla
    id = Column(Integer, primary_key=True)
    orden_id = Column(Integer, ForeignKey("ordenes.id"), nullable=True)
    repuesto_id = Column(Integer, ForeignKey("repuestos.id"), unique=False, nullable=False)

    cantidad = Column(Integer, nullable=False, default=1)
    precio_unidad = Column(Float, nullable=False)

    orden = relationship("Orden", back_populates="factura")
    repuesto = relationship ("Repuesto", back_populates="factura")

