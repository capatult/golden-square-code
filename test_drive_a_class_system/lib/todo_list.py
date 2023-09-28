

class TodoList:
    def __init__(self):
        self._todos = []

    def add(self, todo):
        self._todos.append(todo)

    def incomplete(self):
        result = [
            todo for todo in self._todos
            if not todo.is_complete
        ]
        return result

    def complete(self):
        result = [
            todo for todo in self._todos
            if todo.is_complete
        ]
        return result

    def give_up(self):
        for todo in self._todos:
            todo.mark_complete()
