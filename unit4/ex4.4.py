# this function returns a generator of all the possible seconds
def gen_sec():
    return (x for x in range(0, 60))

# this function returns a generator of all the possible minuts
def gen_min():
    return (x for x in range(0, 60))

# this function returns a generator of all the possible hours
def gen_hours():
    return (x for x in range(0, 24))

# this function returns a generator of all the possible hour, minutes, seconds in a day
def gen_time():
    for h in gen_hours():
        for m in gen_min():
            for s in gen_sec():
                yield f"{h:02d}:{m:02d}:{s:02d}"

# this function gets a starting year and generates the next years, starting by default from 2019
def gen_years(start=2019):
    while True:
        yield start
        start += 1

# this function returns a generator of all the possible months
def gen_months():
    return (x for x in range(1, 13))

# this function returns a generator of all the possible days in a given month, given a leap year or not
def gen_days(month, leap_year=True):
    days = [31, 29 if leap_year else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return (x for x in range(1, days[month-1] + 1))

# this function generates all the possible years, months, days and time in a day 
# starting from 2019 (given by the defualt value of gen_years functin)

def gen_date():
    for y in gen_years():
        leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
        for m in gen_months():
            for d in gen_days(m, leap):
                for gt in gen_time():
                    yield f"{d:02d}/{m:02d}/{y:04d} {gt}"


def main():
    gen_d = gen_date()

    #prints 1 in every 1000000 dates generated 
    while True:
        print(next(gen_d))
        for _ in range(999999):
            next(gen_d)

if __name__ == '__main__':
    main()