import PyPDF2

temp =PyPDF2.PdfReader(open("marged.pdf","rb"))
watermark = PyPDF2.PdfReader(open("wtr.pdf","rb"))
output = PyPDF2.PdfWriter()

for i in range(temp._get_num_pages()):
    page = temp._get_page(i)
    page.merge_page(watermark._get_page(0))
    output.add_page(page)

with open("wtr_output.pdf","wb") as file :
    output.write(file)