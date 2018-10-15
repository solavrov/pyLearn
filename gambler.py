from random import random


class Gambler:

    def __init__(self, capital=5000, target=15000):
        self.capital = capital
        self.target = target

    def tell_about(self):
        print('You are a gambler')
        print('Your capital is', self.capital)
        print('You need to reach', self.target)
        print('----------------------')

    def print_capital(self):
        print('Your capital is', self.capital)
        print('----------------------')

    def is_bankrupt(self):
        answer = False
        if self.capital <= 0:
            answer = True
            print("YOU ARE BANKRUPT...")
            print('----------------------')
        return answer

    def is_lucky(self):
        answer = False
        if self.capital >= self.target:
            answer = True
            print("YOU REACHED THE GOAL!!!")
            print('----------------------')
        return answer

    def play_roulette(self, bet=5000):
        if self.is_bankrupt():
            print('You can\'t play because you are broke')
        else:
            if bet > self.capital:
                bet = self.capital
            print('Your bet is', bet)
            if random() < 18 / 37:
                self.capital += bet
                print('You WON', bet, '!!!')
            else:
                self.capital -= bet
                print('You LOST', bet)
            self.print_capital()


g = Gambler()
g.tell_about()
while True:
    input('Press ENTER to bet')
    g.play_roulette()
    if g.is_bankrupt() or g.is_lucky():
        break
input('Press ENTER to quit')

###