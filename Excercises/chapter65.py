new_user = input("Add a new member: ")

memberfile = open("members.txt", "a")
memberfile.write(new_user)
memberfile.close()