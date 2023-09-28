

class Todo:

    def __init__(self, task):
        self.task = task
        self.is_complete = False

    def mark_complete(self):
        self.is_complete = True
