# from PyPDF2 import PdfFileWriter, PdfFileReader
# import io
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter
#
# packet = io.BytesIO()
# # create a new PDF with Reportlab
# can = canvas.Canvas(packet, pagesize=letter)
# can.drawString(10, 100, "Hello world")
# can.save()
#
# #move to the beginning of the StringIO buffer
# packet.seek(0)
# new_pdf = PdfFileReader(packet)
# # read your existing PDF
# existing_pdf = PdfFileReader(open("inputfile.pdf", "rb"))
# output = PdfFileWriter()
# # add the "watermark" (which is the new pdf) on the existing page
# page = existing_pdf.getPage(0)
# print(page)
# page.mergePage(new_pdf.getPage(0))
# output.addPage(page)
# # finally, write "output" to a real file
# outputStream = open("destination.pdf", "wb")
# output.write(outputStream)
# outputStream.close()


# from reportlab.lib.pagesizes import letter
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph
#
# styles = getSampleStyleSheet()
# styleN = styles['Normal']
# styleH = styles['Heading1']
#
# def footer(canvas, doc):
#     canvas.saveState()
#     P = Paragraph("This is a multi-line footer.  It goes on every page.  " * 5,
#                   styleN)
#     w, h = P.wrap(doc.width, doc.bottomMargin)
#     P.drawOn(canvas, doc.leftMargin, h)
#     canvas.restoreState()
#
# doc = BaseDocTemplate('test.pdf', pagesize=letter)
# frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height,
#               id='normal')
# template = PageTemplate(id='test', frames=frame, onPage=footer)
# doc.addPageTemplates([template])
#
# text = []
# for i in range(111):
#     text.append(Paragraph("This is line %d." % i,
#                           styleN))
# doc.build(text)

from reportlab.lib.pagesizes import letter, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Image
from functools import partial
from reportlab.lib.units import inch

styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']

def header(canvas, doc, content):
    canvas.saveState()
    filepath = 'input_logo.jpg'
    # i = Image(filepath, 3*inch, 3*inch)
    # canvas.drawImage('input_logo.jpg', 1*inch, 1*inch)
    # image = Image(filepath, width=128, height=82)
    # image.hAlign = 'RIGHT'
    # im = Image.open(filepath)
    # canvas.drawInlineImage(im, 256, 720, width=100, height=60)

    w, h = content.wrap(doc.width, doc.topMargin)
    content.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h)
    canvas.restoreState()

# ----------------------------- #
# def footer(canvas, doc):
#     filepath = 'input_logo.jpg'
#     canvas.saveState()
#     i = Image(filepath, 3*inch, 3*inch)
#     canvas.drawImage('input_logo.jpg', inch, 5 - 2 * inch)
#     P = Paragraph("<img src='input_logo.jpg' height='10'>This is a multi-line footer.  It goes on every page.  " * 5,
#                   styleN)
#     w, h = P.wrap(doc.width, doc.bottomMargin)
#     P.drawOn(canvas, doc.leftMargin, h)
#     canvas.restoreState()

# ---------- main ----------------#
def header_footer(canvas, doc):
    print("hhhhhh")
    # Save the state of our canvas so we can draw on it
    canvas.saveState()
    styles = getSampleStyleSheet()

    # Header
    header = Paragraph('This is a multi-line header.  It goes on every page.   ' * 5, styles['Normal'])
    w, h = header.wrap(doc.width, doc.topMargin)
    header.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h)

    # Footer
    footer = Paragraph('This is a multi-line footer.  It goes on every page.   ' * 5, styles['Normal'])
    w, h = footer.wrap(doc.width, doc.bottomMargin)
    footer.drawOn(canvas, doc.leftMargin, h)

    # Release the canvas
    canvas.restoreState()

doc = BaseDocTemplate('test.pdf', pagesize=letter)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height-2*cm, id='normal')
header_content = Paragraph("This is a multi-line header.  It goes on every page.", styleN)
template = PageTemplate(id='test', frames=frame, onPage=partial(header, content=header_content))
doc.addPageTemplates([template])

text = []
for i in range(111):
    text.append(Paragraph("This is line %d." % i, styleN))
doc.build(text)






