import random

class House:
    def __init__(self):
        self.mess = 0
        self.food = 50  # больше стартовой еды

class Cat:
    def __init__(self, name="Cat", home=None):
        self.name = name
        self.money = 0
        self.gladness = 50
        self.satiety = 50
        self.home = home

    def get_home(self):
        self.home = House()

    def eat(self):
        if self.home.food < 5:
            print(f"{self.name} wants to eat but there's no food!")
        else:
            self.satiety += 5
            self.home.food -= 5
            print(f"{self.name} ate. Satiety is now {self.satiety}")

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
        print(f"{self.name} chilled. Gladness is now {self.gladness}")

    def days_indexes(self, day):
        print(f"{' Today the ' + str(day) + ' of ' + self.name + ' life ':=^50}")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}\n")

    def is_alive(self):
        if self.gladness < 0:
            print(f"{self.name} is in depression...")
            return False
        if self.satiety < 0:
            print(f"{self.name} died of hunger...")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False
        if self.home is None:
            print(f"{self.name} found a new home!")
            self.get_home()
        self.days_indexes(day)
        if self.satiety < 20:
            self.eat()
        elif self.gladness < 20:
            self.chill()
        else:
            action = random.choice(["chill", "eat", "sleep"])
            if action == "chill":
                self.chill()
            elif action == "eat":
                self.eat()
        return True

class Human:
    def __init__(self, name, home, cat: Cat):
        self.name = name
        self.home = home
        self.money = 100
        self.cat = cat

    def work(self):
        self.money += 50
        print(f"{self.name} worked. Money: {self.money}")

    def clean_house(self):
        self.home.mess = max(0, self.home.mess - 10)
        print(f"{self.name} cleaned the house. Mess level: {self.home.mess}")

    def buy_food_for_cat(self):
        if self.money >= 20:
            self.home.food += 20
            self.money -= 20
            print(f"{self.name} bought food for {self.cat.name}. Food in house: {self.home.food}")
        else:
            print(f"{self.name} has no money to buy food.")

    def live(self, day):
        print(f"\n{' Nick\'s day ':*^50}")
        if self.home.food < 10:
            self.buy_food_for_cat()
        elif self.home.mess > 20:
            self.clean_house()
        else:
            self.work()

shared_home = House()
Murka = Cat(name="Murka", home=shared_home)
Nick = Human(name="Nick", home=shared_home, cat=Murka)


for day in range(1, 31):
    print()
    Nick.live(day)
    if not Murka.live(day):
        break
