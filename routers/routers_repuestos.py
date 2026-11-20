from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.database import obtener_bd
from schemas.schemasRepuesto import RepuestoCreate, RepuestoResponde

routerM = APIRouter(prefix="/repuestos", tags=["Gestionar repuestos"])

@routerM.post("/crear", status_code=201)
async def crear_repuesto(repuesto: RepuestoCreate, db: AsyncSession = Depends(obtener_bd)):
    nuevo_repuesto = Repuesto(**repuesto.model_dump())
    db.add(nuevo_repuesto)

    try:
        await db.commit()
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail="Error al guardar el repuesto en la base de datos.")

    await db.refresh(nuevo_repuesto)
    return "Nuevo repuesto ingresado", nuevo_repuesto

@routerM.get("/listar")
async def listar_repuestos(db: AsyncSession = Depends(obtener_bd)):
    seleccionar = select(Repuesto)
    resultado = await db.execute(seleccionar)
    repuestos = resultado.scalars().all()

    return repuestos