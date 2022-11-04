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


#Here is the shortcut method


def unique_List(yourList):
    setFirst = set(yourList)
    listAgain = list(setFirst)
    print(yourList)
    print(listAgain, "\n")
    pass
unique_List([1,1,1,1,2,2,2,2,3,3,3,4,4,4,5,5,5])

#Here is the manual method

def unique_manual(your_list):
    final_list = []
    for items in your_list:
        if items not in final_list:
           final_list.append(items)
    final_list.sort()
    print(final_list)
    pass

unique_manual([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10])


print("Number 5: Write a python function to multiply all the numbers in a list")
def multiply(numbers):
    product = 1
    for members in numbers:
        product = product * members
    print(product)
    pass
multiply([1,2,3,-4])

print("Number 6: Write a Python function that checks whether a word or phrase is palindrome")


def palindrome(s):
    if s == s[::-1]:
        print(f"{s} is a palindrome \n")
    else:
        print(f"{s} is not a palindrome \n")
    pass


palindrome("natan")

print("Number 7: Pangram")


def pangram(sentence, alphabet=string.ascii_lowercase):
    without_space = sentence.replace(" ", "")
    first_list = []

    for letters in without_space:
        first_list.append(letters)

    final_set = set(first_list)
    alphabet_set = set(alphabet)

    if final_set == alphabet_set:
        print("This is a pangram")
    else:
        print("This is not a pangram")
    pass


pangram("the quick brown fox jumps over the lazy dog")

