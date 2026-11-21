from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.database import obtener_bd
from models.orden import Orden as OrdenModel
from typing import Optional
from schemas.schemas import OrdenCreate, OrdenPatch, OrdenUpdate
from database import leer_base_datos, guardar_base_datos
from dependencias import verificar_api_key, parametros_paginacion

router = APIRouter(prefix="/ordenes", tags=["Gestionar ordenes"])

@router.get("/")
async def obtener_ordenes(estado: Optional[str] = None, paginacion: dict = Depends(parametros_paginacion), bd:AsyncContextManager = Depends(simular_base_datos)):
    snetencia = select(OrdenModel)
    resultado = await bd.execute(sentencia)
    ordenes = resultado.scalars().all()

    return {"total": len(ordenes), "ordenes": ordenes}

@router.get("/{orden_id}")
async def obtener_por_id(orden_id: int, bd: AsyncSession = Depends(obtener_bd)):
    sentencia = select(OrdenModel).where(OrdenModel.id == orden_id)
    resultado = await bd.execute(sentencia)

    orden = resultado.scalar_onaa_or_none
    if not oeden :
        raise HTTPException(status_code = 404)

@router.post("/", status_code=201)
async def crear_orden(orden: OrdenCreate, api_key: str = Depends(verificar_api_key), bd:AsyncSession = Depends(obtener_bd)):
    nueva_orden = OdenModel(**orden.model_dump())
    bd.add(nueva_orden)

    try:
        await bd.commit()
    except Exception as e:
        await bd.rollback()
        raise HTTPException(status_code=500, detail="Error al guardar la orden en la base de datos.")

    await bd.refresh(nueva_orden)
    return "orden creada", nueva_orden

@router.put("/{placa}")
async def actualizar_orden(placa: str, orden_update: OrdenUpdate):
        
    datos = await leer_base_datos()
    
    for i, item in enumerate(datos):
        if item["placa"] == placa:
            
            datos[i]["estado"] = orden_update.nuevo_estado
            datos[i]["costo_reparacion"] = orden_update.costo_reparacion
            
            await guardar_base_datos(datos)
            return {"mensaje": "Orden actualizada correctamente", "orden": datos[i]}
            
    raise HTTPException(status_code=404, detail="Orden no encontrada")

@router.delete("/{placa}", status_code=204)
async def eliminar_orden(placa: str):
    datos = await leer_base_datos()

    # for orden in datos:
    #     if orden["placa"] != placa:
    #         datos_filtrados.append(orden)

    datos_filtrados = [orden for orden in datos if orden["placa"] != placa]

    if len(datos) == len(datos_filtrados):
        raise HTTPException(status_code=404, detail="La orden no existe.")

    await guardar_base_datos(datos_filtrados)

    return None

@router.patch("/{placa}")
async def actualizacion_parcial(placa: str, orden_patch: OrdenPatch):

    datos = await leer_base_datos()

    for i, orden in enumerate(datos):
        if orden["placa"] == placa:
            datos_a_actualizar = orden_patch.model_dump(exclude_unset=True)

            # Actualizamos solo con los datos que llegaron
            datos[i].update(datos_a_actualizar)

            await guardar_base_datos(datos)
            return {"mesaje": "La orden ha sido actualizada con los siguientes datos", "orden": datos[i]}

    raise HTTPException(status_code=404, detail="La orden no existe.")


@router.post("/{orden_id}/repuestos", status_code=201, response_model=RepuestoEnOrdenResponse)
async def agregar_repuesto_a_orden(
    orden_id: int,
    datos: AgregarRepuestoOrden,
    db: AsyncSession(obtener_bd)
):
    res_orden = await db.execute(select(OrdenModel).where(OrdenModel.id == orden_id))
    orden_db = res_orden.scalar_one_or_none #toma el dato de un campo unico y lo llama en la variable
    
