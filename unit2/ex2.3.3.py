class dog:
    counter = 0
    def __init__(self, name = input("Enter name:"), age =input("Enter age:") ):
        self._name = name
        self._age = age
        counter+=1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age
    
    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

def main():
    dog1 = dog("Lichy", 8)
    dog1.birthday()
    print(dog1.get_age())
    dog2 = dog("Kiwii",5)
    print(dog2.get_age())

if __name__ == "__main__":
    main()