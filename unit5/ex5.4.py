class IDIterator():
    """
    An iterator that generates next 10 valid ID numbers.
    """
    def __init__(self,id):
        self._id = id
        self._index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index > 10:
            raise StopIteration
        self._index += 1
        self._id+=1
        while not check_id_valid(self._id) and self._id <= 999999999 :
            self._id +=1
        return self._id
    
#function is getting an id and checking to see if it is valid
def check_id_valid(id_number):
    sum_of_numbers =0
    i=0
    for num in str(id_number):
        number = int(num)
        if i % 2 == 0:
            number *= 1
        else:
            number *= 2  
        while number > 9:
            number -= 9 
        sum_of_numbers += number
        i+=1
    return sum_of_numbers%10 == 0

#function gets an id and return a generator that generates the next valid id number
def id_generator(id_number):
    while True:
        id_number+=1
        while not check_id_valid(id_number) and id_number <= 999999999 :
            id_number +=1
        yield id_number

def main():
    id = int(input("Enter ID: "))
    mode = input("Generator or Iterator? (gen/it)? ")
    # generator prints 10 new valid ids
    if(mode == "gen"):
        id_gen = id_generator(id)
        for i in range(10):
            print(next(id_gen))
    # iterator prints 10 new valid ids
    elif(mode == "it"):
        for i in IDIterator(id):
          print(i)


if __name__ == "__main__":
    main()