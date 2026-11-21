from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSeccion
from core.database import obtener_bd
from schemas.schemas import OrdenPatch

@router.patch("/ordenes/{orden.id}")    
async def actualizacion_parcial(
    placa: str, 
    orden_patch: OrdenPatch,
    db: AsyncSession = Depends(obtener_bd)
):
    sentencia = select(OrdenModel).where(OrdenModel.placa == placa)
    resultado = await db.execute(sentencia)
    orden = resultado.scalar_one_or_none()

    if not orden:
        raise HTTPException(status_code=404, detail="La orden no existe")

    datos_a_actualizar = orden_patch.model_dump(exclude_unset=True)#.model_dump: toma unicamente los datos guardados en orden_patch

    if "nuevo_estado" in datos_a_actualizar:    
        datos_a_actualizar["estado"] = datos_a_actualizar.pop("nuevo_estado")#borra en estado y lo cambia por el nuevo

        if datos_a_actualizar["estado"] == "Reparado":
            print("El estado fue actualizado con exito")

    for campo, valor in datos_a_actualizar.items():#items filtrauno por uno de los datos del campo
        setattr(orden, campo, valor)

    try:
        await db.commit()
        await db.refresh(orden)
    except Exception:
        await db.rollback()
        raise HTTPException(status_code=500, detail="Error aplicando la actualización parcial.")

    return {"mensaje": "La orden ha sido actualizada con éxito", "orden": orden}
