print("Assessment Task 3 \n")
print("Number 1: Print out words that starts with letter 's' \n")

st = "Print out the words that starts with s in this sentence"

for word in st.split():
    if word[0] == "s":
        print(word)
print("\n")

print("Number 2: Use range to print all even numbers from 0 to 10 \n")

for x in range(0, 11):
    if x % 2 == 0:
        print(x)
print("\n")

print("Number 3: If the length of the word is even then print even \n")
st1 = "Print every word in this sentence that has an even number of letters"

for word in st1.split():
    if len(word) % 2 == 0:
        print(word)
print("\n")

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)

print("\n")
