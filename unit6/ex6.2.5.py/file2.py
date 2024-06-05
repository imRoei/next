from file1 import GreetingCard

class BirthdayCard(GreetingCard):
    def __init__(self, recipient='Dana Ev', sender='Eyal Ch',sender_age=0):
        super().__init__(recipient, sender)
        self._sender_age = sender_age

    def greeting_msg(self):
        return f'Happy birthday: {self._recipient},from{self._sender}, {self._sender_age} years old'
        

def main():
    card1 = GreetingCard()
    print(card1.greeting_msg())

if __name__ == "__main__":
    main()