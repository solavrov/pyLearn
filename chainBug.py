class Foo:

    def __init__(self):
        self.value = 0

    def add_one(self):
        self.value += 1
        return self


if __name__ == "__main__":
    a = Foo()
    a.add_one().add_one().add_one()
    print(a.value)
