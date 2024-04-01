def avg(*num):
    avrg = sum(num) / len(num)
    print(avrg)


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [1, 2, 3, 4, 5, 6, 7]
l3 = [1, 2, 7, 8, 9]
l4 = [1, 2, 3, 4]

# Args
avg(*l1)
avg(*l2)
avg(*l3)
avg(*l4)

# Kwargs are same
