from django.shortcuts import get_object_or_404,render
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from io import BytesIO
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, legal, landscape
from django.views.generic import View
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages
import datetime
from django.utils.dateparse import parse_date
import os, sys, subprocess
import webbrowser
from datospersonalesapp.models import Paciente
from laboratorioapp.models import Examen_Hematologia, Examen_Heces, Examen_Orina, Examen_General, Examen_Quimica_Sanguinea, Examen_Especiales
from laboratorioapp.forms import HematologiaForm, archivoForm, orinaForm, hecesForm, generalForm, especialesForm, quimicaForm, archivoOrinaForm, archivoHecesForm, archivoQuimicaForm, archivoEspecialesForm, archivoNuevoIngresoForm

# Estas son las vistas que se utilizan para el modulo de laboratorio clinico.
@login_required(login_url='logins')
def laboratorio_list(request):
    pacientes=Paciente.objects.filter(estadoExpediente='A')
    return render(request,"laboratorio/laboratorio_list.html",{'personalpaciente':pacientes})

@login_required(login_url='logins')
def hematologia_list(request):
    hematologia=Examen_Hematologia.objects.all()
    return render(request,"laboratorio/hematologia_list.html",{'hematologia':hematologia})

@login_required(login_url='logins')
def examen_heces_list(request):
    examen_heces=Examen_Heces.objects.all()
    return render(request,"laboratorio/examen_heces_list.html",{'examen_heces':examen_heces})

@login_required(login_url='logins')
def examen_orina_list(request):
    examen_orina=Examen_Orina.objects.all()
    return render(request,"laboratorio/examen_orina_list.html",{'examen_orina':examen_orina})

@login_required(login_url='logins')
def examen_general_list(request):
    examen_general=Examen_General.objects.all()
    return render(request,"laboratorio/examen_general_list.html",{'examen_general':examen_general})

@login_required(login_url='logins')
def examen_quimica_list(request):
    examen_quimica=Examen_Quimica_Sanguinea.objects.all()
    return render(request,"laboratorio/examen_quimica_list.html",{'examen_quimica':examen_quimica})

@login_required(login_url='logins')
def examen_especiales_list(request):
    examen_especiales=Examen_Especiales.objects.all()
    return render(request,"laboratorio/examen_especiales_list.html",{'examen_especiales':examen_especiales})

@login_required(login_url='logins')
def hematologia_nuevo(request,pk):
    paciente = Paciente.objects.get(pk=pk)
    info = ""
    form = HematologiaForm()
    hm = request.POST.get('hemoglobina')
    mcv = request.POST.get('mcv')
    ch = request.POST.get('mch')
    chc = request.POST.get('mchc')
    subir = request.POST.get('eleccion')
    archivos = request.FILES.get('archivo')
    if request.method == "POST":
        if subir == "cargarArchivo":
            data1={'paciente':Paciente.objects.filter(codigoPaciente = request.POST.get('codigoPaciente')),'edad':int(request.POST.get('edad')),'archivo':archivos}
            archivo = archivoForm(data1,request.FILES or None)
            if archivo.is_valid():
                archivoHematologia = archivo.save(commit=False)
                archivoHematologia.nombreRecibido = request.user
                archivoHematologia.fechaIngreso = timezone.now()
                archivoHematologia.fechaModificacion = timezone.now()
                archivoHematologia.save()
                info = "Datos Guardados Exitosamente"
                return redirect('laboratorio-list')
            else:
                form=HematologiaForm()
                info = "Ocurrio un error los datos no se guardaron"
        else:
            data2={'paciente':Paciente.objects.filter(codigoPaciente = request.POST.get('codigoPaciente')),'edad':int(request.POST.get('edad')),'hemoglobina':float(hm.replace(',', '.')),
            'mcv':float(mcv.replace(',', '.')),'mch':float(ch.replace(',', '.')),'mchc':float(chc.replace(',', '.')),
            'hematocrito':int(request.POST.get('hematocrito')),'globulosBlancos':int(request.POST.get('globulosBlancos')),'globulosRojos':int(request.POST.get('globulosRojos')),'plaquetas':int(request.POST.get('plaquetas')),
            'neutrofilos':int(request.POST.get('neutrofilos')),'linfocitos':int(request.POST.get('linfocitos')),'monocitos':int(request.POST.get('monocitos')),'eosinofilos':int(request.POST.get('eosinofilos')),
            'basofilos':int(request.POST.get('basofilos')),'eritrosedimentacion':request.POST.get('eritrosedimentacion'),'gotaGruesa':request.POST.get('gotaGruesa')}
            form = HematologiaForm(data2,request.POST or None)
            if form.is_valid():
                examenHematologia = form.save(commit=False)
                examenHematologia.nombreRecibido = request.user
                examenHematologia.fechaIngreso = timezone.now()
                examenHematologia.fechaModificacion = timezone.now()
                examenHematologia.save()
                info = "Datos Guardados Exitosamente"
                return redirect('hematologia-view',pk=examenHematologia.codExamen_Hematologia)
            else:
                form=HematologiaForm()
                info = "Ocurrio un error los datos no se guardaron"
    return render(request,"laboratorio/hematologia_editar.html",{'form':form,'informacion':info,'paciente':paciente})

