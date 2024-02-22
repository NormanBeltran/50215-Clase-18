from django.template import Template, Context, loader 
from django.http import HttpResponse
import random

import datetime
from aplicacion.models import *

def saludar(request):
    return HttpResponse("Bienvenidos a la Comision 50215 - Clase Django")

def bienvenida(request, nombre, apellido):
    respuesta = f"Te damos la bienvenida a la Comisión 50215 {apellido}, {nombre}"
    return HttpResponse(respuesta)

def bienvenido_html(request, nombre, apellido):
    hoy = datetime.datetime.now()
    respuesta = f"""
    <html>
    <h1>Bienvenidos al curso de Django!!</h1>
    <h2>Esta es la comision 50215</h2>
    <h2>Te damos la bienvenida a la Comisión 50215 {apellido}, {nombre}</h2>
    <h3> Hoy es {hoy} </h3>
    </html>
    """
    return HttpResponse(respuesta)

def bienvenido_template(request):
    miHtml = open("C:/CoderHouse/50215/Clase_18/proyecto/proyecto/plantillas/bienvenido.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    contexto = Context()
    respuesta = plantilla.render(contexto)
    return HttpResponse(respuesta)

#_______________________________  22/02/2024
def bienvenido_template1(request):
    hoy = datetime.datetime.now()
    nombre = "Amadeus"
    apellido = "Mozart"
    notas = [7,8,9,10,6,5]
    contexto = {"nombre": nombre, "apellido": apellido, "hoy": hoy, "notas": notas}
    plantilla = loader.get_template("bienvenido1.html") 
    respuesta = plantilla.render(contexto)
    return HttpResponse(respuesta)

def nuevo_curso(request):
    iComision = random.randint(20000, 30000)
    sNombre = "Python " + str(iComision)
    curso = Curso(nombre=sNombre, comision=iComision)
    curso.save()
    respuesta = f"<html><h1>Se guardo {sNombre} : {iComision}</h1></html>"
    return HttpResponse(respuesta)