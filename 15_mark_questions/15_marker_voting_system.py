#voting system for 30 marker questions

print("Welcome to the student voting system")

class tutor_group():
    def __init__(self, name, students):
        self.name = ""
        self.num_students = 0
        self.num_candidates = 0
        self.name_candidates = []

    def add_vote(self):
        self.votes += 1

    def __str__(self):
        return f"{self.name}: {self.votes}"