@login_required(login_url='logins')
def paciente_detalle(request, pk):
    paciente = Paciente.objects.get(pk=pk) 
    return render(request, "laboratorio/hematologia_editar.html", {'paciente':paciente})

@login_required(login_url='logins')
def examen_heces_nuevo(request, pk):
    paciente = Paciente.objects.get(pk=pk)
    info = ""
    form = hecesForm()
    subir = request.POST.get('eleccion')
    archivos = request.FILES.get('archivo')
    if request.method == "POST":
        if subir == "cargarArchivo":
            data1={'paciente':Paciente.objects.filter(codigoPaciente = request.POST.get('codigoPaciente')),'edad':int(request.POST.get('edad')),'archivo':archivos}
            archivo = archivoHecesForm(data1,request.FILES or None)
            if archivo.is_valid():
                archivoHeces = archivo.save(commit=False)
                archivoHeces.nombreRecibido = request.user
                archivoHeces.fechaIngreso = timezone.now()
                archivoHeces.fechaModificacion = timezone.now()
                archivoHeces.save()
                info = "Datos Guardados Exitosamente"
                return redirect('laboratorio-list')
            else:
                form=hecesForm()
                info = "Ocurrio un error los datos no se guardaron"
        else:
            data2={'paciente':Paciente.objects.filter(codigoPaciente = request.POST.get('codigoPaciente')),'edad':int(request.POST.get('edad')),
                'color':request.POST.get('color'),'consistencia':request.POST.get('consistencia'),'mucus':request.POST.get('mucus'),
                'protoActivos':request.POST.get('protoActivos'),'protoQuistes':request.POST.get('protoQuistes'),'metazoarios':request.POST.get('metazoarios'),
                'leucocitos':request.POST.get('leucocitos'),'hematies':request.POST.get('hematies'),'macro':request.POST.get('macro'),
                'micro':request.POST.get('micro'),'observaciones':request.POST.get('observaciones')
            }
            form = hecesForm(data2,request.POST or None)
            if form.is_valid():
                examenHeces = form.save(commit=False)
                examenHeces.nombreRecibido = request.user
                examenHeces.fechaIngreso = timezone.now()
                examenHeces.fechaModificacion = timezone.now()
                examenHeces.save()
                info = "Datos Guardados Exitosamente"
                return redirect('laboratorio-list')
            else:
                form=hecesForm()
                info = "Ocurrio un error los datos no se guardaron"
    return render(request, "laboratorio/examen_heces_editar.html", {'paciente':paciente,'form':form,'informacion':info})

