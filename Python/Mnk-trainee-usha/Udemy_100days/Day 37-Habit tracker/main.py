#Habit tracker using pixela api,posting our data in pixela to be tracked .
from http.client import responses
from datetime import datetime
import requests
#creating user
USERNAME="username"
TOKEN="password"
pixela_endpoint="https://pixe.la/v1/users"
GRAPH_ID="graph01"
user_parameters={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response=requests.post(url=pixela_endpoint,json=user_parameters)
# print(response.text)

#creating a graph
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_body={
    "id":GRAPH_ID,
    "name":"Walking",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}

headers={
    "X-USER-TOKEN":TOKEN
}

# response=requests.post(url=graph_endpoint,json=graph_body,headers=headers)
# print(response.text)

#post data to a graph
adding_data_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today=datetime.now()

adding_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many km did you walk today?")
}
response=requests.post(url=adding_data_endpoint,json=adding_data,headers=headers)
print(response.text)

#PUT-changing previous data using put
update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_data={
    "quantity":"9.5"
}
# response=requests.put(url=update_endpoint,json=new_data,headers=headers)
# print(response.text)

#DELETE-to delete a data
delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20250106"
# responses=requests.delete(url=delete_endpoint,headers=headers)
# print(responses.text)