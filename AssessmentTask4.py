print("Assessment Task 4 \n")

print("Number 1: Write a function that computes the value of a sphere given its radius.")


def volume(radius):
    pi = 3.14
    volume = 4 / 3 * (pi * radius ** 3)
    print(volume, "\n")
    pass


volume(2)

print("Number 2: Write a function that checks whether a number is in a given range.")


def ran_check(num, low, high):
    list1 = []
    for x in range(low, high):
        list1.append(x)
    if num in list1:
        print(num, "is in the range of ", low, "and", high, "\n")
    else:
        print(num, "is not in the range of ", low, "and", high, "\n")
    pass


ran_check(5, 2, 7)

print("Number 3: Write a python function that accepts a string and calculate the number of uppercase and lower case")


def up_low(sentence):
    uppercase = 0
    lowercase = 0
    for letters in sentence:
        if letters.isupper():
            uppercase += 1
        if letters.islower():
            lowercase += 1
    print("Original String: Panget Ka Bobo tang ina mo")
    print("No. of uppercase letters", uppercase)
    print("No. of lowercase letters", lowercase, "\n")
    pass


up_low("Panget Ka Bobo ka tang ina mo")

print("Number 4: Write a python function that takes a list and returns a new list with unique elements of the first "
      "list")

def unique_List(yourList):
    setFirst = set(yourList)
    listAgain = list(setFirst)
    print(yourList)
    print(listAgain, "\n")
    pass
unique_List([1,1,1,1,2,2,2,2,3,3,3,4,4,4,5,5,5])

print("Number 5: Write a python function to multiply all the numbers in a list")
def multiply(numbers):
    product = 1
    for members in numbers:
        product = product * members
    print(product)
    pass
multiply([1,2,3,-4])

