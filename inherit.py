class Man:

    def __init__(self):
        self.age = 0

    def grow_up(self):
        self.age += 1


class Soldier(Man):

    def __init__(self):
        super().__init__()
        self.weapon = 'pistol'

    def fire(self):
        print('bah! bah! bah! with', self.weapon)


class Soldier2(Man):
    weapon = 'pistol'

    def fire(self):
        print('bah! bah! bah! with', self.weapon)


if __name__ == '__main__':
    a = Soldier()
    a.grow_up()
    print(a.age)
    a.fire()
