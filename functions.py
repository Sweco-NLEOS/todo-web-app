FILEPATH = "todos.txt"


def get_todos(filepath_arg=FILEPATH):
    """" Lees tekst bestand en geef todo's """
    with open(filepath_arg, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath_arg=FILEPATH):
    """ schrijf lijst met todo's """
    with open(filepath_arg, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())

print("functions loaded")
