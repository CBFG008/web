import PyPDF2

marger = PyPDF2.PdfMerger()
marger.append("dummy.pdf")
marger.append("twopage.pdf")
marger.append("wtr.pdf")

marger.write("marged.pdf")
marger.close()