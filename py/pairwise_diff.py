

sel = [2, 4, 6, 3, 5]
a = [2, 3, 4, 6, 7]
b = [3, 4, 5]

#sel = [3, 5, 1, 3, 7]
#a = [3, 4, 5, 1, 9]
#b = [3, 6 , 7]


sum = 0
for i in a:
    for j in b:
        sum += i-j

print(sum)