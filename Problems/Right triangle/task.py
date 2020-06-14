class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.area = self.a * self.b / 2


# triangle from the input
c, a, b = [int(x) for x in input().split()]

if c ** 2 != a ** 2 + b ** 2:  # use pythagoreom theorem to check if right triangle
    print("Not right")
else:
    triangle = RightTriangle(c, a, b)
    print(triangle.area)