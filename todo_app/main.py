#from functions import get_todos,write_todos
from todo_app import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit , complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            print(f"{index + 1}.{item.strip("\n")}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1
            todos = functions.get_todos()
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue



    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:]) - 1
            todos = functions.get_todos()
            todo_to_complete = todos[number].strip("\n")
            todos.pop(number)

            functions.write_todos(todos)

            message = f"Todo {todo_to_complete} has been completed."
            print(message)
        except IndexError:
            print("There is no Item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid input")


print("Bye!")




