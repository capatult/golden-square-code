from lib.todo_list import TodoList

def test_can_init():
    todo_list = TodoList()

def test_list_of_todos_empty_after_init():
    todo_list = TodoList()
    assert todo_list._todos == []

def test_incomplete_returns_empty_list_after_init():
    todo_list = TodoList()
    assert todo_list.incomplete() == []

def test_giving_up_does_nothing_after_init():
    todo_list = TodoList()
    todo_list.give_up()
    assert todo_list._todos == []
    assert todo_list.incomplete() == []
    assert todo_list.complete() == []