def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


# ~ printing 0 to print it every time when iteration begins
n = int(input("enter you number "))
print(0)
for i in range(0, n):
    print(fibo(i))

print("Done BOss ")
