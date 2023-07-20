import pdfplumber
import tabula
import pandas as pd
# with pdfplumber.open('cds_2014-15.pdf') as pdf:
#     count=0
#     for page in pdf.pages:
#         count+=1
#         text = page.extract_text()
#         if count==3:

#             print(text)
#             break
# Specify the path to the PDF file
pdf_file_path = "cds_2014-15.pdf"
pdf_file_path2 = "amherst.pdf"
check1 = False
check2=False
# Read tables from the PDF into a list of DataFrames
# You may need to experiment with the `pages` parameter to specify the page numbers
tables1 = tabula.read_pdf(pdf_file_path, pages='all', multiple_tables=True)
new_tables = [] #take only A0 to A5 as test sample
for i in range(6):
    new_tables.append(tables1[i])
tables2 = tabula.read_pdf(pdf_file_path2, pages = 'all', multiple_tables=True)
excel_file = "amherst.xlsx"

#combinging the 2 tables
#...
#...
#...


writer = pd.ExcelWriter(excel_file, engine="xlsxwriter")
for i, table_df in enumerate(tables1, start=1):
    sheet_name = f"Table_{i}"
    table_df.to_excel(writer, sheet_name=sheet_name, index=False)
writer.save()


# hi
