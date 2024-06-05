import functools

# return the longest name in the given list
def max_name(names):
    return max(names, key=len)

# return the sum of the lengths of the names in the given list
def sum_of_names(names):
    return sum(map(len, names))

# return the two shortest names in the given list
def shortest_names(names):
    return '\n'.join(sorted(names, key=len)[0:2])

# return the length of each name in the given list
def length_of_names(names):
    return '\n'.join(map(str,list(len(name) for name in names)))

# return the names whose length matches the user's input
def user_length_input(names):
    num = input("Enter name length: ")
    return '\n'.join(map(str,list(name for name in names if len(name) == int(num))))




def main():
    # opens a file that contains the names for the mission
    file = open("unit1/names.txt", "r")
    # reads the names from the file and splits them into a list of names
    list_of_names = file.read().split("\n")

    # print all the results for the methods of the mission
    print(list_of_names)
    print(max_name(list_of_names))
    print(sum_of_names(list_of_names))
    print(shortest_names(list_of_names))
    print(length_of_names(list_of_names))
    print(user_length_input(list_of_names))
    
    # closes the file
    file.close()


if __name__ == "__main__":
    main()