@login_required(login_url='logins')
def examen_orina_nuevo(request, pk):
    paciente = Paciente.objects.get(pk=pk)
    info = ""
    form = orinaForm()
    ph=request.POST.get('ph')
    b=request.POST.get('bilirrubina')
    u=request.POST.get('urobilinigeno')
    h=request.POST.get('hematies')
    subir = request.POST.get('eleccion')
    archivos = request.FILES.get('archivo')
    if request.method == "POST":
        if subir == "cargarArchivo":
            data1={'paciente':Paciente.objects.filter(codigoPaciente = request.POST.get('codigoPaciente')),'edad':int(request.POST.get('edad')),'archivo':archivos}
            archivo = archivoOrinaForm(data1,request.FILES or None)
            if archivo.is_valid():
                archivoOrina = archivo.save(commit=False)
                archivoOrina.nombreRecibido = request.user
                archivoOrina.fechaIngreso = timezone.now()
                archivoOrina.fechaModificacion = timezone.now()
                archivoOrina.save()
                info = "Datos Guardados Exitosamente"
                return redirect('laboratorio-list')
            else:
                form=orinaForm()
                info = "Ocurrio un error los datos no se guardaron"
        else:
            data2={'paciente':Paciente.objects.filter(codigoPaciente = request.POST.get('codigoPaciente')),'edad':int(request.POST.get('edad')),
                'color':request.POST.get('color'),'aspecto':request.POST.get('aspecto'),'ph':float(ph.replace(',', '.')),'nitritos':request.POST.get('nitritos'),
                'densidad':int(request.POST.get('densidad')),'proteinas':request.POST.get('proteinas'),'cetonicos':request.POST.get('cetonicos'),
                'glucosa':int(request.POST.get('glucosa')),'bilirrubina':float(b.replace(',','.')),'urobilinigeno':float(u.replace(',','.')),
                'leucocitos':int(request.POST.get('leucocitos')),'hematies':float(h.replace(',','.')),'epiteliales':request.POST.get('epiteliales'),
                'cristales':request.POST.get('cristales'),'cilindros':request.POST.get('cilindros'),'sangre':int(request.POST.get('sangre')),
                'esterasaLeucocitaria':int(request.POST.get('esterasaLeucocitaria')),'bacterias':request.POST.get('bacterias'),'observaciones':request.POST.get('observaciones')
            }
            form = orinaForm(data2,request.POST or None)
            if form.is_valid():
                examenOrina = form.save(commit=False)
                examenOrina.nombreRecibido = request.user
                examenOrina.fechaIngreso = timezone.now()
                examenOrina.fechaModificacion = timezone.now()
                examenOrina.save()
                info = "Datos Guardados Exitosamente"
                return redirect('laboratorio-list')
            else:
                form=orinaForm()
                info = "Ocurrio un error los datos no se guardaron"
    return render(request, "laboratorio/examen_orina_editar.html", {'paciente':paciente,'form':form, 'informacion':info})

