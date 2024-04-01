f = open('p4.txt', 'r')
i = 0
s = 0
students = ["Ali", "Fatima", "Saeed", "Ayesha", "Ahmed", "Zainab", "Bilal", "Hira", "Kamran", "Sana",
            "Imran", "Nazia", "Usman", "Nadia", "Rizwan", "Mehreen", "Shahid", "Sadia", "Farhan", "Fariha",]

Subjects = ['ICT', 'ECC', 'OOP']

print("Welcome to the Student Management System")
arr = []
while True:
    data = f.readline().strip()
    if not data:
        break
    marks = data.split(',')
    if len(marks) >= 3:
        m1 = int(marks[0])
        m2 = int(marks[1])
        m3 = int(marks[2])
    else:
        m1 = int('')
        m2 = int('')
        m3 = int('')

    print(f'{students[i]} has got {m1} marks in {Subjects[s]}')
    print(f'{students[i]} has got {m2} marks in {Subjects[s+1]}')
    print(f'{students[i]} has got {m3} marks in {Subjects[s+2]}')
    total_marks = m1+m2+m3
    print(f'Total : {total_marks}\n')
    arr.append(total_marks)
    i += 1

avg_list = list(map(lambda x: (x/200)*100, arr))
topper = list(filter(lambda x: x > 85, avg_list))

for i in avg_list:
    print(i)

fi = open('p4List.txt', 'w')
print(f'NAME{"":^13}TOTAL{" ":<10}AVERAGE')
fi.write(f'NAME{"":^13}TOTAL{" ":<10}AVERAGE\n')
for i in range(len(students)):
    print(f'{students[i]:<10}{arr[i]:>10}{avg_list[i]:>20}')
    fi.write(f'{students[i]:<10}{arr[i]:>10}{avg_list[i]:>20} \n')

print("\n\tToppers are:")
for i in topper:
    print(i)

for i in range(20):
    if (topper[i] == avg_list[i]):
        print(students[i])
    else:
        continue


f.close()
fi.close()
