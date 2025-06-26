from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#--------------------------------------------------------------

@app.get("/")
def read_root():
    return {"FastAPI corriendo, Don Chimbolio"}

#--------------------------------------------------------------

@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"saludo": f"Hola, {nombre}!"}

#--------------------------------------------------------------

@app.post("/enviar/{dato}")
def recibir_dato(dato: str):
    return {"respuesta": f"Me has enviado: {dato}"}

#--------------------------------------------------------------

class Persona(BaseModel):
    nombre: str
    cedula: str

@app.post("/registrar")
def registrar_persona(persona: Persona):
    return {
        "nombre_recibido": persona.nombre,
        "cedula_recibida": persona.cedula
    }

class Numeros(BaseModel):
    numero1: str
    numero2: str
    numero3: str
    numero4: str

@app.post("/numeros")
def ordenar_numeros(numeros: Numeros):
    # convierte a float
    lista_numeros = [
        float(numeros.numero1),
        float(numeros.numero2),
        float(numeros.numero3),
        float(numeros.numero4),
    ]

    mayor = max(lista_numeros)
    promedio = sum(lista_numeros) / len(lista_numeros)

    return {
        "valores": lista_numeros,
        "mayor": mayor,
        "promedio": promedio
    }
