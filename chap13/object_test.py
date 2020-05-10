class GameCharacter:
    def __init__(self, aJob, aLife):
        self.job = aJob
        self.life = aLife

    def info(self):
        print(self.job)
        print(self.life)

warrior = GameCharacter("Warrior", 100)
warrior.info()

magician = GameCharacter("Magician", 80)
magician.info()