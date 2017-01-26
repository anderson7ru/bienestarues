# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-08 21:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('datospersonalesapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PacienteInscripcion',
            fields=[
                ('codigoPlanificacion', models.AutoField(primary_key=True, serialize=False)),
                ('edad', models.PositiveIntegerField()),
                ('aniosEscolaridad', models.PositiveIntegerField(verbose_name=b'Anios de escolaridad')),
                ('primeraVida', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'S', max_length=1, verbose_name=b'1era vez en la vida')),
                ('primeraInstitucion', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'S', max_length=1, verbose_name=b'1era vez en la institucion')),
                ('embarazos', models.PositiveIntegerField(default=0)),
                ('partosTermino', models.PositiveIntegerField(default=0, verbose_name=b'Partos a Termino')),
                ('prematuros', models.PositiveIntegerField(default=0)),
                ('abortos', models.PositiveIntegerField(default=0)),
                ('vivos', models.PositiveIntegerField(default=0)),
                ('nacidosVivos', models.PositiveIntegerField(default=0, verbose_name=b'Nacidos Vivos')),
                ('nacidosMuertos', models.PositiveIntegerField(default=0, verbose_name=b'Nacidos Muertos')),
                ('partoVaginal', models.PositiveIntegerField(default=0, verbose_name=b'Partos via Vaginal')),
                ('partoOpereratorio', models.PositiveIntegerField(default=0, verbose_name=b'Partos Operatorios')),
                ('fup', models.DateField(blank=True, help_text=b'DD/MM/YYYY', null=True, verbose_name=b'FUP')),
                ('lactando', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'Esta Lactando')),
                ('ueProductoVivo', models.CharField(blank=True, choices=[(b'S', b'Si'), (b'N', b'No')], max_length=1, null=True, verbose_name=b'Producto Vivo')),
                ('ueTerminacion', models.CharField(blank=True, choices=[(b'A', b'Aborto'), (b'V', b'Parto Vaginal'), (b'O', b'Parto Operatorio')], max_length=1, null=True, verbose_name=b' ')),
                ('menarquia', models.PositiveIntegerField(help_text=b'anios')),
                ('fur', models.DateField(help_text=b'DD/MM/YYYY', verbose_name=b'FUR')),
                ('edadPrimeraVez', models.PositiveIntegerField(help_text=b'anios', verbose_name=b'Edad del primer coito')),
                ('dismenorrea', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'Dismenorrea')),
                ('cicloMenstrual', models.CharField(choices=[(b'R', b'Regulares'), (b'I', b'Irregulares')], default=b'R', max_length=1, verbose_name=b'Ciclos Menstruales')),
                ('duracionCiclo', models.PositiveIntegerField(help_text=b'dias', verbose_name=b'Duracion del ciclo')),
                ('sangramientos', models.CharField(choices=[(b'E', b'Escasos'), (b'M', b'Moderados'), (b'A', b'Abundantes')], default=b'M', max_length=1, verbose_name=b'Sangramientos')),
                ('duracionSangramiento', models.PositiveIntegerField(help_text=b'dias', verbose_name=b'Duracion del sangramiento')),
                ('fechaPap', models.DateField(blank=True, help_text=b'DD/MM/YYYY', null=True, verbose_name=b'Fecha del ultimo PAP')),
                ('resultado', models.CharField(blank=True, max_length=100, null=True)),
                ('agObservaciones', models.CharField(blank=True, max_length=500, null=True, verbose_name=b'Observaciones')),
                ('cefaleaIntensa', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'Cefalea Intensa')),
                ('trastCardiovascular', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'Transtorno Cardiovascular')),
                ('hta', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'HTA')),
                ('diabetes', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1)),
                ('trastHepaticos', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'Transtornos Hepaticos')),
                ('trastConvulsivo', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'Transtorno Convulsivo')),
                ('varices', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1)),
                ('tabaquismo', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1)),
                ('cirugiaPelv', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'Cirugia Pelvica')),
                ('infeccionPelv', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'Infeccion Pelvica')),
                ('alergias', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1)),
                ('vih', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'VIH+')),
                ('its', models.BooleanField(default=False, verbose_name=b'ITS')),
                ('apObservaciones', models.CharField(blank=True, max_length=500, null=True, verbose_name=b'Observaciones')),
                ('metAnticonceptivos', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'Ha utilizado metodos anticonceptivos?')),
                ('metUtilizado', models.CharField(blank=True, max_length=60, null=True, verbose_name=b'Metodo Utilizado')),
                ('metTiempo', models.PositiveIntegerField(blank=True, help_text=b'semanas', null=True, verbose_name=b'Por cuanto tiempo')),
                ('metLapso', models.CharField(choices=[(b'N', b'Ninguno'), (b'D', b'Dias'), (b'S', b'Semanas'), (b'M', b'Meses'), (b'A', b'Anos')], default=b'N', max_length=1, verbose_name=b' ')),
                ('metJustificar', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'Porque dejo de usarlo')),
                ('metLugar', models.CharField(blank=True, max_length=60, null=True, verbose_name=b'Donde lo obtuvo')),
                ('temperatura', models.DecimalField(decimal_places=1, max_digits=3)),
                ('pulso', models.PositiveIntegerField()),
                ('peso', models.PositiveIntegerField()),
                ('presionArterial', models.CharField(max_length=7, verbose_name=b'T.A.')),
                ('naCabeza', models.CharField(choices=[(b'N', b'Normal'), (b'A', b'Anormal')], default=b'N', max_length=1, verbose_name=b'Cabeza')),
                ('cabeza', models.CharField(blank=True, max_length=100, null=True, verbose_name=b' ')),
                ('naCuello', models.CharField(choices=[(b'N', b'Normal'), (b'A', b'Anormal')], default=b'N', max_length=1, verbose_name=b'Cuello')),
                ('cuello', models.CharField(blank=True, max_length=100, null=True, verbose_name=b' ')),
                ('naMamas', models.CharField(choices=[(b'N', b'Normal'), (b'A', b'Anormal')], default=b'N', max_length=1, verbose_name=b'Mamas')),
                ('mamas', models.CharField(blank=True, max_length=100, null=True, verbose_name=b' ')),
                ('naTorax', models.CharField(choices=[(b'N', b'Normal'), (b'A', b'Anormal')], default=b'N', max_length=1, verbose_name=b'Torax')),
                ('torax', models.CharField(blank=True, max_length=100, null=True, verbose_name=b' ')),
                ('naAbdomen', models.CharField(choices=[(b'N', b'Normal'), (b'A', b'Anormal')], default=b'N', max_length=1, verbose_name=b'Abdomen')),
                ('abdomen', models.CharField(blank=True, max_length=100, null=True, verbose_name=b' ')),
                ('naMiembros', models.CharField(choices=[(b'N', b'Normal'), (b'A', b'Anormal')], default=b'N', max_length=1, verbose_name=b'Miembros')),
                ('miembros', models.CharField(blank=True, max_length=100, null=True, verbose_name=b' ')),
                ('genitalesExternos', models.CharField(choices=[(b'N', b'Normal'), (b'A', b'Anormal')], default=b'N', max_length=1, verbose_name=b'Genitales Externos')),
                ('cistocele', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1)),
                ('gradoCistocele', models.PositiveIntegerField(blank=True, null=True, verbose_name=b'grado')),
                ('rectocele', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1)),
                ('gradoRectocele', models.PositiveIntegerField(blank=True, null=True, verbose_name=b'grado')),
                ('prolapsoUterino', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'Prolapso Uterino')),
                ('gradoProlapsoUterino', models.PositiveIntegerField(blank=True, null=True, verbose_name=b'grado')),
                ('vagina', models.CharField(choices=[(b'N', b'Normal'), (b'A', b'Anormal')], default=b'N', max_length=1)),
                ('snSecrecionVagina', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'Secrecion en vagina')),
                ('secrecionVagina', models.CharField(blank=True, max_length=100, null=True, verbose_name=b' ')),
                ('cuPalpacion', models.CharField(choices=[(b'N', b'Normal'), (b'A', b'Anormal')], default=b'N', max_length=1, verbose_name=b'Cuello Uterino Palpacion')),
                ('cuConsistencia', models.CharField(choices=[(b'N', b'Normal'), (b'A', b'Anormal')], default=b'N', max_length=1, verbose_name=b'Consistencia')),
                ('cuMovilidad', models.CharField(choices=[(b'N', b'Normal'), (b'A', b'Anormal')], default=b'N', max_length=1, verbose_name=b'Movilidad')),
                ('cuDolorMov', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'Dolor a la movilizacion')),
                ('sangrarTacto', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'Sangra al contacto')),
                ('tomaPap', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'Toma PAP')),
                ('cuObservaciones', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'Observaciones')),
                ('uteroPosicion', models.CharField(choices=[(b'A', b'Anteflexion'), (b'M', b'Retroflexion'), (b'P', b'Retroversion')], default=b'A', max_length=1, verbose_name=b'Utero Posicion')),
                ('uTamano', models.CharField(choices=[(b'N', b'Normal'), (b'A', b'Anormal')], default=b'N', max_length=1, verbose_name=b'Tamano')),
                ('uConsistencia', models.CharField(choices=[(b'N', b'Normal'), (b'A', b'Anormal')], default=b'N', max_length=1, verbose_name=b'Consistencia')),
                ('uMovilidad', models.CharField(choices=[(b'N', b'Normal'), (b'A', b'Anormal')], default=b'N', max_length=1, verbose_name=b'Movilidad')),
                ('uDolorMov', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'Dolor a la movilizacion')),
                ('usnTumores', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'Tumores')),
                ('uTumores', models.CharField(blank=True, max_length=100, null=True, verbose_name=b' ')),
                ('anexosLibres', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'Anexos Libres')),
                ('engrosados', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1)),
                ('aDolorPalpitacion', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'Dolor a la palpacion')),
                ('asnTumores', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'Tumores')),
                ('aTumores', models.CharField(blank=True, max_length=100, null=True, verbose_name=b' ')),
                ('fondoSaco', models.CharField(choices=[(b'N', b'Normal'), (b'A', b'Anormal')], default=b'N', max_length=1, verbose_name=b'Fondo de saco')),
                ('fechaInicioMetodo', models.DateField(blank=True, null=True, verbose_name=b'Fecha de inicio de metodo')),
                ('anticonceptivo', models.CharField(blank=True, choices=[(b'O', b'Oral'), (b'D', b'DIU'), (b'I', b'Inyectable'), (b'C', b'Condones'), (b'N', b'Norplant'), (b'E', b'Esterilizaciones'), (b'T', b'Otros')], max_length=1, null=True)),
                ('miONombre', models.CharField(blank=True, max_length=15, null=True, verbose_name=b'Nombre')),
                ('miOtros', models.CharField(blank=True, max_length=15, null=True, verbose_name=b'Otros')),
                ('diagnostico', models.CharField(blank=True, max_length=100, null=True)),
                ('indicaciones', models.CharField(blank=True, max_length=100, null=True)),
                ('fechaProximaConsulta', models.DateField(blank=True, null=True, verbose_name=b'Fecha de proxima consulta')),
                ('fechaIngreso', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha de Inscripcion')),
                ('nombreResponsable', models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'Nombre Responsable')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datospersonalesapp.Paciente', verbose_name=b'No expediente')),
            ],
        ),
        migrations.CreateModel(
            name='PacienteSubSecuentePF',
            fields=[
                ('codigoPlanificacionSub', models.AutoField(primary_key=True, serialize=False)),
                ('edad', models.PositiveIntegerField()),
                ('peso', models.PositiveIntegerField()),
                ('presionArterial', models.CharField(max_length=7, verbose_name=b'PA')),
                ('metUtilizado', models.CharField(blank=True, max_length=60, null=True, verbose_name=b'Metodo Utilizado')),
                ('metTiempo', models.PositiveIntegerField(blank=True, null=True, verbose_name=b'Tiempo de uso')),
                ('metLapso', models.CharField(choices=[(b'N', b'Ninguno'), (b'D', b'Dias'), (b'S', b'Semanas'), (b'M', b'Meses'), (b'A', b'Anos')], default=b'N', max_length=1, verbose_name=b' ')),
                ('histHallazgos', models.CharField(blank=True, max_length=500, null=True, verbose_name=b'Historia y hallazgos')),
                ('metContinuacion', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'S', max_length=1, verbose_name=b'Continua con el metodo')),
                ('nombreCambio', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Cambia a')),
                ('motivoCambio', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'Motivo del cambio')),
                ('diagnostico', models.CharField(blank=True, max_length=100, null=True)),
                ('tomaPap', models.CharField(choices=[(b'S', b'Si'), (b'N', b'No')], default=b'N', max_length=1, verbose_name=b'Toma PAP')),
                ('tipoConsulta', models.CharField(choices=[(b'N', b'Control Normal'), (b'M', b'Morbilidad'), (b'F', b'Falla de metodo')], default=b'N', max_length=1, verbose_name=b'Tipo de Consulta')),
                ('indicaciones', models.CharField(blank=True, max_length=100, null=True)),
                ('fechaProximaConsulta', models.DateField(blank=True, null=True, verbose_name=b'Fecha de proxima visita')),
                ('fechaIngreso', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha')),
                ('nombreResponsable', models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'Nombre Responsable')),
                ('pacienteInscrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planificacionfamiliarapp.PacienteInscripcion', verbose_name=b'Paciente')),
            ],
        ),
    ]