def fun():
    return "This a Funtion"


def scnd_func():
    yield "This Is Yielded Statment"


print(fun())
for i in scnd_func():
    print(i)
