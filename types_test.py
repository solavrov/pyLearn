class Car:

    def __init__(self):
        self.speed = 0
        self.color = "black"

    def speedup(self):
        self.speed += 10
        return self


def repaint(c: Car, color: str) -> Car:
    c.color = color
    return c


def paint_green(c: Car) -> Car:
    c.color = "green"
    return c


def do_some(f: callable, c: Car) -> Car:
    return f(c)


a = Car()
a.speedup()
b = repaint(a, "red")
b.speedup()
do_some(paint_green, b)
print(b.color)

