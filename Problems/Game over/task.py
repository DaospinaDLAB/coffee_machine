scores = input().split()
# put your python code here
cont_miss = 0
cont_ace = 0
message = "You won"
if 15 <= len(scores) <= 50:
    for i in scores:
        if i == 'I':
            cont_miss += 1
            if cont_miss == 3:
                message = "Game over"
                break
        else:
            cont_ace += 1

print(message)
print(cont_ace)
