from file1 import GreetingCard
from file2 import BirthdayCard


def main():
    greeting = GreetingCard()
    print(greeting.greeting_msg())
    birthday = BirthdayCard()
    print(birthday.greeting_msg())


if __name__ == "__main__":
    main()