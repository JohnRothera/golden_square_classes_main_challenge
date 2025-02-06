from lib.todo_class import *


"""
Test to see that the todo object has been instatiated
"""


def test_todo_is_instatiated():
    todo = Todo()
    assert isinstance(todo, Todo)


"""
Test to see that constructor sets an empty list
"""


def test_todo_instance_is_empty_list():
    todo = Todo()
    assert todo.todos == []


"""
Test that we can add a new task to todos
"""


def test_add_task_to_todos():
    todo = Todo()
    todo.add_todo("Clean teeth")
    assert todo.todos == ["Clean teeth"]


"""
Test that we can add multiple new tasks to todos
"""


def test_add_multiple_tasks_to_todos():
    todo = Todo()
    todo.add_todo("Clean teeth")
    todo.add_todo("Wash hair")
    assert todo.todos == ["Clean teeth", "Wash hair"]


"""
Test that we can return list of all todos in 
a nicely formatted way.
"""


def test_return_list_of_todos_to_user():
    todo = Todo()
    todo.add_todo("Clean teeth")
    todo.add_todo("Wash hair")
    result = todo.view_todos()
    assert result == "TODO list:\nClean teeth\nWash hair"
