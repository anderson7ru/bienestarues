#pdfReport
from reportlab.pdfgen import canvas
from reportlab.platypus import Spacer, Image, Paragraph
#from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import cm, inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_CENTER
from reportlab.lib.units import mm
import time

#(8.5*inch, 11*inch)
#PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]
PAGE_HEIGHT=11*inch; PAGE_WIDTH=8.5*inch

#Funcion para quitar repeticion de codigo
def agregaTexto(text, arrg, estilo, espacio):
	#Estilos ha utilizar
	styles=getSampleStyleSheet()
	"""Estilos predeterminados
	"Normal" "BodyText" "Italic" "Heading1" "Title" 
	"Heading2" "Heading3" "Heading4" "Heading5" "Heading6" "Bullet" "Definition" "Code"
	"""
	#Estilos personalizados
	styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
	styles.add(ParagraphStyle(name='Derecha', alignment=TA_RIGHT))
	styles.add(ParagraphStyle(name='Centro', alignment=TA_CENTER))
	
	arrg.append(Paragraph(text, styles[estilo]))
	arrg.append(Spacer(1, espacio))

#Funcion para la creacion del encabezado
def header(canvas, doc):
	ues = "UNIVERSIDAD DE EL SALVADOR"
	bienestar = "BIENESTAR UNIVERSITARIO"
	fecha_impresion = "Fecha de impresion: "+time.ctime()
	medicina = "./static/images/medicinaBN.jpg"
	minerva = "./static/images/minervaBN.gif"
	
	canvas.saveState()
	canvas.drawImage(medicina,500, 690, width=60, height=75)
	canvas.drawImage(minerva,50, 690, width=60, height=75)
	canvas.setFont('Helvetica-Bold',14)
	canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-45, ues)
	canvas.setFont('Helvetica-Bold',14)
	canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-60, bienestar)
	canvas.line(30,680,580,680)
	canvas.setFont("Helvetica", 9)
	canvas.drawCentredString(450, 2, fecha_impresion)
	canvas.restoreState()

#Funcion para la creacion del encabezado personalizado de datospersonalesapp
def headerdp(canvas, doc):
	titulo1 = "FICHA DE IDENTIFICACION"
	titulo2 = "DEL EXPEDIENTE CLINICO"
	
	canvas.saveState()
	header(canvas, doc)
	canvas.setFont('Helvetica-Bold',12)
	canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-80, titulo1)
	canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-95, titulo2)
	canvas.restoreState()

#Funcion para la creacion del encabezado personalizado de planificacionfamiliar
def headerpp(canvas, doc):
	titulo1 = "GUIA DE ATENCION EN PLANIFICACION FAMILIAR"
	titulo2 = "UTILIZADA POR EL MINSAL Y ASISTENCIA SOCIAL"
	
	canvas.saveState()
	header(canvas, doc)
	canvas.setFont('Helvetica-Bold',12)
	canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-80, titulo1)
	canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-95, titulo2)
	canvas.restoreState()
	
def headergg(canvas, doc):
	titulo1 = "HISTORIAL DE CONSULTAS"
	#titulo2 = "DEL EXPEDIENTE CLINICO"
	
	canvas.saveState()
	header(canvas, doc)
	canvas.setFont('Helvetica-Bold',12)
	canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-80, titulo1)
	#canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-95, titulo2)
	canvas.restoreState()

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
   
# referencia interna
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

# referencia externa
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

# referencia interna
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

# receta
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

# consulta general
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

class PageNumCanvas(canvas.Canvas):
	def __init__(self, *args, **kwargs):
		#Constructor
		canvas.Canvas.__init__(self, *args, **kwargs)
		self.pages = []
	def showPage(self):
		#On a page break, add information to the list
		self.pages.append(dict(self.__dict__))
		self._startPage()
	def save(self):
		#Add the page number to each page (page x of y)
		page_count = len(self.pages)
		for page in self.pages:
			self.__dict__.update(page)
			self.draw_page_number(page_count)
			canvas.Canvas.showPage(self)
		canvas.Canvas.save(self)
	def draw_page_number(self, page_count):
		#Add the page number
		page = "Pagina %s de %s" % (self._pageNumber, page_count)
		self.setFont("Helvetica", 9)
		self.drawRightString(205*mm,241*mm, page) 