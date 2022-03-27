from books_quiz_data import books_question_data
from random import shuffle
import html

class Question:
    """Question class with methods for get question methods and choices and correct answers"""

    def __init__(self, question, correct_answer, choices):
        """Initializing 3 variables: question, correct_answer, and choices"""
        self._question = question
        self._correct_answer = correct_answer
        self._choices = choices

    def get_question(self):
        "gets the question from the question api"
        return self._question

    def get_correct_answer(self):
        """gets the correct answers from question api"""
        return self._correct_answer

    def get_choices(self):
        """get the choices from question api"""
        return self._choices

class QuizBrain:
    """The background works of the quiz"""

    def __init__(self, questions):
        """Initializing 4 variables: question no, score, questions, and current question"""
        self._question_no = 0
        self._score = 0
        self._questions = questions
        self._current_question = None

    def has_more_questions(self):
        """Sees if question number is smaller than the number of questions"""
        return self._question_no < len(self._questions)

    def get_question(self):
        """Gets current question, increases question answered by 1"""
        self._current_question = self._questions[self._question_no]
        self._question_no += 1

        q_text = self._current_question.get_question()

        return f"Q{self._question_no}: {q_text}"

    def get_answer_choices(self):
        """Gets answer choices"""
        answer_choices = self._current_question.get_choices()
        return answer_choices

    def check_answer(self, player_selection):
        """Check whether the answer is correct, if true, add one to score, if not, displays correct answers"""
        correct_answer = self._current_question.get_correct_answer()

        if player_selection.lower() == correct_answer.lower():
            self._score += 1
            return (True, correct_answer)
        else:
            return (False, correct_answer)

    def get_score(self):
        """Gets the score"""
        return self._score

    def store_user_name(self, user_name):
        """docstring"""
        self._user_name = user_name
        return

    def get_user_name(self):
        """docstring"""
        return self._user_name