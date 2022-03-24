import requests

parameters = {
    "amount": 10,
    "type": "muliple"
}

response = requests.get(url="https://opentdb.com/api.php?amount=10&category=17&difficulty=easy&type=multiple",
                        params=parameters)
science_question_data = response.json()["results"]