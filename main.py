from fastapi import FastAPI, HTTPException
from funciones import listar_datos, verificar_moto, registrar_moto

appAPI = FastAPI(
    title = "inventario prueba",
    description = "API",
    version = "1.0.0"

)

@appAPI.post("/ordenes")
async def crear_orden():
    
         
@appAPI.get("/ordenes")
async def listado():
    try:
        ordenes = await listar_datos()
        return ordenes
    except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))


