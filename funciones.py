import aiofiles
import json

BD_motores = "inventario.json"

async def leer_datos():
    try:
        async with aiofiles.open(BD_motores, mode="r", encoding="utf-8" ) as f:
            contenido = await f.read()
            return json.loads(contenido)
    except FileNotFoundError:
        return [] 

async def guardar_datos(datos):
    async with aiofiles.open(BD_motores, node="w", encoding="ytf-8") as f:
        await f.write(json.dumps(datos, indent=4))

async def registrar_moto(marca, placa, nombre_dueño,):
    datos = await leer_datos()

    for dato in datos:
        if dato["placa"] == placa:
            raise ValueError(f"El vehiculo de placa {placa} ya esta registrado")

    nuevo_registro = {"placa": placa, "marca": marca, "titular": nombre_dueño, "estado": "en diagnostico", "costo": 0, "falla_reportada": "en revision"}
    datos.append(nuevo_registro)

    await guardar_datos(datos)
    return nuevo_registro

async def listar_datos():
    if not datos:
        ValueError("No hay vehiculos registrados")
    return datos

async def actualizar_datos(estado, placa, costo, falla_reportada):
    datos = leer_datos()

    for dato in datos:
        if dato["placa"] == placa:
            dato["estado"] == estado
            dato["costo"] == costo
            dato["falla_reportada"] == falla_reportada
            await guardar_datos(datos)
            return dato

async def verificar_moto(placa):
    datos = leer_datos()
    
    for dato in datos:
        if dato[placa] == placa:
            print(f"La moto registrada con la placa {placa} ya se encuentra en el taller")


