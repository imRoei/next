class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
            self.age += 1

    def get_age(self):
            return self.age

def main():
    dog1 = dog("Lichy", 8)
    dog1.birthday()
    print(dog1.get_age())
    dog2 = dog("Kiwii",5)
    print(dog2.get_age())

if __name__ == "__main__":
    main()