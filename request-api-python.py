import json
import requests

#Get API Python
#requisicao = requests.get("http://10.61.228.86:1337/api/contato-parceiros")
#print(requisicao)
#print(requisicao.json())


#Post API Python
r = requests.post('http://10.61.228.86:1337/api/contato-parceiros', json={
    "data": {
                "Nome_contato": "Lucas Estefano PYTHON",
                "Celular_contato": "1100023",
                "Email_contato": "lucas.estefano@oi.net.br"       
        }
})
print(f"Status Code: {r.status_code}, Response: {r.json()}")


