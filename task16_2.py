class Turtle:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
    def go_up(self):
        self.y += self.s
        return self.y
    def go_down(self):
        self.y -= self.s
        return self.y
    def go_left(self):
        self.x -= self.s
        return self.x
    def go_right(self):
        self.x += self.s
        return self.x
    def evolve(self):
        self.s += 1
        return self.s
    def degrade(self):
        if self.s <= 0:
            print('s = 0')
        else:
            self.s -=1
        return self.s
    def count_moves(self, x2, y2):
        return round(abs(x2-self.x)/self.s)+round(abs(y2-self.y)/self.s)

r=Turtle(3, 6, 2)

print(r.go_up())

print(r.go_down())

print(r.go_left())

print(r.go_right())

print(r.evolve())

print(r.degrade())

print(r.count_moves(7,3))
