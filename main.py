#Creating a habit tracking app using Pixela API
from keys import *
import requests

pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": pixela_token
}

user_params = {
    "token": pixela_token,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params )
# print(response.text)
## Pixela Account Succefully created

##Graph endpoint

# graph_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"

# graph_configuration ={ 
#     "id": "graph1",
#     "name": "Language Practice",
#     "unit": "minutes",
#     "type": "int",
#     "color": "sora"
# }

# response = requests.post(url=graph_endpoint, json=graph_configuration, headers=headers)
# print(response.text)
## Graph Successfully Created

entry_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/graph1"

entry_configuration = {
    "date": "20231222",
    "quantity": "10"
}

response = requests.post(url=entry_endpoint, json=entry_configuration, headers=headers)
print(response.text)