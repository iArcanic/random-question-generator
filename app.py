from tkinter import *
import os
import random
from database import questions_folder, Questions, questions_path, load_file

class App(Tk):
    """An app class that handles the elements of the GUI, such as window dimensions and showing the relevant frames."""
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # self.geometry("%dx%d+0+0" % (self.winfo_screenwidth(), self.winfo_height()))

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menu = Menu(self)
        self.config(menu=menu)

        pages = Menu(menu, tearoff=0)

        # pages.add("command", label="Start Page", command=lambda:[controller.refresh(StartPage), controller.show_frame(StartPage)])
        # pages.add("command", label="Random Question", command=lambda:[controller.refresh(RandomQuestion), controller.show_frame(RandomQuestion)])
        # pages.add("command", label="Random Question By Topic", command=lambda:[controller.refresh(RandomQuestionByTopic), controller.show_frame(RandomQuestionByTopic)])
        # pages.add("command", label="Admin Login", command=lambda:[controller.refresh(AdminLogin), controller.show_frame(AdminLogin)])

        about = Menu(menu, tearoff=0)
        about.add("command", label="Read Me", command=os.system(os.getcwd() + "/README.md"))

        menu.add_cascade(label="Pages", menu=pages)
        menu.add_cascade(label="About", menu=about)

        self.frames = {}

        for F in (ErrorPage, StartPage, RandomQuestion, RandomQuestionByTopic, AdminLogin):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nesw")

        if os.path.exists(questions_path) == True:
            self.show_frame(StartPage)
            # questions_folder("topic_questions")
        else:
            self.show_frame(ErrorPage)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()

    def refresh(self, context):
        self.destroy()
        self.__init__()

class ErrorPage(Frame):
    """Only shows is the 'questions.csv' file doesn't exist, with an appropriate error message."""
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="No file named 'questions.txt' in the project root folder: " + "\n" + os.getcwd())
        label.pack(padx=10, pady=10)

class StartPage(Frame):
    """A start page that shows all the buttons to the relevant pages."""

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        title = Label(self, text="Start Page")
        title.pack(padx=10, pady=10)

        generate_random_question = Button(self, text="Generate a Random Question", command=lambda:[controller.refresh(RandomQuestion), controller.show_frame(RandomQuestion)])
        generate_random_question.pack(fill=X)

        generate_random_question_by_topic = Button(self, text="Generate a Random Question by Topic", command=lambda:[controller.refresh(RandomQuestionByTopic), controller.show_frame(RandomQuestionByTopic)])
        generate_random_question_by_topic.pack(fill=X)

        admin_login = Button(self, text="Admin Login", command=lambda:controller.show_frame(AdminLogin))
        admin_login.pack(fill=X)

        quit = Button(self, text="Quit", command=self.quit)
        quit.pack(fill=X)

class RandomQuestion(Frame):
    """Shows a random question from the 'questions.csv' file."""

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        title = Label(self, text="Random Question")
        title.pack(padx=10, pady=10)

        questions_list = load_file()

        random_question = Label(self, text=questions_list[random.randint(0, len(questions_list) - 1)].name)
        random_question.pack(padx=10, pady=10)

        show_answer = Button(self, text="Show Markscheme")
        show_answer.pack(fill=X)

        generate_next_random_question = Button(self, text="Generate Next Random Question", command=lambda:[controller.refresh(RandomQuestion), controller.show_frame(RandomQuestion)])
        generate_next_random_question.pack(fill=X)

        start_page = Button(self, text="Back to Start Page", command=lambda:controller.show_frame(StartPage))
        start_page.pack(fill=X)

class RandomQuestionByTopic(Frame):
    """Shows a list of all the topics."""

    def func(self, value):
        print(value)
        return value

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        topics = []

        title = Label(self, text="Random Question By Topic")
        title.pack(padx=10, pady=10)

        random_question_by_topic = Label(self, text="Select Topic")
        random_question_by_topic.pack(padx=10, pady=10)

        clicked = StringVar(self)
        clicked.set("Choose Topic")

        questions_list = load_file()

        for i in range(0, len(questions_list)):
            topics.append(questions_list[i].topic)

        topics_dropdown = OptionMenu(self, clicked, *topics, command=self.func)
        topics_dropdown.pack(padx=10, pady=10)

        generate_next_random_question = Button(self, text="Generate Random Question", command=lambda:[controller.refresh(RandomQuestionByTopic), controller.show_frame(RandomQuestionByTopic)])
        generate_next_random_question.pack(fill=X)

        show_answer = Button(self, text="Show Markscheme")
        show_answer.pack(fill=X)

        start_page = Button(self, text="Back to Start Page", command=lambda:controller.show_frame(StartPage))
        start_page.pack(fill=X)

class AdminLogin(Frame):
    """An admin page so that the administrator can update of add questions as necessary."""
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        title = Label(self, text="Admin Login")
        title.pack(padx=10, pady=10)

        start_page = Button(self, text="Back to Start Page", command=lambda:controller.show_frame(StartPage))
        start_page.pack(fill=X)

app = App()
