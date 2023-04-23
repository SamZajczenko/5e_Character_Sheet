from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import AnnotationBuilder
import os

# Fill the writer with the pages you want
pdf_path = os.path.join("sample.pdf")
reader = PdfReader(pdf_path)
page = reader.pages[0]
writer = PdfWriter()
writer.add_page(page)

# Create the annotation and add it
annotation = AnnotationBuilder.free_text(
    text="Hello World\nThis is the second line!",
    rect=(50, 550, 200, 650),
    font="Arial",
    bold=True, 
    italic=True,
    font_size="20pt",
    font_color="00ff00",
    border_color="0000ff",
    background_color="cdcdcd",
)
writer.add_annotation(0, annotation)

# Write the annotated file to disk
with open("annotated-pdf.pdf", "wb") as f:
    writer.add_annotation(0, annotation)
    writer.write(f)