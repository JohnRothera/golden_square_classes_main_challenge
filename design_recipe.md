# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Todo:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   none: sets empty todo list
        # Side effects:
        #   Sets a task in todo list
        pass # No code here yet

    def add_todo(self, todo):
        # Parameters:
        #   task: string representing a single todo task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self.todo list
        pass # No code here yet

    def see_todo_tasks(self):
        # Returns:
        #   A list showing the user any todo tasks
        # Side-effects:
        #   Throws an exception if no task is set
        #   Possibly preferential to return a string so we don't 
        #   exit the program
        pass # No code here yet

    def remove_complete_tasks(self, todo_complete):
        # Returns:
        #   firstly run the see_todo_tasks function 
        #   ask the user if they have completed any.
        #   if Y, remove from the list.
        # Side-effects:
        #   Throws an exception if no task is set
        #   Possibly preferential to return a string so we don't 
        #   exit the program
        pass # No code here yet

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Test to see that the todo object has been instatiated
"""
def test_todo_is_instatiated():
    todo = Todo()
    assert isinstance(todo, Todo())

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

"""
Test that the user can remove a task of their choice. 
May require feedback from the program.
"""
def test_remove_todo_task_from_todos_list():
    todo = Todo()
    todo.add_todo("Clean teeth")
    todo.add_todo("Wash hair")
    todo.remove_todo("Wash hair")
    result = todo.view_todos()
    assert result == "TODO list:\nClean teeth"
    
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
