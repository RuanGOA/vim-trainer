from random import randint

class level:
    def __init__(self, id_level, lessons):
        self.name = "LEVEL " + str(id_level)
        self.lessons = lessons

    def get_lesson(self):
        quant_lessons = len(self.lessons)
        lesson = randint(0, len(self.lessons)-1)
        return list(self.lessons.items())[lesson]

