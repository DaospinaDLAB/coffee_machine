numbers = 0
cont = 0
while True:
    number = input()
    if number == ".":
        break
    numbers += int(number)
    cont += 1
print(numbers / cont)
