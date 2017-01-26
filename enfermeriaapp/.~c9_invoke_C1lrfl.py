from django.shortcuts import render
from enfermeriaapp.models import Cola_Consulta, Cola_Enfermeria
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils import timezone
import time
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.db import connection
import json
from datospersonalesapp.models import Paciente
from nuevoingresoapp.models import Expediente_Provisional
from enfermeriaapp.forms import ColaEnfermeriaForm

# Vista para poner un nuevo paciente en la cola para la toma de signos vitales
@login_required(login_url='logins')
def cola_enfermeria_nuevo(request,pk):
    info = ""
    pacientes=Paciente.objects.filter(estadoExpediente='A').order_by('facultadE')
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(p.facultadE_id), f.nombreFacultad FROM datospersonalesapp_paciente as p, datospersonalesapp_facultad as f WHERE p.facultadE_id = f.codigoFacultad ORDER BY f.nombreFacultad')
    auxL = cursor.fetchall()
    if request.method == "GET":
        data = {'idPaciente':Paciente.objects.filter(codigoPaciente = pk)
            
        }
        form = ColaEnfermeriaForm(data)
        existe = Cola_Enfermeria.objects.filter(idPaciente = pk)
        if existe:
            info="El paciente ya existe en la cola"
        else:
            if form.is_valid():
                expediente = form.save(commit=False)
                expediente.hora = time.strftime("%H:%M:%S") #Formato de 24 horas
                expediente.save()
                info = "Datos Guardados Exitosamen"
                return render(request,"datospersonales/paciente_list.html",{'personalpaciente':pacientes,'datoFacult':auxL,'informacion':info})
            else:
                form=ColaEnfermeriaForm()
                info = "Ocurrio un error los datos no se guardaron"
    return render(request,"datospersonales/paciente_list.html",{'personalpaciente':pacientes,'datoFacult':auxL,'informacion':info})

#Muestra el listado de pacientes en cola para tomarles signos vitales
@login_required(login_url='logins')
def cola_enfermeria_list(request):
    cola=Cola_Enfermeria.objects.order_by('hora')
    return render(request,"enfermeriaapp/cola_enfermeria_list.html",{'cola':cola})

# Vista para borrar manualmente un paciente en la cola para la toma de signos vitales
@login_required(login_url='logins')
def cola_enfermeria_borrar(request,pk):
    cola=Cola_Enfermeria.objects.order_by('hora')
    info = ""
    if request.method == "GET":
        data = {'idPaciente':Paciente.objects.filter(codigoPaciente = pk)
            
        }
        form = ColaEnfermeriaForm(data)
        existe = Cola_Enfermeria.objects.filter(idPaciente = pk)
        if existe:
            if form.is_valid():
                existe.delete()
                info = "Datos eliminados exitosamente"
                return render(request,"enfermeriaapp/cola_enfermeria_list.html",{'cola':cola})
            else:
                form=ColaEnfermeriaForm()
                info = "Ocurrio un error no se pudo eliminar el paciente de la cola"
        else:
            info="El paciente no existe en la cola"

    return render(request,"enfermeriaapp/cola_enfermeria_list.html",{'cola':cola})

#Muestra el listado de pacientes en cola para pasar consulta
@login_required(login_url='logins')
def cola_consulta_list(request):
    cu
    cursor.execute('SELECT distinct(p.nit) as codigo, p.nombrePrimero as nombre,p.nombreSegundo as nombreSegundo, p.apellidoPrimero as apellido,c.hora,c.idDoctor_id as doctor FROM datospersonalesapp_paciente as p, enfermeriaapp_cola_consulta as c WHERE p.nit = c.nit')
    cursor2 = connection.cursor()
    cursor2.execute('SELECT distinct(p.nit) as codigo, p.nombrePrimero as nombre,p.nombreSegundo as nombreSegundo, p.apellidoPrimero as apellido,c.hora,c.idDoctor_id as doctor FROM datospersonalesapp_expediente_provisional as p, enfermeriaapp_cola_consulta as c WHERE p.nit = c.nit')
    cola = cursor.fetchall()
    cola += cursor2.fetchall()
    #cola=Cola_Consulta.objects.order_by('hora')
    return render(request,"enfermeriaapp/cola_consulta_list.html",{'cola':cola})


