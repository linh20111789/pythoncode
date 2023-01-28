from PyPDF2 import PdfFileWriter, PdfFileReader
pages_to_keep = [0, 1] # page numbering starts from 0
infile = PdfFileReader('23.1_U5_ Review (1).pdf', 'rb')
output = PdfFileWriter()

for i in pages_to_keep:
    p = infile.getPage(i)
    output.addPage(p)

with open('newfile.pdf', 'wb') as f:
    output.write(f)