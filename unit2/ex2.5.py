class Animal:
    """A class representing defualt aspects of an animal."""
    
    # static value for the Animal class
    zoo_name = 'Hayaton'

    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    def is_hungry(self):
        return self._hunger > 0
    
    def feed(self):
        self._hunger -= 1

class Dog(Animal):
    """
    A class representing a dog (inherits from Animal).
    """
    def __str__(self): 
        return 'Dog'
    def talk(self):
        print('woof woof')
    def fetch_stick(self):
       print('There you go, sir!') 

class Cat(Animal):
    """
    A class representing a cat (inherits from Animal).
    """
    def __str__(self): 
        return 'Cat'
    def talk(self):
        print('meow')
    def chase_laser(self):
        print('Meeeeow')

class Skunk(Animal):
    """
    A class representing a Skunk (inherits from Animal).
    """

    def __init__(self, name, hunger=0,stink_count=6):
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def __str__(self): 
        return 'Skunk'
    def talk(self):
        print('tsssss')
    def stink(self):
        print('Dear lord!')

class Unicorn(Animal):
    """
    A class representing a Unicorn (inherits from Animal).
    """
    def __str__(self): 
        return 'Unicorn'
    def talk(self):
        print('Good day, darling')
    def sing(self):
        print('I\'m not your toy...')

class Dragon(Animal):
    """
    A class representing a Dragon (inherits from Animal).
    """
    def __init__(self, name, hunger=0,color='Green'):
        super().__init__(name, hunger)
        self._color = color
    def __str__(selft): 
        return 'Dragon'
    def talk(self):
        print('Raaaawr')
    def breath_fire(self):
        print('$@#$#@$')


def main():
    # Create a list of animals from the list in the mission.
    zoo_lst = [Dog('Brownie', 10), Cat('Zelda', 3), Skunk(
        'Stinky'), Unicorn('Keith', 7), Dragon('Lizzy', 1450), Dog('Doggo', 80), Cat('Kitty', 80), Skunk('Stinky Jr', 80), Unicorn('Clair', 80), Dragon('McFly', 80)]

    # iterates over every animal in the zoo_list
    for animal in zoo_lst:
        # if the animal is hungry, print the animal's type and name and feed it.
        if (animal.is_hungry()):
            print(animal, animal.get_name())
            while animal.is_hungry():
                animal.feed()
        # print what sound the animal does
        animal.talk()

        # identifys what type of animal is the corrent animal and uses the animals special method
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()
    # prints the name of the zoo (same for every animal because of it being a static variable)
    print(animal.zoo_name)

if __name__ == '__main__':
    main()