from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from core.config import settings

# Establece comunicacion con BD
engine = create_async_engine(
    settings.DATABASE_URL, # llama a la base de datos
    echo = True # Imprimir en la consola lo que se haga en SQL
)

#Pide una sesion temporal cada vez que se quiere realizar una accion en la BD
sessionLocal = async_sessionmaker(
    bind = engine,#Indica que use el motor "engine" definido en config.py 
    class_= AsyncSession,#Evita que se bloquee el servidor (funciona como asincrono/async)
    expire_on_commit = False#Indica que no borre datos cuando se guarden los combios, para seguir usandolos sin errores
)

#clase padre
Base=declarative_base()#Indica que SQLAlchemy sepa que clases son tablas para la BD 

#dependencia para fastapi
async def obtener_bd():
    bd= sessionLocal() #Abre una nueva conexion/sesion con la BD
    try:
        yield bd #Envia a la funcion fastapi para que lo use
    finally:
        await bd.close() #Cierra la conexion/sesion sin importar si ahy errores