x, y, z = 0, 0, 0
a = int(input())
for i in range(a):
    num = int(input())
    if num % 3 == 0:
        x += 1
    elif num % 3 == 1:
        y += 1
    elif num % 3 == 2:
        z += 1
print(x, y, z)
