def format_string(string):
    return string + '\n'


def read_todos(filepath='todos.txt'):
    # Using with-context-manager, removes need to manually close the file
    with open(filepath, 'r') as file:
        todo_list = file.readlines()
        return todo_list


def write_todos(todos_list, filepath='todos.txt'):
    # Using with-context-manager, removes need to manually close the file
    with open(filepath, 'w') as file:
        file.writelines(todos_list)


def add_todo(action):
    todo = format_string(action)
    all_todos = read_todos()
    all_todos.append(todo)
    write_todos(all_todos)


def complete_todo(index):
    todos = read_todos()
    completed_item = int(index)
    todos.pop(completed_item)
    write_todos(todos)
