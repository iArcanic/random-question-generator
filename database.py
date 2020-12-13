import os

questions_path = os.getcwd() + "/questions.csv"

def questions_folder(path):
    """Creates a folder which is names as the parameter and within it creates sub folders for each question and markscheme."""
    if os.path.exists(path) == False:
        os.makedirs(path)
        for i in range(1, 8):
            os.makedirs(os.path.join(path, "Topic " + str(i)))
            os.makedirs(os.path.join(path + "/Topic " + str(i), "Questions"))
            os.makedirs(os.path.join(path + "/Topic " + str(i), "Markscheme"))

class Questions():
    """A questions class to store each field of the 'questions.csv' file."""
    def __init__(self, id, name, topic, answer):
        self.id = id
        self.name = name
        self.topic = topic
        self.answer = answer

def load_file():
    questions_list = []

    questions_file = open(questions_path)

    for line in questions_file:
        split_line = line.split("|")
        questions_list.append(Questions(split_line[0], split_line[1], split_line[2], split_line[3]))

    return questions_list
