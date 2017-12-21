class animals_on_the_farm:
    def __init__(self, weght, name, legs_amount, say, speed):
        self.weght = weght
        self.name = name
        self.legs_amount = legs_amount
        self.speed = speed
        self.say = say

    def stop(self):
        self.speed = 0

    def say_somthing(self):
        print(self.say)

    def rename(self, name):
        self.name = name
        return self.name

class birds(animals_on_the_farm):
    def __init__(self, name, weght, say, legs_amount=2, speed=0):
        super().__init__(name, weght, legs_amount, say, speed)

    def fly(self):
        self.speed += 10

class animals(animals_on_the_farm):
    def __init__(self, name, weght, say, legs_amount=4, speed=0):
        super().__init__(name, weght, legs_amount, say, speed)

    def go(self):
        self.speed += 10

cow = animals(name = 'Cow', weght=200, say='Moo')
goat = animals(name = 'Goat', weght=50, say='Baa')
sheep = animals(name = 'Dolly', weght=60, say='Maa')
pig = animals(name = 'Pig', weght=100, say='Wiiii')
duck = birds(name = 'Mark', weght=6, say='quack quack')
chichens = birds(name = 'Dinner', weght=4, say='Oh, shit!!!')
geese = birds(name = 'Gus', weght=10, say='I say HA!')

for animal in [cow, goat, sheep, pig, duck, chichens, geese]:
    print(animal.__dict__)
