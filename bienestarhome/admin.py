from django.contrib import admin

###############################
#PRIVILEGIOS UNICOS
#funcion para verificar q el usuario logueado es director
def is_director(user):
    return user.groups.filter(name__in=('desarrolladores','direccion')).exists()

#funcion para verificar q el usuario logueado es jefe de enfermeria
def is_jefenfermeria(user):
    return user.groups.filter(name__in=('desarrolladores','jefe_enfermeria')).exists()

#funcion para verificar q el usuario logueado es jefe de archivo
def is_jefarchivo(user):
    return user.groups.filter(name__in=('desarrolladores','jefe_archivo')).exists()

#funcion para verificar q el usuario logueado es medico
def is_medico(user):
    return user.groups.filter(name__in=('desarrolladores','medicos')).exists()

#funcion para verificar q el usuario logueado es ginecologo
def is_ginecologo(user):
    return user.groups.filter(name__in=('desarrolladores','ginecologos')).exists()

#funcion para verificar q el usuario logueado es psicologo
def is_psicologo(user):
    return user.groups.filter(name__in=('desarrolladores','psicologos')).exists()

#funcion para verificar q el usuario logueado es nutricionista
def is_nutricionista(user):
    return user.groups.filter(name__in=('desarrolladores','nutricionistas')).exists()

#funcion para verificar q el usuario logueado es del area de enfermeria
def is_enfermera(user):
    return user.groups.filter(name__in=('desarrolladores','enfermeria')).exists()

#funcion para verificar q el usuario logueado es del area de laboratorio
def is_laboratorio(user):
    return user.groups.filter(name__in=('desarrolladores','laboratorio')).exists()

#funcion para verificar q el usuario logueado es del area de archivo
def is_archivo(user):
    return user.groups.filter(name__in=('desarrolladores','archivo')).exists()

#funcion para verificar q el usuario logueado es administrador
def is_administrador(user):
    return user.groups.filter(name__in=('desarrolladores','administradores')).exists()

#funcion para verificar q el usuario logueado es desarrollador
def is_desarrollador(user):
    return user.groups.filter(name='desarrolladores').exists()

###############################
#USUARIOS GENERICOS
#PRIVILEGIOS SOLO DE GRUPO + ADMIN + DESARROLLADORES
#Director
def is_director1(user):
    return user.groups.filter(name__in=('administradores','desarrolladores','direccion')).exists()

#jefe de enfermeria
def is_jefenfermeria1(user):
    return user.groups.filter(name__in=('administradores','desarrolladores','jefe_enfermeria')).exists()

#jefe de archivo
def is_jefarchivo1(user):
    return user.groups.filter(name__in=('administradores','desarrolladores','jefe_archivo')).exists()

#medico
def is_medico1(user):
    return user.groups.filter(name__in=('administradores','desarrolladores','medicos')).exists()

#ginecologo
def is_ginecologo1(user):
    return user.groups.filter(name__in=('administradores','desarrolladores','ginecologos')).exists()

#psicologo
def is_psicologo1(user):
    return user.groups.filter(name__in=('administradores','desarrolladores','psicologos')).exists()

#nutricionista
def is_nutricionista1(user):
    return user.groups.filter(name__in=('administradores','desarrolladores','nutricionistas')).exists()

#area de enfermeria
def is_enfermera1(user):
    return user.groups.filter(name__in=('administradores','desarrolladores','enfermeria')).exists()

#area de laboratorio
def is_laboratorio1(user):
    return user.groups.filter(name__in=('administradores','desarrolladores','laboratorio')).exists()

#area de archivo
def is_archivo1(user):
    return user.groups.filter(name__in=('administradores','desarrolladores','archivo')).exists()

#OTROS USUARIOS NECESARIOS
#DETERMINADOS USUARIOS
def is_usuario1(user):
    return user.groups.filter(name__in=('medicos','ginecologos','psicologos','nutricionistas','administradores','desarrolladores')).exists()

def is_usuario2(user):
    return user.groups.filter(name__in=('jefe_archivo','archivo','administradores','desarrolladores')).exists()

def is_usuario3(user):
    return user.groups.filter(name__in=('direccion','jefe_archivo','archivo','administradores','desarrolladores')).exists()

def is_usuario4(user):
    return user.groups.filter(name__in=('direccion','jefe_enfermeria','administradores','desarrolladores')).exists()

def is_usuario5(user):
    return user.groups.filter(name__in=('direccion','enfermeria','administradores','desarrolladores')).exists()

def is_usuario6(user):
    return user.groups.filter(name__in=('jefe_enfermeria','enfermeria','desarrolladores')).exists()

def is_usuario9(user):
    return user.groups.filter(name__in=('enfermeria','archivo','administradores','desarrolladores')).exists()
	
def is_usuario10(user):
    return user.groups.filter(name__in=('enfermeria','medicos','ginecologos','psicologos','nutricionistas','administradores','desarrolladores')).exists()
	
def is_usuario11(user):
    return user.groups.filter(name__in=('direccion','jefe_enfermeria','archivo','administradores','desarrolladores')).exists()

def is_usuario12(user):
    return user.groups.filter(name__in=('jefe_enfermeria','enfermeria','administradores','desarrolladores')).exists()	

def is_usuario13(user):
    return user.groups.filter(name__in=('jefe_enfermeria','enfermeria','archivo','administradores','desarrolladores')).exists()
	
def is_usuario14(user):
    return user.groups.filter(name__in=('medicos','ginecologos','psicologos','nutricionistas')).exists()	

def is_usuario15(user):
    return user.groups.filter(name__in=('jefe_enfermeria','archivo','desarrolladores')).exists()	

#MENOS ESTOS USUARIOS
def is_usuario7(user):  
    return user.groups.exclude(name__in=('direccion','jefe_enfermeria','enfermeria','laboratorio')).exists()

def is_usuario8(user):
    return user.groups.exclude(name__in=('jefe_enfermeria','enfermeria','laboratorio')).exists()
    

    
    
""" 
direccion
medicos
ginecologos
psicologos
nutricionistas
laboratorio
jefe_enfermeria
enfermeria
jefe_archivo
archivo
administradores
desarrolladores
""" 