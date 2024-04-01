class employee:
    Company = "Meta"

    def __init__(s, name, age, sal):
        s.name = name
        s.age = age
        s.salary = sal

    @classmethod
    def CompChanger(s, cmp):
        s.Company = cmp

    def showDet(s):
        print(f"Company: {s.Company}")
        print(f"Name: {s.name}")
        print(f"Age: {s.age}")
        print(f"Salary: {s.salary}\n")

    def __str__(s):
        return f"Company: {s.Company}\nName: {s.name}\nAge: {s.age}\nSalary: {s.salary}\n"


e1 = employee('Talha', 21, 120000)
print(e1)

e2 = employee('Sam', 300, 10000)
e2.CompChanger('Apple')
e2.showDet()

e3 = employee('Mar', 19, 17000)
print(e3)
