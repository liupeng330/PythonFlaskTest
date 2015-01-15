import requests

url = "http://localhost:5000/todo/api/v1.0/tasks" 
response = requests.get(url)
print response.content