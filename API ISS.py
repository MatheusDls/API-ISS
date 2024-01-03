import requests #importação da biblioteca requests

response = requests.get(url="http://api.open-notify.org/iss-now.json") #variavel com solicitação ao link da tela 

response.raise_for_status()
data = response.json()

latitude = data["iss_position"] ["latitude"]

longitude = data["iss_position"]["longitude"]

print(latitude,longitude)

