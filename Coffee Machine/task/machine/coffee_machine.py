class CoffeeMachine:
    water = 400
    milk = 540
    coffee = 120
    dis_cups = 9
    money = 550

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee_type = input()
        if coffee_type == '1':
            if self.water < 250:
                print("Sorry, not enough water!")
            elif self.coffee < 16:
                print("Sorry, not enough coffee!")
            elif self.dis_cups < 1:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water = self.water - 250
                self.coffee = self.coffee - 16
                self.money = self.money + 4
                self.dis_cups = self.dis_cups - 1

        elif coffee_type == '2':

            if self.water < 350:
                print("Sorry, not enough water!")
            elif self.milk < 75:
                print("Sorry, not enough milk!")
            elif self.coffee < 20:
                print("Sorry, not enough coffee!")
            elif self.dis_cups < 1:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water = self.water - 350
                self.milk = self.milk - 75
                self.coffee = self.coffee - 20
                self.money = self.money + 7
                self.dis_cups = self.dis_cups - 1

        elif coffee_type == '3':

            if self.money < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            elif self.coffee < 12:
                print("Sorry, not enough coffee!")
            elif self.dis_cups < 1:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.money = self.money - 200
                self.milk = self.milk - 100
                self.coffee = self.coffee - 12
                self.money = self.money + 6
                self.dis_cups = self.dis_cups - 1
        elif coffee_type == 'back':
            print()

    def fill(self):
        self.water = self.water + int(input("Write how many ml of water do you want to add:"))
        self.milk = self.milk + int(input("Write how many ml of milk do you want to add:"))
        self.coffee = self.coffee + int(input("Write how many grams of coffee beans do you want to add:"))
        self.dis_cups = self.dis_cups + int(input("Write how many disposable cups of coffee do you want to add:"))

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def state(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee, "of coffee beans")
        print(self.dis_cups, "of disposable cups")
        print(self.money, "of money")

    def user(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):")
            if action == 'exit':
                break
            elif action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == 'remaining':
                self.state()


machine = CoffeeMachine()
machine.user()
