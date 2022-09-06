class player:

    def __init__(self, name, xp):
        self.name = "nico"
        self.xp = xp

    def say_hello(self):
        print(f"hello my name is {self.name}")


nico = player("nico", 1000)
print(nico.name, nico.xp)
nico.say_hello()