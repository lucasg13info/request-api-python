######################
# Le o arquivo Json

import json
import requests
import xlrd
import os



json_data = None

with open('C:\path\IBGE.json') as json_file:
    json_data = json.load(json_file)

#auth=('token', 'example')

r = requests.post('http://10.61.228.86:1337/api/cidades-ibges', json=json_data)























#GET API Python
#requisicao = requests.get("http://10.61.228.86:1337/api/contato-parceiros")
#print(requisicao)
#print(requisicao.json())



#Conexão com a planilha
#PathJson = (r"C:\path\IBGE.json")
files = {'file': open('C:\path\IBGE.json', 'rb')}



#Percorrendo a planilha na coluna certa


                        




#POST API Python
r = requests.post('http://10.61.228.86:1337/api/cidades-ibges', files)
print(f"Status Code: {r.status_code}, Response: {r.json()}")






