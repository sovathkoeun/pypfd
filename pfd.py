
from fpdf import FPDF


pdf = FPDF()
pdf.add_page()

pdf.set_font('Arial', 'B', 16)

# Add text content
pdf.cell(190, 10, 'Sample PDF Document', ln=True, align='C')
pdf.set_font('Arial', '', 12)
pdf.cell(190, 10, 'This is a simple PDF created using FPDF', ln=True)

# Save the PDF
pdf.output('sample.pdf')