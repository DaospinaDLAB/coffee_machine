class Sphere:
    PI = 3.1415
    constant = 4 / 3
    volume = 0

    def __init__(self, radius):
        self.radius = radius
        self.volume = self.constant * (self.PI * self.radius ** 3)
