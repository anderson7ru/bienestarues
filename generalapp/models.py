# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datospersonalesapp.models import Paciente
from empleadosapp.models import Doctor
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.








## opciones para indicar el tipo de consulta
#
TCONSULTA_CHOICES = (
    ('PRV', 'Primera vez'),
    ('SUB', 'Subsecuente'),
)


## modelo de consulta, tabla generalapp_consulta
#
class Consulta(models.Model):
    # PK id = models.AutoField(primary_key=True)
    
    # FK hacia el expediente del pacientes
    cod_expediente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    # FK que permite identificar al doctor
    cod_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    nit_paciente = models.CharField(max_length=17)
    
    fecha = models.DateTimeField(auto_now=True)
    
    # primera vez o subsecuente
    tipo_consulta = models.CharField(max_length=50, choices=TCONSULTA_CHOICES)
    
    consulta_por = models.TextField()
    visto_bueno = models.CharField(max_length=2, null=True, blank=True)
    presenta_enfermedad = models.TextField(blank=True)
    
    antecedentes_personales = models.TextField(blank=True)
    antecedentes_familiares = models.TextField(blank=True)
    
    exploracion_clinica = models.TextField()
    diagnostico_principal = models.CharField(max_length=500, blank=True)
    otros_diagnosticos = models.TextField(blank=True)
    tratamiento = models.TextField(blank=True)
    
    observaciones = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)























# ## modelo de medicamento, tabla generalapp_medicamento
# #
# class Medicamento(models.Model):
#     # PK id = models.AutoField(primary_key=True)
#     nombre_medicamento = models.CharField(max_length=500)

# class Unidad(models.Model):
#     # PK id = models.AutoField(primary_key=True)
#     simbolo_unidad = models.CharField(max_length=50)
#     nombre_unidad = models.CharField(max_length=500)






## modelo de forma farmaceutica de los medicamentos, tabla generalapp_forma
#
class Forma(models.Model):
    # PK id = models.AutoField(primary_key=True)
    nombre_forma = models.CharField(max_length=200)

## modelo de via de administracion, tabla generalapp_via
#
class Via(models.Model):
    # PK id = models.AutoField(primary_key=True)
    nombre_via = models.CharField(max_length=200)

##
#



# class Via(models.Model):
#     # PK id = models.AutoField(primary_key=True)
#     nombre_via = models.CharField(max_length=500)







## modelo de receta, tabla generalapp_receta
#
class Receta(models.Model):
    # PK id = models.AutoField(primary_key=True)
    
    # FK hacia el expediente del paciente
    cod_expediente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    # FK que permite identificar al doctor
    cod_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    # FK hacia la consulta
    cod_consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    
    fecha = models.DateTimeField(auto_now=True)
    
    medicamento = models.TextField()
    
    observaciones = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)














# class Compuesto(models.Model):
#     # PK id = models.AutoField(primary_key=True)
    
#     # FK hacia el expediente del paciente
#     cod_expediente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
#     # FK que permite identificar al doctor
#     cod_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
#     # FK hacia la consulta
#     cod_consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    
#     fecha = models.DateTimeField(auto_now=True)
    
#     compuesto = models.TextField()
    
#     observaciones = models.TextField(blank=True)
    
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)













class AreaLab(models.Model):
    codigoArea = models.AutoField(primary_key=True)
    nombreArea = models.CharField(max_length=200)
    
    def __str__(self):
        return '%s' % (self.nombreArea.encode('utf8'))

class ExamenLab(models.Model):
    codigoExamen = models.AutoField(primary_key=True)
    codArea = models.ForeignKey(AreaLab, on_delete=models.CASCADE)
    nombreExamen = models.CharField(max_length=400)
    
    def __str__(self):
        return '%s' % (self.nombreExamen.encode('utf8'))










#
## modelo de orden de laboratorio
#
class OrdenLab(models.Model):
    # PK id = models.AutoField(primary_key=True)
    
    # FK hacia el expediente del paciente
    cod_expediente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    # FK que permite identificar al doctor
    cod_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    # FK hacia la consulta
    cod_consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    
    fecha = models.DateTimeField(auto_now=True)
    
    codArea = models.ForeignKey(AreaLab, on_delete=models.CASCADE)
    codExamen = ChainedForeignKey(ExamenLab, chained_field='codArea', chained_model_field='codArea', show_all=False, auto_choose=True)
    
    observaciones = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#
## modelo de referencia interna, tabla generalapp_referenciainterna
#
class ReferenciaInterna(models.Model):
    # PK id = models.AutoField(primary_key=True)
    
    # FK hacia el expediente del paciente
    cod_expediente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    # FK que permite identificar al doctor
    cod_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    # FK hacia la consulta
    cod_consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    
    fecha = models.DateTimeField(auto_now=True)
    
    referido_a = models.CharField(max_length=500)
    nombre_paciente = models.CharField(max_length=200)
    tipo_paciente = models.CharField(max_length=200)
    procedencia_paciente = models.CharField(max_length=200)
    motivo_referencia = models.TextField()
    
    observaciones = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#
## modelo de referencia externa, tabla generalapp_referenciaexterna
#
class ReferenciaExterna(models.Model):
    # PK id = models.AutoField(primary_key=True)
    
    # FK hacia el expediente del paciente
    cod_expediente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    # FK que permite identificar al doctor
    cod_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    # FK hacia la consulta
    cod_consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    
    fecha = models.DateTimeField(auto_now=True)
    referido_a = models.CharField(max_length=500)
    nombre_paciente = models.CharField(max_length=200)
    edad_paciente = models.PositiveSmallIntegerField()
    sexo_paciente = models.CharField(max_length=1)
    domicilio_paciente = models.CharField(max_length=500)
    telefono_paciente = models.CharField(max_length=9)
    
    presion_arterial = models.CharField(max_length=20)
    frecuencia_cardiaca = models.PositiveSmallIntegerField()
    frecuencia_respiratoria = models.PositiveSmallIntegerField()
    temperatura = models.DecimalField(max_digits=4, decimal_places=2)
    peso = models.PositiveSmallIntegerField()
    talla = models.DecimalField(max_digits=3, decimal_places=2)
    
    consulta_por = models.TextField()
    presenta_enfermedad = models.TextField(blank=True)
    antecedentes_personales = models.TextField(blank=True)
    examen_fisico = models.TextField()
    examenes_laboratorio = models.TextField(blank=True)
    impresion_diagnostica = models.TextField()
    
    observaciones = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#
## modelo de centro asistencial para referencia externa
#
class CentroAsistencial(models.Model):
    # PK id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return '%s' % (self.nombre)
#
##













class db29179_cie10(models.Model):
    id10 = models.CharField(max_length=10, primary_key=True)
    dec10 = models.CharField(max_length=400)
    grp10 = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return '%s' % (self.dec10.encode('utf8'))