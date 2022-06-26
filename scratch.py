import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")

with open ("/home/amirmm4d/Behrooz/Projects/Test3/todos.json",'wt') as f:
    json.dump(response.json(),f)

with open ("/home/amirmm4d/Behrooz/Projects/Test3/todos.json") as d:
    dictData = json.load(d)
    print(type(dictData))
    print (dictData[0])
for k in dictData[100]:
    print(f'{k} is {dictData[100][k]}')