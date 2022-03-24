import requests

parameters = {
    "amount": 10,
    "type": "muliple"
}

response = requests.get(url="https://opentdb.com/api.php?amount=10&category=19&difficulty=easy&type=multiple",
                        params=parameters)
math_question_data = response.json()["results"]