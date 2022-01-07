import json
import requests

#GET API Python
requisicao = requests.get("http://10.61.228.86:1337/api/contato-parceiros")
print(requisicao)
print(requisicao.json())


#POST API Python
#jsonFile = open("replayScript.json", "r+")
r = requests.post('http://10.61.228.86:1337/api/contato-parceiros', json={
    "data": {
                "Nome_contato": "Lucas Estefano PYTHON",
                "Celular_contato": "1100023",
                "Email_contato": "lucas.estefano@oi.net.br"       
            }
})
print(f"Status Code: {r.status_code}, Response: {r.json()}")





#PATCH API Python
requisicao = requests.patch('http://10.61.228.86:1337/api/contato-parceiros/9 / patch', data ={"data": {
                "Nome_contato": "Lucas Estefano PYTHON2",
                "Celular_contato": "11000234444444444"      
            }
            
            
           
})
print(requisicao)
print(requisicao.content)
