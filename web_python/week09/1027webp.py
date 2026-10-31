f = open("./test.txt", "wt")

f.write("Hello World\n")
f.writelines(["Python\n", "Hi\n", "Babo", "Hi"])

f.close()

f = open("./test.txt", "r")

print(f.readlines())

f.close()