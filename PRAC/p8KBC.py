Questions = [
    ["who is founder pakistan? ", "Quaid e Azam", "Iqbal", "Fatima", "Gandhi", 1],
    ["what is my birthday?", "12", "15", "14", "43", 3],
    ["During which period did the Renaissance take place?", "5th to 8th century",
        "14th to 17th century", "10th to 13th century", "19th to 20th century", 3],
    ["Who was the first Roman Emperor?", "Julius Caesar",
        "Augustus", "Nero", "Constantine", 3],
    ["The Great Wall of China was primarily built during the reign of which dynasty?",
        "Han Dynasty", "Tang Dynasty", "Ming Dynasty", "Qin Dynasty"]
]

levels = [10, 100, 1000, 10000, 50000]

for i in range(0, len(Questions)):
    query = Questions[i]
    money = 0
    print(f"question for rupees: {levels[i]}")
    print(f"Q1={Questions[i][0]}")
    print(f"1){Questions[i][1]},     2){Questions[i][2]} ")
    print(f"3){Questions[i][3]},     4){Questions[i][4]} ")
    reply = int(input("enter you answer "))
    if (reply == Questions[i][-1]):
        print(f"you won {levels[i]} rupees!!! ")
        money += levels[i]
    else:
        print("wrong answer")
        break

print("\n\n     !!!CONGRATULATIONS!!!")
print(f"your take home money is {money} rupees ")
