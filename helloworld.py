print("hello world")
answer = True
pi = "John"
print(int(answer))

number = 5
if number == 5:
    print("Number is 5")
else:
    print("Number is not 5")

if number:
    print("truthy")

python_course = True
if not python_course:
    print("True")


if number == 5 and python_course:
    print("both truthy")


a = 1
b = 2

print("bigger" if a > b else "smaller")

studentNames = ["mark", "katrina","jessica"]
print(studentNames[-1])
print("mark" in studentNames)

#del studentNames[2]
print(studentNames[1:2])

for n in studentNames:
    print(n)


for index in range(10):
    print(index)

    print("")
    print("")

    for index in range(1,10, 1):
        print(index)
        break


studentNames = ["mark", "katrina","jessica","frank", "grimes", "paul"]

for name in studentNames:
    if name == "jessica":
        continue
        print("found jessica")
    print("Currently testin " + name)
