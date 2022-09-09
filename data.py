import requests

# additional parameters can be seen if you change the quiz settings @ opentdb.com & generate API URL
parameters = {
    "amount": 20,
    "type": "boolean",
    # "category": 11,
    # "difficulty": "medium",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
# print(data["results"])
question_data = (data["results"])
