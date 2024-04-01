daysOfWeek = ["monday", "tuesday", "wednesday",
              "thursday", "friday", "saturday", "sunday"]
n = int(input("enter the number of day in week "))
if n == 1:
    print(f"The {n}st day is {daysOfWeek[n-1]}")
elif n == 2:
    print(f"The {n}nd day is {daysOfWeek[n-1]}")
elif n == 3:
    print(f"The {n}rd day is {daysOfWeek[n-1]}")
else:
    print(f"The {n}th day is {daysOfWeek[n-1]}")