@login_required(login_url='logins')
def examen_nuevo_ingreso_nuevo(request, pk):
    paciente = Paciente.objects.get(pk=pk)
    info = ""
    form = generalForm()
    ph=request.POST.get('ph')
    b=request.POST.get('bilirrubina')
    u=request.POST.get('urobilinigeno')
    h=request.POST.get('hematiesOrina')
    subir = request.POST.get('eleccion')
    archivos = request.FILES.get('archivo')
    if request.method == "POST":
        if subir == "cargarArchivo":
            data1={'paciente':Paciente.objects.filter(codigoPaciente = request.POST.get('codigoPaciente')),'edad':int(request.POST.get('edad')),'archivo':archivos}
            archivo = archivoNuevoIngresoForm(data1,request.FILES or None)
            if archivo.is_valid():
                archivoNuevoIngreso = archivo.save(commit=False)
                archivoNuevoIngreso.nombreRecibido = request.user
                archivoNuevoIngreso.fechaIngreso = timezone.now()
                archivoNuevoIngreso.fechaModificacion = timezone.now()
                archivoNuevoIngreso.save()
                info = "Datos Guardados Exitosamente"
                return redirect('laboratorio-list')
            else:
                form=generalForm()
                info = "Ocurrio un error los datos no se guardaron"
        else:
            data2={'paciente':Paciente.objects.filter(codigoPaciente = request.POST.get('codigoPaciente')),'edad':int(request.POST.get('edad')),
                'colorOrina':request.POST.get('colorOrina'),'aspecto':request.POST.get('aspecto'),'ph':float(ph.replace(',', '.')),'nitritos':request.POST.get('nitritos'),
                'densidad':int(request.POST.get('densidad')),'proteinas':request.POST.get('proteinas'),'cetonicos':request.POST.get('cetonicos'),
                'glucosa':int(request.POST.get('glucosa')),'bilirrubina':float(b.replace(',','.')),'urobilinigeno':float(u.replace(',','.')),
                'leucocitosOrina':int(request.POST.get('leucocitosOrina')),'hematiesOrina':float(h.replace(',','.')),'epiteliales':request.POST.get('epiteliales'),
                'cristales':request.POST.get('cristales'),'cilindros':request.POST.get('cilindros'),'sangre':int(request.POST.get('sangre')),
                'esterasaLeucocitaria':int(request.POST.get('esterasaLeucocitaria')),'bacterias':request.POST.get('bacterias'),'levaduras':request.POST.get('levaduras'),
                'otros':request.POST.get('otros'),'hematocrito':int(request.POST.get('hematocrito')),'hemoglobina':request.POST.get('hemoglobina'),'serologia':request.POST.get('serologia'),'consistencia':request.POST.get('consistencia'),
                'colorHeces':request.POST.get('colorHeces'),'mucus':request.POST.get('mucus'),'protoActivos':request.POST.get('protoActivos'),'protoQuistes':request.POST.get('protoQuistes'),'metazoarios':request.POST.get('metazoarios'),
                'leucocitosHeces':request.POST.get('leucocitosHeces'),'hematiesHeces':request.POST.get('hematiesHeces'),'macro':request.POST.get('macro'),'micro':request.POST.get('micro')
            }
            form = generalForm(data2,request.POST or None)
            if form.is_valid():
                examenGeneral = form.save(commit=False)
                examenGeneral.nombreRecibido = request.user
                examenGeneral.fechaIngreso = timezone.now()
                examenGeneral.fechaModificacion = timezone.now()
                examenGeneral.save()
                info = "Datos Guardados Exitosamente"
                return redirect('laboratorio-list')
            else:
                form=generalForm()
                info = "Ocurrio un error los datos no se guardaron"
    return render(request, "laboratorio/examen_nuevo_ingreso_editar.html", {'paciente':paciente,'form':form, 'informacion':info})

