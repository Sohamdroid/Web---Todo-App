FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return [t.strip() for t in todos]  # remove ALL whitespace

def write_todos(todos, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(t + "\n" for t in todos)