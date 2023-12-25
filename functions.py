def get_todos(file_path="todos.txt"):
    with open(file_path, "r") as local_file:
        todos_local = local_file.readlines()
    return todos_local


def write_todos(local_todos, file_path="todos.txt"):
    with open(file_path, "w") as file:
        file.writelines(local_todos)


if __name__ == "__main__":
    print("Hello from functions")
