from tkinter import *
from PIL import ImageTk, Image
from playsound import playsound
from books_quiz_data import books_question_data
from question_model import Question, QuizBrain
from random import shuffle
import html


class QuestionUI:
    """Docstring"""

    def __init__(self, quiz_brain):
        """docstring"""
        self._quiz = quiz_brain

        # create quiz base/window
        self._window = Tk()
        self._window.geometry("900x600")

        # create canvas background/display
        self._CANVAS_WIDTH = 900
        self._CANVAS_HEIGHT = 600

        self._canvas = Canvas(self._window, width=self._CANVAS_WIDTH, height=self._CANVAS_HEIGHT)
        self._canvas.pack()

        # add image to canvas
        bg_img = ImageTk.PhotoImage(Image.open('Assets/quiz_question_background_900x600.jpg'))
        self._canvas.create_image(0, 0, image=bg_img, anchor='nw')
        self._canvas.create_rectangle(75, 75, 825, 525, fill="White")

        # add frame to canvas to hold widgets
        self._mframe = Frame(self._canvas, height=425, width=725, bg="white")
        self._mframe.place(x=450, y=300, anchor="center")

        # display initial trivia question and answers
        self.display_question()
        self.display_answer_choices()

        self._window.mainloop()

    def clear_frame(self):
        """docstring"""
        for widgets in self._mframe.winfo_children():
            widgets.destroy()
        return

    def display_question(self):
        """docstring"""
        q_text = self._quiz.get_question()
        question_label = Label(self._mframe, text=q_text, font=('Ariel', 18, 'bold'),
                               bg="white", bd=0, width=45, wrap=680)
        question_label.place(x=15, y=30, anchor="nw")
        return

    def set_player_answ(self, player_choice):
        """Docstring"""
        # # play sound
        # playsound("Assets/zapsplat_click1.mp3")

        # store player answer in variable
        player_choice = player_choice

        is_correct = self._quiz.check_answer(player_choice)
        self.show_answers(is_correct)

    def display_answer_choices(self):
        """Docstring"""

        answer_choices = self._quiz.get_answer_choices()
        y_pos = 150

        for option in answer_choices:
            choice = Button(self._mframe, text=option, width=50, font=("Ariel", 14),
                            relief="flat", bd=0, activebackground="yellow", bg="White",
                            command=lambda selection=option: self.set_player_answ(selection))
            choice.place(x=350, y=y_pos, anchor="center")
            y_pos += 75

    def show_answers(self, answer_key):
        """Docstring"""
        bool_val, answer = answer_key
        x_pos = self._mframe.winfo_width()//2
        y_pos = self._mframe.winfo_height()//2

        color = "green"
        fb_text = "Good Job! Keep it up!"
        if bool_val == 0:
            color = "red"
            fb_text = f"Oops! The right answer is {answer}."

        self.clear_frame()
        feedback = Label(self._mframe, width=60, height=18, text=fb_text, bg="white",
                         fg=color, font=("Ariel", 16, "italic"))
        feedback.place(x=x_pos, y=y_pos - 50, anchor="center")
        self.next_button()

    def next_question(self):
        """Docstring"""

        # # play click sound
        # playsound("Assets/zapsplat_click1.mp3")
        # self.clear_frame()

        if self._quiz.has_more_questions():
            self.display_question()
            self.display_answer_choices()
        else:
            self.display_results()

    def next_button(self):
        """Docstring"""
        x_pos = self._mframe.winfo_width()//2

        nxt_btn = Button(self._mframe, text="Next", width=10, relief='flat', bg='white', bd=0,
                         font=("Ariel", 14, 'bold'), command=self.next_question)
        nxt_btn.place(x=x_pos, y=250, anchor="center")

    def display_results(self):
        """Docstring"""

        score = f"Your Score: {self._quiz.get_score()}"
        x_pos = self._mframe.winfo_width() // 2
        y_pos = self._mframe.winfo_height() // 2

        player_name = "Angela Montez"   # Sample Function Call: self._quiz.get_player_name()
        whoop = "Congratulations! " + player_name

        whoop_label = Label(self._mframe, text=whoop, font=('Ariel', 20, 'bold', 'italic'),
                            fg="#FFD700", bg="black", bd=0, width=45, wrap=680)
        whoop_label.place(x=x_pos, y=y_pos-175, anchor="center")

        score_label = Label(self._mframe, text=score, font=('Ariel', 20, 'bold', 'italic'),
                            bg="#FFD700", bd=0, width=45, wrap=680)
        score_label.place(x=x_pos, y=y_pos-125, anchor="center")

        trophy_img = Image.open("Assets/trophy.jpg")
        trophy_resize = trophy_img.resize((300, 300))
        trophy_final = ImageTk.PhotoImage(trophy_resize)

        trophy_display = Label(self._mframe, image=trophy_final, bd=0)
        trophy_display.place(x=x_pos, y=y_pos + 50, anchor="center")

        self._window.mainloop()


question_bank = []
for question in books_question_data:
    choices = []
    question_text = html.unescape(question["question"])
    correct_answer = html.unescape(question["correct_answer"])
    incorrect_answers = question["incorrect_answers"]

    for ans in incorrect_answers:
        choices.append(html.unescape(ans))
    choices.append(correct_answer)
    shuffle(choices)

    q_question = Question(question_text, correct_answer, choices)
    question_bank.append(q_question)

qb = QuizBrain(question_bank)
q = QuestionUI(qb)
