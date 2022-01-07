import json
import requests

#GET API Python
#requisicao = requests.get("http://10.61.228.86:1337/api/contato-parceiros")
#print(requisicao)
#print(requisicao.json())


#POST API Python
#jsonFile = open("replayScript.json", "r+")
r = requests.post('http://10.61.228.86:1337/api/cidades-ibges', json={
    
    "data": {
                "IBGE": "1100051",
                "IBGE7": "1100023",
                "UF": "RO",
                "Municipio": "Alta Floresta D´oeste",
                "Municipio_sem_titulo": "Alta Floresta Doeste",
                "Regiao": "Região Norte",
                "Populcao": "24392",
                "Porte": "Pequeno II",
                "Capital": ""
    }
}

)
#print(f"Status Code: {r.status_code}, Response: {r.json()}")
print(f"Status Code: {r.status_code}")




#PATCH API Python
#requisicao = requests.patch('http://10.61.228.86:1337/api/contato-parceiros/9 / patch', data ={"data": {
#                "Nome_contato": "Lucas Estefano PYTHON2",
##                "Celular_contato": "11000234444444444"      
 #           }
            
            
           
#})
#print(requisicao)
#print(requisicao.content)
