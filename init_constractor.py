class Enemy:

    def __init__(self, life):
        self.enargy = life

    def attack(self):
        print("ouch")
        self.enargy -= 1
    def checklife(self):
        if self.enargy <= 0:
            print("i am dead")
        else:
            print(str(self.enargy) + " life left")

sadi = Enemy(5)
queen = Enemy(10)

sadi.attack()
sadi.checklife()

queen.attack()
queen.checklife()