@login_required(login_url='logins')
def quimica_sanguinea_nuevo(request, pk):
    paciente = Paciente.objects.get(pk=pk)
    info = ""
    form = quimicaForm()
    ph1=request.POST.get('ph')
    b=request.POST.get('bilirrubina')
    u=request.POST.get('urobilinigeno')
    h=request.POST.get('hematies')
    subir = request.POST.get('eleccion')
    archivos = request.FILES.get('archivo')
    if request.method == "POST":
        if subir == "cargarArchivo":
            data1={'paciente':Paciente.objects.filter(codigoPaciente = request.POST.get('codigoPaciente')),'edad':int(request.POST.get('edad')),'archivo':archivos}
            archivo = archivoQuimicaForm(data1,request.FILES or None)
            if archivo.is_valid():
                archivoQuimica = archivo.save(commit=False)
                archivoQuimica.nombreRecibido = request.user
                archivoQuimica.fechaIngreso = timezone.now()
                archivoQuimica.fechaModificacion = timezone.now()
                archivoQuimica.save()
                info = "Datos Guardados Exitosamente"
                return redirect('laboratorio-list')
            else:
                form=quimicaForm()
                info = "Ocurrio un error los datos no se guardaron"
        else:
            data2={'paciente':Paciente.objects.filter(codigoPaciente = request.POST.get('codigoPaciente')),'edad':int(request.POST.get('edad')),
                'glucosa':int(request.POST.get('glucosa')),'glucosaPospandrial':int(request.POST.get('glucosaPospandrial')),'colesterol':int(request.POST.get('colesterol')),'trigliceridos':int(request.POST.get('trigliceridos')),
                'acidoUrico':float(request.POST.get('acidoUrico')),'creatinina':float(request.POST.get('creatinina')),'hdl':int(request.POST.get('hdl')),
                'ldl':int(request.POST.get('ldl')),'tgo':int(request.POST.get('tgo')),'tgp':int(request.POST.get('tgp')),
                'bilirrubinaTotal':float(request.POST.get('bilirrubinaTotal')),'bilirrubinaDirecta':float(request.POST.get('bilirrubinaDirecta')),'bilirrubinaIndirecta':float(request.POST.get('bilirrubinaIndirecta')),
                'tiempoProtrombina':int(request.POST.get('tiempoProtrombina')),'tiempoTromboplastina':int(request.POST.get('tiempoTromboplastina')),'tiempoSangramiento':int(request.POST.get('tiempoSangramiento')),
                'tiempoCoagulacion':int(request.POST.get('tiempoCoagulacion')),'eritrosedimentacion':int(request.POST.get('eritrosedimentacion')),'glucosaAjustada':request.POST.get('glucosaAjustada'),
                'pospandrialAjustada':request.POST.get('pospandrialAjustada'),'colesterolAjustada':request.POST.get('colesterolAjustada'),'trigliceridosAjustada':request.POST.get('trigliceridosAjustada'),
                'uricoAjustada':request.POST.get('uricoAjustada'),'creatininaAjustada':request.POST.get('creatininaAjustada'),'hdlAjustada':request.POST.get('hdlAjustada'),'ldlAjustada':request.POST.get('ldlAjustada'),
                'tgoAjustada':request.POST.get('tgoAjustada'),'tgpAjustada':request.POST.get('tgpAjustada'),'bTotalAjustada':request.POST.get('bTotalAjustada'),'bDirectaAjustada':request.POST.get('bDirectaAjustada'),
                'bIndirectaAjustada':request.POST.get('bIndirectaAjustada'),'protrombinaAjustada':request.POST.get('protrombinaAjustada'),'tromboplastinaAjustada':request.POST.get('tromboplastinaAjustada'),
                'sangramientoAjustada':request.POST.get('sangramientoAjustada'),'coagulacionAjustada':request.POST.get('coagulacionAjustada'),'eritrosedimentacionAjustada':request.POST.get('eritrosedimentacionAjustada')
            }
            form = quimicaForm(data2,request.POST or None)
            if form.is_valid():
                examenQuimica = form.save(commit=False)
                examenQuimica.nombreRecibido = request.user
                examenQuimica.fechaIngreso = timezone.now()
                examenQuimica.fechaModificacion = timezone.now()
                examenQuimica.save()
                info = "Datos Guardados Exitosamente"
                return redirect('laboratorio-list')
            else:
                form=quimicaForm()
                info = "Ocurrio un error los datos no se guardaron"
    return render(request, "laboratorio/quimica_sanguinea_editar.html", {'paciente':paciente,'form':form, 'informacion':info})

@login_required(login_url='logins')
def pruebas_especiales_nuevo(request, pk):
    paciente = Paciente.objects.get(pk=pk)
    info = ""
    form = especialesForm()
    subir = request.POST.get('eleccion')
    archivos = request.FILES.get('archivo')
    if request.method == "POST":
        if subir == "cargarArchivo":
            data1={'paciente':Paciente.objects.filter(codigoPaciente = request.POST.get('codigoPaciente')),'edad':int(request.POST.get('edad')),'archivo':archivos}
            archivo = archivoEspecialesForm(data1,request.FILES or None)
            if archivo.is_valid():
                archivoEspeciales = archivo.save(commit=False)
                archivoEspeciales.nombreRecibido = request.user
                archivoEspeciales.fechaIngreso = timezone.now()
                archivoEspeciales.fechaModificacion = timezone.now()
                archivoEspeciales.save()
                info = "Datos Guardados Exitosamente"
                return redirect('laboratorio-list')
            else:
                form=especialesForm()
                info = "Ocurrio un error los datos no se guardaron"
        else:
            data2={'paciente':Paciente.objects.filter(codigoPaciente = request.POST.get('codigoPaciente')),'edad':int(request.POST.get('edad')),
                'tipoExamen':request.POST.get('tipoExamen'),'resultado':request.POST.get('resultado')
            }
            form = especialesForm(data2,request.POST or None)
            if form.is_valid():
                examenEspeciales = form.save(commit=False)
                examenEspeciales.nombreRecibido = request.user
                examenEspeciales.fechaIngreso = timezone.now()
                examenEspeciales.fechaModificacion = timezone.now()
                examenEspeciales.save()
                info = "Datos Guardados Exitosamente"
                return redirect('laboratorio-list')
            else:
                form=especialesForm()
                info = "Ocurrio un error los datos no se guardaron"
    return render(request, "laboratorio/pruebas_especiales_editar.html", {'paciente':paciente,'form':form, 'informacion':info})

