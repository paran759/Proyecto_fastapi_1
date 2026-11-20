from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSeccion
from core.database import obtener_bd
from schemas.schemasFactura import