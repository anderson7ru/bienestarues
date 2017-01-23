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

def headergg(canvas, doc):
	titulo1 = "HISTORIAL DE CONSULTAS"
	#titulo2 = "DEL EXPEDIENTE CLINICO"
	
	canvas.saveState()
	header(canvas, doc)
	canvas.setFont('Helvetica-Bold',12)
	canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-80, titulo1)
	#canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-95, titulo2)
	canvas.restoreState()

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