A = int(input())  # Hours recommended to sleep
B = int(input())  # Hours maximun to sleep
H = int(input())  # Hours to sleep

if A <= B:
    if H < A:
        print("Deficiency")
    elif H > B:
        print("Excess")
    else:
        print("Normal")