@login_required(login_url='logins')
def hematologia_detalle(request,pk):
    hematologia = Examen_Hematologia.objects.get(pk=pk)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(BASE_DIR,"exameneslab/")
    return render(request, "laboratorio/examen_hematologia_detalle.html", {'hematologia':hematologia,'path':MEDIA_ROOT})

@login_required(login_url='logins')
def examen_heces_detalle(request,pk):
    examen_heces = Examen_Heces.objects.get(pk=pk)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(BASE_DIR,"exameneslab/")
    return render(request, "laboratorio/examen_heces_detalle.html", {'examen_heces':examen_heces,'path':MEDIA_ROOT})

@login_required(login_url='logins')
def examen_general_detalle(request,pk):
    examen_general = Examen_General.objects.get(pk=pk)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(BASE_DIR,"exameneslab/")
    return render(request, "laboratorio/examen_general_detalle.html", {'examen_general':examen_general,'path':MEDIA_ROOT})

@login_required(login_url='logins')
def examen_orina_detalle(request,pk):
    examen_orina = Examen_Orina.objects.get(pk=pk)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(BASE_DIR,"exameneslab/")
    return render(request, "laboratorio/examen_orina_detalle.html", {'examen_orina':examen_orina,'path':MEDIA_ROOT})

@login_required(login_url='logins')
def examen_quimica_detalle(request,pk):
    examen_quimica = Examen_Quimica_Sanguinea.objects.get(pk=pk)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(BASE_DIR,"exameneslab/")
    return render(request, "laboratorio/examen_quimica_detalle.html", {'examen_quimica':examen_quimica,'path':MEDIA_ROOT})

@login_required(login_url='logins')
def examen_especiales_detalle(request,pk):
    examen_especiales = Examen_Especiales.objects.get(pk=pk)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(BASE_DIR,"exameneslab/")
    return render(request, "laboratorio/examen_especiales_detalle.html", {'examen_especiales':examen_especiales,'path':MEDIA_ROOT})

@login_required(login_url='logins')
def abrir_archivo_heces(request,pk):
    examen_heces = Examen_Heces.objects.get(pk=pk)
    pathAux=str(examen_heces.archivo)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(BASE_DIR,"exameneslab/") + pathAux
    webbrowser.open(os.path.abspath(MEDIA_ROOT))
    #archivo = os.startfile(MEDIA_ROOT)
    return render(request, "laboratorio/examen_heces_detalle.html", {'examen_heces':examen_heces,'path':MEDIA_ROOT})

@login_required(login_url='logins')
def abrir_archivo_hematologia(request,pk):
    hematologia = Examen_Hematologia.objects.get(pk=pk)
    pathAux=str(hematologia.archivo)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(BASE_DIR,"exameneslab/") + pathAux
    #subprocess.Popen([MEDIA_ROOT],shell=True)
    #archivo = os.system("evince "+MEDIA_ROOT)
    #webbrowser.open("http://www.google.com.sv", new=2, autoraise=True)
    #archivo = os.startfile(MEDIA_ROOT)
    #opener ="start"
    subprocess.call(('open', MEDIA_ROOT))
    #subprocess.call('cmd /c start "" "'+ "workspace/exameneslab/hematologia/voucherReporte04-10-2016_3.pdf" +'"')
    return render(request, "laboratorio/examen_hematologia_detalle.html", {'hematologia':hematologia,'path':MEDIA_ROOT})

