from django.db import models

# Create your models here.
# Profesor, Estudiante, Curso, Entregable

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)

class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()
