from django.contrib import admin

# Register your models here.
#funcion para verificar q el usuario logueado es director
def is_director(user):
    return user.groups.filter(name='direccion').exists()

#funcion para verificar q el usuario logueado es jefe de enfermeria
def is_jefenfermeria(user):
    return user.groups.filter(name='jefe_enfermeria').exists()

#funcion para verificar q el usuario logueado es jefe de archivo
def is_jefarchivo(user):
    return user.groups.filter(name='jefe_archivo').exists()

#funcion para verificar q el usuario logueado es medico
def is_medico(user):
    return user.groups.filter(name='medicos').exists()

#funcion para verificar q el usuario logueado es ginecologo
def is_ginecologo(user):
    return user.groups.filter(name='ginecologos').exists()

#funcion para verificar q el usuario logueado es psicologo
def is_psicologo(user):
    return user.groups.filter(name='psicologos').exists()

#funcion para verificar q el usuario logueado es nutricionista
def is_nutricionista(user):
    return user.groups.filter(name='nutricionistas').exists()

#funcion para verificar q el usuario logueado es del area de enfermeria
def is_enfermera(user):
    return user.groups.filter(name='enfermeria').exists()

#funcion para verificar q el usuario logueado es del area de laboratorio
def is_laboratorio(user):
    return user.groups.filter(name='laboratorio').exists()

#funcion para verificar q el usuario logueado es del area de archivo
def is_archivo(user):
    return user.groups.filter(name='archivo').exists()

#funcion para verificar q el usuario logueado es administrador
def is_administrador(user):
    return user.groups.filter(name='administradores').exists()

#funcion para verificar q el usuario logueado es desarrollador
def is_desarrollador(user):
    return user.groups.filter(name='desarrolladores').exists()