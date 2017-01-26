from django.http import JsonResponse

from .models import AlimentosGrupo, GruposAlimentos

def get_alimentos(request):
    grupo_id = request.POST.get('grupos_id')
    alimentos = AlimentosGrupo.objects.none()
    options = '<option value="" selected="selected>-----------</option>'
    if grupo_id:
        alimentos = AlimentosGrupo.objects.filter(grupo=grupo_id)
    for x in alimentos:
        options += '<option value="%s">%s</option>' % (x.pk, x.alimento)
    response = {}
    response[alimentos] = options
    return JsonResponse(response)