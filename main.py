from pdf2docx import Converter

# Specify the input PDF file and output DOCX file
input_pdf = 'Swiftlance Work.pdf'
output_docx = 'Swiftlance Work.docx'

# Create a Converter object
cv = Converter(input_pdf)

# Convert the PDF to DOCX
cv.convert(output_docx, start=0, end=None)  # You can specify pages using start and end

# Close the converter
cv.close()

print(f"Conversion completed! Word file saved as {output_docx}")

