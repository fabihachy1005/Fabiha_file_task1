# A
file = open("students.csv", "w")
file.write("student_name,section,age\n")
file.write("Ariha,2,15\n")
file.write("Sara,1,16\n")
file.write("Lima,3,15\n")
file.close()

# B
file = open("students.csv", "r")   # ✅ changed to r
for line in file:
    data = line.strip().split(",")

    name = data[0]
    section = data[1]
    age = data[2]

    print(f"{name} is in section {section}, her age is {age}")
file.close()