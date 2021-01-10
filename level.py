from random import randint

class level:
    def __init__(self, name, lessons):
        self.name = name
        self.lessons = lessons

    def get_lesson(self):
        quant_lessons = len(self.lessons)
        lesson = randint(0, len(self.lessons)-1)
        return list(self.lessons.items())[lesson]


