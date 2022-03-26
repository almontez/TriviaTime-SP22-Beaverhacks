from books_quiz_data import books_question_data
from random import shuffle
import html

class Question:
    """Docstring"""

    def __init__(self, question, correct_answer, choices):
        """Docstring"""
        self._question = question
        self._correct_answer = correct_answer
        self._choices = choices

    def get_question(self):
        "Docstring"
        return self._question

    def get_correct_answer(self):
        """docstring"""
        return self._correct_answer

    def get_choices(self):
        """Docstring"""
        return self._choices

class QuizBrain:
    """docstring"""

    def __init__(self, questions):
        """Docstring"""
        self._question_no = 0
        self._score = 0
        self._questions = questions
        self._current_question = None

    def has_more_questions(self):
        """docstring"""
        return self._question_no < len(self._questions)

    def get_question(self):
        """Docstring"""
        self._current_question = self._questions[self._question_no]
        self._question_no += 1

        q_text = self._current_question.get_question()

        return f"Q{self._question_no}: {q_text}"

    def get_answer_choices(self):
        """Docstring"""
        answer_choices = self._current_question.get_choices()
        return answer_choices

    def check_answer(self, player_selection):
        correct_answer = self._current_question.get_correct_answer()

        if player_selection.lower() == correct_answer.lower():
            self._score += 1
            return (True, correct_answer)
        else:
            return (False, correct_answer)

    def get_score(self):
        """Docstring"""
        return self._score
