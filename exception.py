student = {
    "name" : "Mark",
    "id" : 100
}

try:
    lastName = student["name"]
    lastName += 3
    print(lastName)
except KeyError:
    print("Error")
except TypeError:
    print("Type Error")
except Exception:
    print("unknown error")



try:
    lastName = student["name"]
    lastName += 3
    print(lastName)
except Exception as error:
    print(error)


def getMax(x,y=0):
    return x +y

print(getMax(x=3))


def var_args(name , *args):
    print (args)

var_args("test", "sddf", 3, "True", None)


def k_args(**kwargs):
    print(kwargs["name"])

k_args(name="test", city="city", zip =3, Snow = "True", Desc = None)


def saveFile(name):
    try:
        f = open("alldata.txt", "a")
        f.write(name)
        f.close()
    except Exception:
        print("Error")

saveFile("arjun")

number = lambda x: x *2;
print(number(3))

print("EOL")