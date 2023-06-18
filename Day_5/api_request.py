import requests

response = requests.get("https://api.github.com/search/users?q=junyichong")

print(response.json())
