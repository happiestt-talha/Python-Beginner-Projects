class alag:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, ot):
        if isinstance(ot, alag):
            return alag(self.x+ot.x, self.y+ot.y)
        else:
            return "TypeError"


a = alag(3, 2)
b = alag(42, 48)
res = a+b
print(res)
print(f"Resulta: ({res.x}   {res.y})")
