#Creating a habit tracking app using Pixela API
from keys import *
import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": pixela_token,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

## Pixela Account Succefully created
# response = requests.post(url=pixela_endpoint, json=user_params )
# print(response.text)

#Graph endpoint
graph_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"

graph_configuration ={ 
    "id": "graph1",
    "name": "Language Practice",
    "unit": "minutes",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": pixela_token
}

response = requests.post(url=graph_endpoint, json=graph_configuration, headers=headers)
print(response.text)