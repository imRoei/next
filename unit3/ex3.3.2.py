class UnderAge(Exception):
    def __init__(self, age):
        self._age = int(age)
        super().__init__()

    def __str__(self):
        return f"You are not old enough, you need {18 - self._age} more years."

def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
        else:
            print("You should be invited, " + name)
    except UnderAge as e:
        print(e)

send_invitation("omri",17)