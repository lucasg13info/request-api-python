###########################################################################################################
#                                                                                                         #
#                                       ROBÔ DE CARGA NA API 2022                                          #
#                                                                                                         #
###########################################################################################################
#                                                                                                         #
#       - 1 - Realizado a conexão e leitura de uma aba e cola específico de uma planilha formato xlsx     #
#       - 2 - Realizado um for para percorrer toda a coluna a ser lida                                    #
#       - 3 - Convertido os valores recebidos para um "dicionário" (array)                                #
#       - 3 - Realizado o POST na API passando todos os valores percorridos da planilha                   #
#                                                                                                         #
#                                                                                                         #
#                                                       Implementado dia: 12/01/2022  - Lucas Estefano    #
###########################################################################################################
#                                                                                                         #     
#                                                                                                         #
#                                   O JSON QUE ESTIVER NA PLANILHA                                        #
#                                    DEVE FICAR NO FORMATO ABAIXO                                         #
#                                                 |                                                       #
#                                                 |                                                       #
#                                                 ↓                                                       #
###########################################################################################################
#                                                                                                         #
#           {"data":{"IBGE": "110038","IBGE7": "1100288","UF":"RO","Municipio": "Rolim de Moura",         #
#           "Municipio_sem_titulo": "Rolim de Moura","Regiao": "Região Norte","Populcao": "50648",        #
#           "Porte": "Médio","Capital": ""}}                                                              #
#                                                                                                         #
###########################################################################################################


# -*- coding: utf-8 -*-
import json
import requests
import xlrd
import ast
import time

#Timer de execução do Robô
timerCod = time.time()

#Conexão com a planilha
workbook = xlrd.open_workbook(r"C:\path\IBGE13.xls")
#Selecionando a aba da planilha
sheet = workbook.sheet_by_name("Url")




#Percorrendo a planilha na coluna certa
for i1 in range(1, 11):
    jsonFormatadoParaInsert = str(sheet.cell_value(rowx=i1, colx=2))

    #Convertendo para dicionario = array caso algum dado esteja incorreto, entra no except:
    try:
        convertListDicionario = ast.literal_eval(jsonFormatadoParaInsert)
    except:
        print('DADO', i1, 'COM VALORES INCORRETOS NA PLANILHA!')
    #print(type(convertListDicionario))
    #print(convertListDicionario)


    #POST API Python
    url = 'http://10.61.228.86:1337/api/cidades-ibges'
    r = requests.post(url, json= convertListDicionario)
    print('Dados inseridos: ', i1, '  Status code:', r.status_code)
    #print(f"Status Code: {r.status_code}, Response: {r.json()}")


print('*--------------------------------------------------------------------*')
print('Foram inseridos no total:', i1 ,'dados na API.')
print('*---------------------------------------------------------------------*')


tempoExec = time.time() -timerCod
print('O tempo de execução do robô foi de: {} Segundos.'.format(tempoExec))
print('*---------------------------------------------------------------------*')

 
    


    


##############################################################################

#######GET API Python
#requisicao = requests.get("http://10.61.228.86:1337/api/contato-parceiros")
#print(requisicao)
#print(requisicao.json())


######Convertendo para lista e tirando as aspas
#convertList = (list(jsonFormatadoParaInsert))
#convertList2 = (''.join(convertList).replace("'", ""))
#print(type(convertList2))
#convertList2 = (convertList.join(convertList).replace("'", ""))
#print(convertList2)

#######Converte para formato json
######jsonFormatadoParaInsert2 = json.dumps(jsonFormatadoParaInsert).replace("'", '"')
#####print(jsonFormatadoParaInsert2)