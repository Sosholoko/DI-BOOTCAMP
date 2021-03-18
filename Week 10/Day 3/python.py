import requests
import json

url = "https://newsapi.org/v2/everything"
token = "eb83a5a421e045b28d9872755d7341a6"

r = requests.get(url, params = {"apiKey": token,"q":"israel", "pageSize": "5", "from": "2021"})
string_text = r.text
print(r.text)
print(type(r.text))


dict_text = json.loads(string_text)

for article in dict_text["articles"][:5]:
    print(article["title"])
print(type(dict_text))
