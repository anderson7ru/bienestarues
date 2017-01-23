from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages
import time
from django.contrib.auth.decorators import login_required
from django.db import connection

#apps internas y externas
from datospersonalesapp.models import Paciente
from empleadosapp.models import Doctor
from enfermeriaapp.forms import ColaConsultaForm, ColaEnfermeriaForm
from enfermeriaapp.models import Cola_Enfermeria, Cola_Consulta
from signosvitalesapp.models import SignosVitales
from signosvitalesapp.forms import SignosForm

#Listado de las personas a las que se les han tomado los signos vitales
@login_required(login_url='logins')
def signosvitales_list(request):
    signos=SignosVitales.objects.order_by('-fechaIngreso','-horaIngreso')
    return render(request,"signosvitales/signosvitales_list.html",{'signos':signos})

#View para agregar los signos vitales a un determinado paciente
@login_required(login_url='logins')
def signosvitales_nuevo(request,pk):
    paciente = Paciente.objects.get(codigoPaciente=pk)
    doctores = Doctor.objects.all()
    #cursor = connection.cursor()
    #cursor.execute('SELECT distinct(d.codigoDoctor) as doctor,e.codigoEmpleado as empleado,e.nombrePrimero as nombrePrimero,e.nombreSegundo as nombreSegundo,e.apellidoPrimero as apellidoPrimero,e.apellidoSegundo as apellidoSegundo FROM empleadosapp_doctor as d inner join empleadosapp_empleado as e on d.codigoEmpleado_id=e.codigoEmpleado')
    #doctores = cursor.fetchall()
    form=SignosForm()
    if request.method == "POST":
        data = {'presionArterial':request.POST.get('presionArterial'),
            'talla':request.POST.get('talla'),'temperatura':request.POST.get('temperatura'),'peso':request.POST.get('peso'),'frecuenciaRespiratoria':int(request.POST.get('frecuenciaRespiratoria')),
            'frecuenciaCardiaca':int(request.POST.get('frecuenciaCardiaca'))
        }
        doctor ={'idDoctor':Doctor.objects.filter(codigoDoctor = request.POST.get('doctor'))
            
        }
        form = SignosForm(data)
        if form.is_valid():
            signosV = form.save(commit=False)
            datos = Paciente.objects.get(codigoPaciente=pk)
            colaEnfermeria = Cola_Enfermeria.objects.filter(idPaciente = pk)
            signosV.paciente = datos
            signosV.edad=datos.edad_paciente()
            signosV.nombreRecibido = request.user
            signosV.fechaIngreso = timezone.now()
            signosV.horaIngreso = time.strftime("%H:%M:%S") #Formato de 24 horas
            signosV.save()
            consultaForm = ColaConsultaForm(doctor)
            if consultaForm.is_valid():
                consulta = consultaForm.save(commit=False)
                consulta.nit = datos.nit
                consulta.hora = time.strftime("%H:%M:%S") #Formato de 24 horas
                consulta.save()
                colaEnfermeria.delete()
                messages.success(request,'Se han registrado exitosamente los signos vitales del paciente con el Expediente: '+datos.codigoPaciente)
                return redirect("signosvitales-list")
            else:
                messages.success(request,'No se registraron los signos vitales del paciente con el Expediente: '+datos.codigoPaciente)
                return redirect("signosvitales-list")
        else:
            form=SignosForm()
    return render(request,"signosvitales/signos_editar.html",{'form':form,'paciente':paciente,'doctores':doctores})
	
#View para consultar los signos vitales de un determinado paciente
@login_required(login_url='logins')
def signosvitales_detalle(request, pk):
	signosV = SignosVitales.objects.get(pk=pk) 
	datos =  Paciente.objects.get(codigoPaciente=signosV.paciente_id)
	return render(request, "signosvitales/signos_detalle.html", {'signos': signosV,'datos':datos})