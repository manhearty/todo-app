import glob

print(glob.glob("*.txt"))

for filepath in glob.glob("*.txt"):
    with open(filepath) as file_local:
        todos = file_local.readlines()
        print(todos)