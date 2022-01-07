import json
import requests
import xlrd
import os

#GET API Python
#requisicao = requests.get("http://10.61.228.86:1337/api/contato-parceiros")
#print(requisicao)
#print(requisicao.json())

#Conexão com a planilha
workbook = xlrd.open_workbook(r"C:\path\IBGE.xls")
sheet = workbook.sheet_by_name("Url")
#getting the first sheet
sheet_1 = workbook.sheet_by_index(0)

#Lista as colunas
for sh in workbook.sheets():
    print(sh.name)

sh = workbook.sheet_by_index(0)

#Percorrendo a planilha na coluna certa

for i1 in range(1, 5572):
    jsonFormatadoParaInsert = str(sheet.cell_value(rowx=i1, colx=2)).replace('.', ',')  
    #print(jsonFormatadoParaInsert)
                        




    #POST API Python
    r = requests.post('http://10.61.228.86:1337/api/cidades-ibges', json= jsonFormatadoParaInsert)
    print(f"Status Code: {r.status_code}, Response: {r.json()}")






#"data": {
#                "IBGE": "",
#                "IBGE7": "1100023",
#                "Email_contato": "lucas.estefano@oi.net.br",
#                "UF" : "SP",       
#                "Municipio" : "SP",    
#                "Municipio_sem_titulo" : "Sao Paulo",    
#                "Regiao" : "São Paulo",    
#                "Populcao" : "700000000",    
#                "Porte" : "Grande",    
#                "Capital" : "São paulo"
#            }