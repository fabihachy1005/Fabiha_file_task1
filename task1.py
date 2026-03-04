# A
file = open("student info.txt", "w")
file.write("C12\n")
file.write("C23\n")
file.write("C44\n")
file.close()

# B
file = open("student info.txt", "w")
file.write("C13\n")
file.write("C24\n")
file.write("C45\n")
file.close()

# C
file = open("student info.txt", "r")
for line in file:
    print(line.strip())
file.close()