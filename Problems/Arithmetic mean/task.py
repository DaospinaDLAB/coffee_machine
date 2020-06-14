numbers = [int(x) for x in input().split()]
suma = 0
for i in numbers:
    suma += i
mean = suma / len(numbers)
print(mean)
