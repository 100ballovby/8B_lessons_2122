l = [4, 12, 7, 34, 50, 20, 5, 3, 1, 0]

for i in range(len(l)):
    if l[i] == 20:
        l[i] = 200
        break

print(l)
