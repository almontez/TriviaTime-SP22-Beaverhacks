import requests

parameters = {
    "amount": 10,
    "type": "multiple"
}

response = requests.get(url="https://opentdb.com/api.php?amount=10&category=10&difficulty=easy&type=multiple",
                        params=parameters)
books_question_data = response.json()["results"]