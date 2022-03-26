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

        self._fframe = Frame(self._window, width=900, height=600)
        self._fframe.pack(fill=Y, anchor="center")

        self.first_screen()
        self._window.mainloop()

    def question_frame(self):
        """docstring"""
        # add image to canvas
        self.clear_frame()

        x_pos = self._fframe.winfo_width() // 2
        y_pos = self._fframe.winfo_height() // 2

        question_img = Image.open("Assets/quiz_question_background_900x600.jpg")
        question_resize = question_img.resize((900, 600))
        question_final = ImageTk.PhotoImage(question_resize)

        question_label = Label(self._fframe, image=question_final)
        question_label.place(x=x_pos, y=y_pos, anchor="center")

        white_box = Label(question_label, width=100, height=33, bg="white")
        white_box.place(x=x_pos, y=y_pos, anchor="center")

        self.display_question()

    def clear_frame(self):
        """docstring"""
        for widgets in self._fframe.winfo_children():
            widgets.destroy()
        return

    def display_question(self):
        """docstring"""
        q_text = self._quiz.get_question()
        question_label = Label(self._fframe, text=q_text, font=('Ariel', 18, 'bold'),
                               bg="white", bd=0, width=45, wrap=650)
        question_label.place(x=110, y=120, anchor="nw")

        self.display_answer_choices()

    def set_player_answ(self, player_choice):
        """Docstring"""
        playsound("Assets/zapsplat_click1.mp3")

        # store player answer in variable
        player_choice = player_choice

        is_correct = self._quiz.check_answer(player_choice)
        self.show_answers(is_correct)

    def display_answer_choices(self):
        """Docstring"""

        answer_choices = self._quiz.get_answer_choices()
        y_pos = 250

        for option in answer_choices:
            choice = Button(self._fframe, text=option, width=50, font=("Ariel", 14),
                            relief="flat", bd=0, activebackground="yellow", bg="White",
                            command=lambda selection=option: self.set_player_answ(selection))
            choice.place(x=450, y=y_pos, anchor="center")
            y_pos += 75

        self._window.mainloop()

    def show_answers(self, answer_key):
        """Docstring"""
        bool_val, answer = answer_key

        color = "green"
        fb_text = "Good Job! Keep it up!"
        if bool_val == 0:
            color = "red"
            fb_text = f"Oops! The right answer is {answer}."

        self.clear_frame()
        x_pos = self._fframe.winfo_width() // 2
        y_pos = self._fframe.winfo_height() // 2

        question_img = Image.open("Assets/quiz_question_background_900x600.jpg")
        question_resize = question_img.resize((900, 600))
        question_final = ImageTk.PhotoImage(question_resize)

        question_label = Label(self._fframe, image=question_final)
        question_label.place(x=x_pos, y=y_pos, anchor="center")

        white_box = Label(question_label, width=100, height=33, bg="white")
        white_box.place(x=x_pos, y=y_pos, anchor="center")

        feedback = Label(self._fframe, width=40, height=5, text=fb_text, bg="white",
                         fg=color, font=("Ariel", 20, "italic"), wrap=500)
        feedback.place(x=x_pos, y=y_pos - 50, anchor="center")
        self.next_button()

    def next_question(self):
        """Docstring"""

        # play click sound
        playsound("Assets/zapsplat_click1.mp3")
        self.clear_frame()

        if self._quiz.has_more_questions():
            self.question_frame()
        else:
            self.display_results()

    def next_button(self):
        """Docstring"""
        x_pos = self._fframe.winfo_width() // 2

        nxt_btn = Button(self._fframe, text="Next", width=10, relief='flat', bg='white', bd=0,
                         font=("Ariel", 16, 'bold'), command=self.next_question)
        nxt_btn.place(x=x_pos, y=325, anchor="center")
        self._window.mainloop()

    def display_results(self):
        """Docstring"""
        score = f"Your Score: {self._quiz.get_score()}"
        x_pos = self._fframe.winfo_width() // 2
        y_pos = self._fframe.winfo_height() // 2

        player_name = "Angela Montez"  # Sample Function Call: self._quiz.get_player_name()
        whoop = "Congratulations! " + player_name

        question_img = Image.open("Assets/quiz_question_background_900x600.jpg")
        question_resize = question_img.resize((900, 600))
        question_final = ImageTk.PhotoImage(question_resize)

        question_label = Label(self._fframe, image=question_final)
        question_label.place(x=x_pos, y=y_pos, anchor="center")

        white_box = Label(question_label, width=113, height=33, bg="white")
        white_box.place(x=x_pos, y=y_pos, anchor="center")

        whoop_label = Label(self._fframe, text=whoop, font=('Ariel', 20, 'bold', 'italic'),
                            fg="#FFD700", bg="black", bd=0, width=45, wrap=680)
        whoop_label.place(x=x_pos, y=y_pos - 175, anchor="center")

        score_label = Label(self._fframe, text=score, font=('Ariel', 20, 'bold', 'italic'),
                            bg="#FFD700", bd=0, width=45, wrap=680)
        score_label.place(x=x_pos, y=y_pos - 125, anchor="center")

        trophy_img = Image.open("Assets/trophy.jpg")
        trophy_resize = trophy_img.resize((300, 300))
        trophy_final = ImageTk.PhotoImage(trophy_resize)

        trophy_display = Label(self._fframe, image=trophy_final, bd=0)
        trophy_display.place(x=x_pos, y=y_pos + 50, anchor="center")

        self._window.mainloop()

    def first_screen(self):
        """docstring"""
        x_pos = self._fframe.winfo_width() // 2
        y_pos = self._fframe.winfo_height() // 2

        homepg_img = Image.open("Assets/homepage_image.jpg")
        homepg_resize = homepg_img.resize((900, 600))
        homepg_final = ImageTk.PhotoImage(homepg_resize)

        homepg_label = Label(self._fframe, image=homepg_final)
        homepg_label.place(x=x_pos, y=y_pos)

        blue_bckgrd = Label(homepg_label, width=113, height=33, bg="#AFEEEE")
        blue_bckgrd.place(x=x_pos + 50, y=y_pos + 50, anchor="nw")

        books_img = Image.open("Assets/pink_bubble_books.png")
        books_resize = books_img.resize((150, 150))
        books_final = ImageTk.PhotoImage(books_resize)

        books_btn = Button(self._fframe, image=books_final, bg="#AFEEEE", relief="flat",
                           activebackground="#AFEEEE", command=self.question_frame)
        books_btn.place(x=75, y=75)

        math_img = Image.open("Assets/red_bubble_math.png")
        math_resize = math_img.resize((160, 160))
        math_final = ImageTk.PhotoImage(math_resize)

        math_btn = Button(self._fframe, image=math_final, bg="#AFEEEE", relief="flat",
                          activebackground="#AFEEEE")
        math_btn.place(x=70, y=365)

        art_img = Image.open("Assets/green_bubble_art.png")
        art_resize = art_img.resize((140, 140))
        art_final = ImageTk.PhotoImage(art_resize)

        art_btn = Button(self._fframe, image=art_final, bg="#AFEEEE", relief="flat",
                         activebackground="#AFEEEE")
        art_btn.place(x=110, y=235)

        science_img = Image.open("Assets/teal_bubble_science.png")
        science_resize = science_img.resize((200, 200))
        science_final = ImageTk.PhotoImage(science_resize)

        science_btn = Button(self._fframe, image=science_final, bg="#AFEEEE", relief="flat",
                             activebackground="#AFEEEE")
        science_btn.place(x=250, y=100)

        history_img = Image.open("Assets/yellow_bubble_history.png")
        history_resize = history_img.resize((200, 200))
        history_final = ImageTk.PhotoImage(history_resize)

        history_btn = Button(self._fframe, image=history_final, bg="#AFEEEE", relief="flat",
                             activebackground="#AFEEEE")
        history_btn.place(x=250, y=325)

        title_text = "It's Trivia Time!"
        title_label = Label(self._fframe, text=title_text, font=("Snap ITC", 45), bg="#AFEEEE", wrap=350)
        title_label.place(x=525, y=100)

        sub_text = "Click on a category to test your knowledge! Score at least a 7 out of 10 to earn a badge." \
                   "\n\nKeep playing to earn badges!"
        sub_text_label = Label(self._fframe, text=sub_text, font=("Ariel", 12), bg="#AFEEEE", wrap=340)
        sub_text_label.place(x=490, y=350)

        name_label = Label(self._fframe, text="Enter Player Name", font=("Ariel", 12), bg="#AFEEEE")
        name_label.place(x=575, y=450)
        player_name = Entry(self._fframe, relief="flat", justify="center", font=("Ariel", 16))
        player_name.place(x=525, y=475)

        self._window.mainloop()
        return


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
