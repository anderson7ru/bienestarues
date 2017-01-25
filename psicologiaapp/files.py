#pdfReport
from reportlab.pdfgen import canvas
from reportlab.platypus import Spacer, Image, Paragraph, PageBreak
#from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import cm, inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_CENTER
from reportlab.lib.units import mm
import time

from bienestarhome.files import header

PAGE_HEIGHT=11*inch; PAGE_WIDTH=8.5*inch 
#Anchura : 612 px => 8.5*inch.
#Altura : 792 px => 11*inch

def headerPsico(canvas,doc):
    subtitle1 = "CENTRO DE SALUD UNIVERSITARIO"
    subtitle2 = "CLINICA DE PSICOLOGIA"
    psico = "./static/images/psi-simbolo.jpg"
	
    canvas.saveState()
    canvas.drawImage(psico,460,685, width=30,height=30)
    canvas.restoreState()
    
    canvas.saveState()
    header(canvas,doc)
    canvas.setFont('Helvetica-Bold',12)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-75, subtitle1)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-105, subtitle2)
    canvas.restoreState()
    
def headerPsico2(canvas,doc):
    psico = "./static/images/psi-simbolo.jpg"
    fecha_impresion = "Fecha de impresion: "+time.ctime()
    canvas.saveState()
    canvas.drawImage(psico,500, 700, width=40, height=65)
    canvas.line(30,680,580,680)
    canvas.setFont("Helvetica", 9)
    canvas.drawCentredString(450, 2, fecha_impresion)
    canvas.restoreState()
    
def headerProcesos(canvas,doc):
    subtitle1 = "PROCESO TERAPEUTICO"
    canvas.saveState()
    headerPsico2(canvas,doc)
    canvas.setFont('Helvetica-Bold',12)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-75, subtitle1)
    canvas.restoreState()
    
def headerRegistro(canvas,doc):
    subtitle1 ="REGISTRO DE AVANCES TERAPEUTICOS"
    subtitle2 ="COMENTARIOS"
    canvas.saveState()
    headerPsico2(canvas,doc)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-75, subtitle1)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-105, subtitle2)
    canvas.restoreState()
    
    
def writeLine(text, arrg, estilo, espacio):
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY, leading=30))
    #styles.add(ParagraphStyle(name='Derecha', alignment=TA_RIGHT, leading=30))
    #styles.add(ParagraphStyle(name='Centro', alignment=TA_CENTER, leading=30))
    styles.add(ParagraphStyle(name='Justify2', alignment=TA_JUSTIFY, leading=20))
	
    arrg.append(Paragraph(text, styles[estilo]))
    arrg.append(Spacer(1, espacio))
    
def saltoPagina(arrg):
    arrg.append(PageBreak())

#
#
#


#
## referencia interna
#
def headerReInterna(canvas, doc):
    subtitle1 = "CENTRO DE SALUD UNIVERSITARIO"
    subtitle2 = "CONSULTA GENERAL"
    subtitle3 = "REFERENCIA INTERNA"
    
    canvas.saveState()
    header(canvas, doc)
    canvas.setFont('Helvetica-Bold', 12)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-75, subtitle1)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-90, subtitle2)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-105, subtitle3)
    canvas.restoreState()
#
## referencia externa
#
def headerReExterna(canvas, doc):
    subtitle1 = "CENTRO DE SALUD UNIVERSITARIO"
    subtitle2 = "CONSULTA GENERAL"
    subtitle3 = "REFERENCIA EXTERNA"
    
    canvas.saveState()
    header(canvas, doc)
    canvas.setFont('Helvetica-Bold', 12)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-75, subtitle1)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-90, subtitle2)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-105, subtitle3)
    canvas.restoreState()
#
## referencia interna
#
def headerOrdenLab(canvas, doc):
    subtitle1 = "CENTRO DE SALUD UNIVERSITARIO"
    subtitle2 = "CONSULTA GENERAL"
    subtitle3 = "ORDEN DE LABORATORIO"
    
    canvas.saveState()
    header(canvas, doc)
    canvas.setFont('Helvetica-Bold', 12)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-75, subtitle1)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-90, subtitle2)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-105, subtitle3)
    canvas.restoreState()
#
## receta
#
def headerReceta(canvas, doc):
    subtitle1 = "CENTRO DE SALUD UNIVERSITARIO"
    subtitle2 = "CONSULTA GENERAL"
    subtitle3 = "RECETA MEDICA"
    
    canvas.saveState()
    header(canvas, doc)
    canvas.setFont('Helvetica-Bold', 12)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-75, subtitle1)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-90, subtitle2)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-105, subtitle3)
    canvas.restoreState()
#
## consulta general
#
def headerConsultaGeneral(canvas, doc):
    subtitle1 = "CENTRO DE SALUD UNIVERSITARIO"
    subtitle2 = "CONSULTA GENERAL"
    subtitle3 = "CONSULTA GENERAL"
    
    canvas.saveState()
    header(canvas, doc)
    canvas.setFont('Helvetica-Bold', 12)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-75, subtitle1)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-90, subtitle2)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-105, subtitle3)
    canvas.restoreState()
#