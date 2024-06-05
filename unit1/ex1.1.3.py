def dividein4(num):
    return (num%4==0)

def four_dividers(number):
    return list(filter(dividein4, range(1, number+1)))

print(four_dividers(9))