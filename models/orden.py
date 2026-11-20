from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base

class Orden(Base):
    __tablename__ = "ordenes" #Crea la tabla ordenes 

    #columnas y valores de a tabla 
    id = Column(Integer, primary_key=True, index=True, autoincrement=True) #Id definido como llave primaria
    placa = Column(String(6), index=True, nullable=False, ) #defina un maximo de 6 caracteres
    modelo = Column(String(20))
    falla_reportada = Column(String(255))
    estado = Column(String(20), default="En diagnóstico")
    costo_reparacion = Column(Float, default=0.0) #tiene un valor definido de 0.0

    mecanico_id = Column(Integer, ForeignKey("mecanicos.id").nullableTrue) #Llave foranea/esterna que se importa de la tabla "mecanicos" // se especifica que es obligatorio

    mecanico = relationship("Mecanico", back_populates="ordenes") #Puente diecto que conecta las tablas // define de muchos a muchos
    repuestos_usados = relationship("OrdenRepuesto", back_populates="orden", cascad="all, delete-orphan")#delete-orphan: sirve para borrar los datos de las tablas relacionadas, all: lo hace con todas las tablas relacionadas
    factura = relationship("Factura", back_populates="orden", uselist=False)