@login_required(login_url='logins')
def abrir_archivo_orina(request,pk):
    examen_orina = Examen_Orina.objects.get(pk=pk)
    pathAux=str(examen_orina.archivo)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(BASE_DIR,"exameneslab/") + pathAux
    #archivo = os.startfile(MEDIA_ROOT)
    return render(request, "laboratorio/examen_orina_detalle.html", {'examen_orina':examen_orina,'path':MEDIA_ROOT})

@login_required(login_url='logins')
def abrir_archivo_general(request,pk):
    examen_general = Examen_General.objects.get(pk=pk)
    pathAux=str(examen_general.archivo)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(BASE_DIR,"exameneslab/") + pathAux
    #archivo = os.startfile(MEDIA_ROOT)
    return render(request, "laboratorio/examen_general_detalle.html", {'examen_general':examen_general,'path':MEDIA_ROOT})

@login_required(login_url='logins')
def abrir_archivo_quimica(request,pk):
    examen_quimica = Examen_Quimica_Sanguinea.objects.get(pk=pk)
    pathAux=str(examen_quimica.archivo)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(BASE_DIR,"exameneslab/") + pathAux
    #archivo = os.startfile(MEDIA_ROOT)
    return render(request, "laboratorio/examen_quimica_detalle.html", {'examen_quimica':examen_quimica,'path':MEDIA_ROOT})

@login_required(login_url='logins')
def abrir_archivo_especiales(request,pk):
    examen_especiales = Examen_Especiales.objects.get(pk=pk)
    pathAux=str(examen_especiales.archivo)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(BASE_DIR,"exameneslab/") + pathAux
    #archivo = os.startfile(MEDIA_ROOT)
    return render(request, "laboratorio/examen_especiales_detalle.html", {'examen_especiales':examen_especiales,'path':MEDIA_ROOT})

