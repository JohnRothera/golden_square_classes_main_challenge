class Todo:
    def __init__(self):
        self.todos = []

    def add_todo(self, todo):
        self.todos.append(todo)

    def view_todos(self):
        result = "\n"
        return "TODO list:\n" + result.join(self.todos)

    def remove_todo(self, todo):
        if todo in self.todos:
            return self.todos.remove(todo)
        else:
            return "This task has been completed already"
