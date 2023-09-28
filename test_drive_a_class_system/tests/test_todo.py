from lib.todo import Todo

def test_can_init():
    todo = Todo("")

def test_task_set_correctly():
    todo_1 = Todo("Something")
    todo_2 = Todo("Something else")
    assert todo_1.task == "Something"
    assert todo_2.task == "Something else"

def test_init_as_incomplete():
    todo_1 = Todo("")
    todo_2 = Todo("Todo with nonempty task")
    assert todo_1.is_complete == False
    assert todo_2.is_complete == False

def test_can_mark_complete():
    todo_1 = Todo("")
    todo_2 = Todo("Gotta do it")
    todo_1.mark_complete()
    todo_2.mark_complete()
    assert todo_1.is_complete == True
    assert todo_2.is_complete == True

def test_remains_complete_if_marked_complete_twice():
    todo = Todo("Thing")
    todo.mark_complete()
    todo.mark_complete()
    assert todo.is_complete == True