#Imprimir examen de hematologia
@login_required(login_url='logins')
def hematologiaPDF(request,pk):
    hematologia = Examen_Hematologia.objects.get(pk=pk)
    # Create the HttpResponse object with the appropriate PDF headers.
    #paciente = hematologia.paciente.nombrePrimero
    #filename = str(paciente)+'.pdf'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename="Paciente.pdf"'
    minerva_imagen = settings.MEDIA_ROOT+'/imagenes/ues.jpg'
    medicina_imagen = settings.MEDIA_ROOT+'/imagenes/microscopio.jpg'
    buffer = BytesIO()

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(buffer,pagesize = A4)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawImage(minerva_imagen, 0, 680, 200, 120,preserveAspectRatio=True)
    p.drawImage(medicina_imagen, 400, 680, 200, 120,preserveAspectRatio=True)
    #p.drawImage(minerva_imagen, 0, A4[1]/2, width=400, height=400)
    #Margen izquierdo
    p.line(30,250,30,815)
    #Margen inferior
    p.line(30,250,565,250)
    #margen derecho
    p.line(565,250,565,815)
    #Margen superior
    p.line(30,815,565,815)
    p.setFont("Helvetica", 13)
    p.drawString(197, 790, "UNIVERSIDAD DE EL SALVADOR")
    p.drawString(212, 770, "BIENESTAR UNIVERSITARIO")
    p.setFont("Helvetica", 13)
    p.drawString(187, 750, "CENTRO DE SALUD UNIVERSITARIO")
    p.setFont("Helvetica", 16)
    p.drawString(209, 730, "LABORATORIO CLINICO")
    p.setFont("Helvetica", 13)
    p.drawString(197, 710, "TELEFONO: 2511-2010 EXT.: 2010")
    #Doble lineas divisoras
    p.line(30,670,565,670)
    p.line(30,668,565,668)
    #Linea divisora vertical izquierda
    p.line(170,670,170,815)
    #Linea divisora vertical derecha
    p.line(430,670,430,815)
    
    #Resultados recuperados datos personales
    p.setFont("Helvetica", 13)
    p.drawString(40, 650, "PACIENTE: ")
    p.drawString(130, 650, str(hematologia.paciente.nombrePrimero)+" "+str(hematologia.paciente.nombreSegundo)+" "+str(hematologia.paciente.apellidoPrimero)+" "+str(hematologia.paciente.apellidoSegundo))
    p.drawString(350, 650, "EDAD: ")
    p.drawString(400, 650, str(hematologia.edad))
    #p.drawString(430, 650, "")
    p.drawString(40, 630, "FECHA: ")
    p.drawString(130, 630, str(hematologia.fechaIngreso.day)+"/"+str(hematologia.fechaIngreso.month)+"/"+str(hematologia.fechaIngreso.year))
    #Linea divisora horizontal
    p.line(30,620,565,620)
    #Titulo del examen
    p.drawString(250, 600, "HEMATOLOGIA")
    #Linea divisora horizontal
    p.line(30,580,565,580)
    #Resultados del examen de hematologia
    p.setFont("Helvetica", 10)
    p.drawString(40, 530, "HEMATOCRITO:")
    p.drawString(120, 530, str(hematologia.hematocrito))
    p.drawString(150, 530, "%")


    p.drawString(40, 500, "HEMOGLOBINA:")
    p.drawString(120, 500, str(hematologia.hemoglobina))
    p.drawString(170, 500, "g/dl")


    p.drawString(40, 470, "GLOBULOS BLANCOS:")
    p.drawString(150, 470, str(hematologia.globulosBlancos))
    p.drawString(200, 470, "xmmc")


    p.drawString(40, 440, "GLOBULOS ROJOS:")
    p.drawString(150, 440, str(hematologia.globulosRojos))
    p.drawString(200, 440, "xmmc")


    p.drawString(40, 410, "MCV:")
    p.drawString(90, 410, str(hematologia.mcv))


    p.drawString(40, 380, "MCH:")
    p.drawString(90, 380, str(hematologia.mch))


    p.drawString(40, 350, "MCHC:")
    p.drawString(90, 350, str(hematologia.mchc))

    #Linea divisora vertical central
    p.line(240,250,240,580)

    #Linea divisora vertical izquierda
    p.line(375,250,375,580)

    #Linea divisora horizontal
    p.line(240,560,565,560)

    #Titulo central
    p.drawString(250, 565, "DIFERENCIAL")

    #Resultados diferenciales
    p.drawString(250, 530, "NEUTROFILOS:")
    p.drawString(330, 530, str(hematologia.neutrofilos))
    p.drawString(355, 530, "%")


    p.drawString(250, 500, "LINFOCITOS:")
    p.drawString(330, 500, str(hematologia.linfocitos))
    p.drawString(355, 500, "%")


    p.drawString(250, 470, "MONOCITOS:")
    p.drawString(330, 470, str(hematologia.monocitos))
    p.drawString(355, 470, "%")


    p.drawString(250, 440, "EOSINOFILOS:")
    p.drawString(330, 440, str(hematologia.eosinofilos))
    p.drawString(355, 440, "%")


    p.drawString(250, 410, "BASOFILOS:")
    p.drawString(330, 410, str(hematologia.basofilos))
    p.drawString(355, 410, "%")


    p.drawString(410, 565, "ERITROSEDIMENTACION")
    p.drawString(385, 530, str(hematologia.eritrosedimentacion))



    p.drawString(410, 465, "GOTA GRUESA")
    p.drawString(385, 430, str(hematologia.gotaGruesa))


    p.drawString(250, 150, "Firma y Sello:")
    p.drawString(210, 170, str(hematologia.nombreRecibido))
    p.line(170,160,395,160)


    #Linea divisora horizontal
    p.line(375,480,565,480)
    p.line(375,455,565,455)
    p.line(375,395,565,395)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response