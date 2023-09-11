import requests

url = "https://robomatic-ai.p.rapidapi.com/api"

payload = {
	"in": "What's 2 plus 9?",
	"op": "in",
	"cbot": "1",
	"SessionID": "RapidAPI1",
	"cbid": "1",
	"key": "RHMN5hnQ4wTYZBGCF3dfxzypt68rVP",
	"ChatSource": "RapidAPI",
	"duration": "1"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "5256b88b43mshc6340f9fc2764e3p1a424ajsn7f04a28ee0ae",
	"X-RapidAPI-Host": "robomatic-ai.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())