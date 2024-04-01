class farig:
    def __init__(self, value):
        self.val = value

    @property.setter()
    def show(self):
        print(f"Value is {self.val}")


a = farig(12)
a.show = 23
print(a.val)
a.show()
