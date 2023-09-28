from lib.todo_list import TodoList
from lib.todo import Todo

"""
When an instance of Todo is added to a new TodoList instance
The instance is stored in a list attribute of the TodoList instance
"""
def test_can_add_todo_instance_to_todo_list():
    todo_list = TodoList()
    todo = Todo("Stuff to do")
    todo_list.add(todo)
    assert todo_list._todos == [todo]

"""
When two instances of Todo are added to a new TodoList instance
The instances are stored in a list attribute of the TodoList instance in the order they were added
"""
def test_can_add_two_todo_instances_to_todo_list():
    todo_list = TodoList()
    todo_1 = Todo("Do thing 1")
    todo_2 = Todo("Do thing 2")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    assert todo_list._todos == [todo_1, todo_2]

"""
When instances of Todo are added to a new TodoList instance
And those instances are all incomplete
And we call .incomplete() on the TodoList instance
It returns a list of all stored Todo instances in the order they were added
"""
def test_all_todo_instances_returned_by_incomplete_if_all_incomplete():
    todo_list = TodoList()
    todo_1 = Todo("Do thing A")
    todo_2 = Todo("Do thing B")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    incomplete_todos = todo_list.incomplete()
    assert incomplete_todos == [todo_1, todo_2]

"""
When instances of Todo are added to a new TodoList instance
And those instances are all incomplete
And we call .complete() on the TodoList instance
It returns an empty list
"""
def test_no_todo_instances_returned_by_complete_if_all_incomplete():
    todo_list = TodoList()
    todo_1 = Todo("First task")
    todo_2 = Todo("Second task")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    complete_todos = todo_list.complete()
    assert complete_todos == []

"""
When instances of Todo are added to a new TodoList instance
And those instances are all complete
And we call .incomplete() on the TodoList instance
It returns an empty list
"""
def test_no_todo_instances_returned_by_incomplete_if_all_complete():
    todo_list = TodoList()
    todo_1 = Todo("Do thing A")
    todo_1.mark_complete()
    todo_2 = Todo("Do thing B")
    todo_2.mark_complete()
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    incomplete_todos = todo_list.incomplete()
    assert incomplete_todos == []

"""
When instances of Todo are added to a new TodoList instance
And those instances are all complete
And we call .complete() on the TodoList instance
It returns a list of all stored Todo instances in the order they were added
"""
def test_all_todo_instances_returned_by_complete_if_all_complete():
    todo_list = TodoList()
    todo_1 = Todo("Do thing A")
    todo_1.mark_complete()
    todo_2 = Todo("Do thing B")
    todo_2.mark_complete()
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    incomplete_todos = todo_list.complete()
    assert incomplete_todos == [todo_1, todo_2]

"""
When instances of Todo are added to a new TodoList instance
And some of those instances are incomplete and some are complete
And we call .incomplete() on the TodoList instance
It returns a list of only the incomplete Todo instances in the order they were added
"""
def test_correct_todo_instances_correctly_returned_by_complete_and_incomplete():
    todo_list = TodoList()
    tasks = [
        "Thing Zero",
        "Thing One",
        "Thing Two",
        "Thing Three",
        "Thing Four",
    ]
    todos = [
        Todo(task)
        for task in tasks
    ]
    todos[1].mark_complete()
    todos[3].mark_complete()
    todos[4].mark_complete()
    for todo in todos:
        todo_list.add(todo)
    complete_todos = todo_list.complete()
    incomplete_todos = todo_list.incomplete()
    assert complete_todos == [todos[1], todos[3], todos[4]]
    assert incomplete_todos == [todos[0], todos[2]]

"""
When an incomplete instance of Todo is added to a new TodoList instance
And then that instance is marked as complete
And we call .incomplete() and .complete() on the TodoList instance
It returns an empty list for .incomplete()
It returns a list containing just that Todo instance for .complete()
"""
def test_complete_and_incomplete_update_correctly_for_single_todo_instance_todo_list():
    todo_list = TodoList()
    todo = Todo("Get this done soon!")
    todo_list.add(todo)
    todo.mark_complete()
    complete_todos = todo_list.complete()
    incomplete_todos = todo_list.incomplete()
    assert complete_todos == [todo]
    assert incomplete_todos == []


"""
When instances of Todo are added to a new TodoList instance
And some of those instances are incomplete and some are complete
And we call .give_up() on the TodoList instance
And we call .incomplete() on the TodoList instance
It returns an empty list
"""
def test_incomplete_returns_empty_list_after_give_up_called():
    todo_list = TodoList()
    tasks = [
        "Thing Zero",
        "Thing One",
        "Thing Two",
        "Thing Three",
        "Thing Four",
    ]
    todos = [
        Todo(task)
        for task in tasks
    ]
    todos[1].mark_complete()
    todos[3].mark_complete()
    todos[4].mark_complete()
    for todo in todos:
        todo_list.add(todo)
    todo_list.give_up()
    incomplete_todos = todo_list.incomplete()
    assert incomplete_todos == []

"""
When instances of Todo are added to a new TodoList instance
And some of those instances are incomplete and some are complete
And we call .give_up() on the TodoList instance
And we call .complete() on the TodoList instance
It returns a list of all stored Todo instances in the order they were added
"""
def test_complete_returns_correct_list_with_all_todos_after_give_up_called():
    todo_list = TodoList()
    tasks = [
        "Thing Zero",
        "Thing One",
        "Thing Two",
        "Thing Three",
        "Thing Four",
    ]
    todos = [
        Todo(task)
        for task in tasks
    ]
    todos[1].mark_complete()
    todos[3].mark_complete()
    todos[4].mark_complete()
    for todo in todos:
        todo_list.add(todo)
    todo_list.give_up()
    complete_todos = todo_list.complete()
    assert complete_todos == todos

"""
When instances of Todo are added to a new TodoList instance
And some of those instances are incomplete and some are complete
And we call .give_up() on the TodoList instance
And we add one new complete and one new incomplete Todo instance to the TodoList
And we call .complete() and .incomplete() on the TodoList instance
It returns a list with all previous given-up-on-todos and the new Todo instance in the order they were added for .complete()
It returns a list containing only the new incomplete Todo instance for .incomplete()
"""
def test_complete_returns_correct_list_with_all_todos_after_give_up_called():
    todo_list = TodoList()
    tasks = [
        "Thing Zero",
        "Thing One",
        "Thing Two",
        "Thing Three",
        "Thing Four",
    ]
    todos = [
        Todo(task)
        for task in tasks
    ]
    todos[1].mark_complete()
    todos[3].mark_complete()
    todos[4].mark_complete()
    for todo in todos:
        todo_list.add(todo)
    todo_list.give_up()
    new_todo_1 = Todo("Not going to do this one")
    new_todo_2 = Todo("Going to do this one though")
    new_todo_2.mark_complete()
    todo_list.add(new_todo_1)
    todo_list.add(new_todo_2)
    complete_todos = todo_list.complete()
    incomplete_todos = todo_list.incomplete()
    assert complete_todos == todos + [new_todo_2]
    assert incomplete_todos == [new_todo_1]

"""
When we add the same instance of Todo to a new TodoList instance twice
And we mark that Todo as complete
It is reflected across both elements of TodoList's stored Todo instances (as they are the same instance)
"""
def test_adding_same_todo_instance_to_todolist_twice_causes_same_instance_to_be_stored_twice():
    todo_list = TodoList()
    todo = Todo("So important you might want to make a note of it twice!")
    todo_list.add(todo)
    for stored_todo in todo_list._todos:
        assert stored_todo is todo
