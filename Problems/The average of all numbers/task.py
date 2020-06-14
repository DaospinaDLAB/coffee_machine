# put your python code here
a = int(input())
b = int(input())
sum_ = 0
length = 0
for i in range(a, (b + 1)):
    if i % 3 == 0:
        sum_ += i
        length += 1
print(sum_ / length)
