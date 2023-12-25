import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")

print("It is", now)

FILEPATH = "todos.txt"

while True:
    user_action = input("Type add, edit, show, complete or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos, FILEPATH)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            item = item.title()
            print(f"{index + 1}: {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(input("Number of the todo to edit: ")) - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = F'{len(todos) + 1}: {new_todo}' + '\n'

            functions.write_todos(todos, FILEPATH)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        number = int(input("Number of the todo to complete: ")) - 1
        todos = functions.get_todos()

        todo_to_remove = todos[number]
        todos.pop(number)

        functions.write_todos(todos, FILEPATH)

        message = f"Todo: {todo_to_remove} was completed and removed"
        print(message)
    elif user_action.startswith("exit"):
        break
    else:
        print("Hey, you entered an unknown command")

print("Bye")
