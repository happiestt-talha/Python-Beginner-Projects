for i in range(5):
    for j in range(7):
        print('*', end='')
    print()

BASE_SIZE = 4
for r in range(BASE_SIZE):
    for c in range(r + 1):
        print('*', end='')
    print()
for i in range(5):
    for j in range(i):
        print(' ', end='*')
    print('#')

for i in range(5):
    print('#', end='')
    for j in range(i):
        print(' ', end='')
    print('#')
