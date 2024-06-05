import itertools


def comb_to_money():
    for i in range(0, 15):
        for comb in itertools.combinations([20,20,20,10,10,10,10,10,5,5,1,1,1,1,1],i):
            if sum(comb) == 100:
                yield comb

def main():
    hundredcomb = {comb for comb in comb_to_money()}
    print(len(hundredcomb))


if __name__ == '__main__':
    main()
    