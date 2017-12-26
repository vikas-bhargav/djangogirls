from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.toreportlab import makerl
from pdfrw.buildxobj import pagexobj

input_file = "inputfile.pdf"
output_file = "my_file_with_footer.pdf"

# Get pages
reader = PdfReader(input_file)
pages = [pagexobj(p) for p in reader.pages]


# Compose new pdf
canvas = Canvas(output_file)

for page_num, page in enumerate(pages, start=1):

    # Add page
    canvas.setPageSize((page.BBox[2], page.BBox[3]))
    canvas.doForm(makerl(canvas, page))
    # Draw header
    header_text = "Jhon institute"
    x = 180
    canvas.saveState()
    canvas.setStrokeColorRGB(0, 0, 0)
    canvas.drawImage('input_logo.jpg', height=60, width=110,x=60, y=700)
    canvas.setFont('Times-Roman', 14)
    canvas.drawString(page.BBox[2] -x, 730, header_text)
    # Draw footer
    footer_text = "It’s easy to play any musical instrument: "+"\n" + " " \
                  "all you have to do is touch the right key at the right time and the instrument will play itself."
    x = 70
    canvas.setStrokeColorRGB(0, 0, 0)
    canvas.setLineWidth(0.5)
    canvas.setFont('Times-Roman', 12)
    canvas.drawString(page.BBox[1] +x, 30, footer_text)
    canvas.restoreState()

    canvas.showPage()

canvas.save()