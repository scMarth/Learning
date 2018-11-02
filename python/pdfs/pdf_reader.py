import PyPDF2

# importing required modules 
import PyPDF2 
  
# creating a pdf file object 
# pdf_file_obj = open('./RoadClosureInfo.pdf', 'rb')
pdf_file_obj = open('./conezone_report.pdf', 'rb') 
  
# creating a pdf reader object 
pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj) 
  
# get number of pages in pdf file 
num_pages = pdf_reader.numPages

# extracting text from page 
# print(pageObj.extractText())
with open("extracted.txt", "w") as file:
    for i in range(0, num_pages):
        # creating a page object
        page_obj = pdf_reader.getPage(i)
        file.write(page_obj.extractText())
        file.write("\n\n\n")
  
# closing the pdf file object 
pdf_file_obj.close() 