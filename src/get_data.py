import tabula as tab

for year in range(2000,2021):
    pdf_name = "./pdf/" + str(year) + "_final.pdf"
    output_name = "./csv/" + str(year) + "_data.csv"
    tab.convert_into(pdf_name, output_name, output_format="csv", pages='all')
    
