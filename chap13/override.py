class Human:
    def __init__(self, name, life):
        self.name = name
        self.life = life

    def info(self):
        print(self.name)
        print(self.life)

class Soldier(Human):
    def __init__(self, name, life, weapon):
        super().__init__(name, life)
        self.weapon = weapon

    def info(self):
        print("My name is " + self.name)
        print("My HP is {}".format(self.life))

    def talk(self):
        print("My weapon is " + self.weapon)

man = Human("Tom", 50)
man.info()
print("--------------")
prince = Soldier("Alex", 300, "Stick of light")
prince.info()
prince.talk()