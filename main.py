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

