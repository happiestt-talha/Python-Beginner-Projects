import time
hours = int(time.strftime("%H"))
name = input("Enter your Good Name: ")
if hours < 12:
    print("GM Dear", name)
elif hours > 12 and hours < 15:
    print("Good Afternoon", name)
elif hours > 15 and hours < 18:
    print("Good Evening", name)
else:
    print("Good Night", name)
print("the time is", time.strftime("%I, %M, %S"))
