#Creating a habit tracking app using Pixela API
from keys import *
import requests
from datetime import datetime


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

#POST Request
entry_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/graph1"

today = datetime.now()
# print(today.strftime("%Y%m%d"))
another_day = datetime(year=2023, month=12, day=22)

entry_configuration = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15"
}

# response = requests.post(url=entry_endpoint, json=entry_configuration, headers=headers)
# print(response.text)


## PUT Request (UPDATE)
put_endpoint = f"{entry_endpoint}/{today.strftime('%Y%m%d')}"

put_configuration = {
    "quantity": "20"
}

# response = requests.put(url=put_endpoint, json=put_configuration, headers=headers)
# print(response.text)

##DELETE request
delete_endpoint = put_endpoint

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)