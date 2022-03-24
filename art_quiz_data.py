import requests

parameters = {
    "amount": 10,
    "type": "multiple"
}

response = requests.get(url="https://opentdb.com/api.php?amount=10&category=25&difficulty=easy&type=multiple",
                        params=parameters)
art_question_data = response.json()["results"]