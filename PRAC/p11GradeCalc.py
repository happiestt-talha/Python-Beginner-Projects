
# ~ get scores, calc total, make percentage
#! evaluate percentage according to grades
# ? allot grade

marks = []
for i in range(5):
    marks.append(int(input(f"enter marks for subject No. {i+1} ")))


# getmarks()
total = sum(marks)  # sum of all the elements in list
prcnt = (total/500)*100


def chk(prcnt):
    if prcnt >= 80.00 or prcnt == 100.00:
        grade = 'A'
    elif prcnt >= 70.00 and prcnt < 80.00:
        grade = 'B'
    elif prcnt >= 60.00 and prcnt < 70.00:
        grade = 'C'
    elif prcnt >= 50.00 and prcnt < 60.00:
        grade = 'D'
    else:
        grade = 'F'
    return grade


print(f"Your Marks Are {marks} ")
print(f"Your Total Marks Are {total} ")
print(f"Your Percentage Is {prcnt} ")
print(f"Your Grade Is {chk(prcnt)}")
