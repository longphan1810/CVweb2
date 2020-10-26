class Animal:
    def __init__(self, Animal):
        print(Animal, 'là một loài động vật.')
 
class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'là động vật máu nóng.')
        super().__init__(mammalName)
    
class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammal):
        print(NonWingedMammal, "không thể bay.")
        super().__init__(NonWingedMammal)

class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "không thể bơi.")
        super().__init__(NonMarineMammal)

class Voi(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Voi có 4 chân.')
        super().__init__('Voi')
     
d = Voi()

bat = NonMarineMammal('Dơi')