print("Number 1: Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is "
      "equal to 100.25. \n")
x = 25 * 10 / (5 ** 2) + 100 - 9.75
print("The equation is 25 * 10 / (5 ** 2) + 100 - 9.75 =", x)
print("\n")
print("Number 2: ")

xx = 4 * (6 + 5)
y = 4 * 6 + 5
z = 4 + 6 * 5

print(xx, y, z)

print("\nNumber 3: What is the type of the result of the expression")
num3 = 3 + 1.5 + 4
print(num3, "therefore the result is a float", "\n")

print("Number 4 and 5: What would you use to find the numbers square root as well as its square?")
print("Square root use this 16 ** (0.5) =", 16 ** 0.5)
print("Square use this 4**2 =", 4**2, "\n")

print("Number 6: in the word hello print e using indexing")
word = "hello"
print(word[1], "\n")

print("Number 7: Reverse the string hello using slicing")
print(word[::-1], "\n")

print("Number 8: Give two methods to produce letter o using indexing")
print(word[4])
print(word[-1], "\n")

print("Number 9 : build thsi list tw o separate ways [0,0,0]")
list1 = [0, 0, 0]
list2 = list1
print(list1)
print(list2, "\n")

print("Number 10: replace hello with goodbye")
list3 = [1, 2, [3, 4, 'hello']]
print("old list 3 value: ", list3)
list3[2].pop(2)
list3[2].append("goodbye")
print("new list 3 value: ", list3, "\n")

print("Number 11: Sort the list below")
list4 = [5, 3, 4, 6, 1]
print("list unsorted value: ", list4)
list4.sort()
print("list sorted value: ", list4, "\n")

print("Number 12: using keys and indexing gran the 'hello' from the dictionaries")
dict1 = {'simple_key': 'hello'}
dict1['simple_key']
print(dict1['simple_key'])

dict2 = {'k1': {'k2': 'hello'}}
dict2['k1']['k2']
print(dict2['k1']['k2'])

dict3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
dict3['k1'][0]['nest_key'][1]
print(dict3['k1'][0]['nest_key'][1])

dict4 = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
dict4['k1'][2]['k2'][1]['tough'][2]
print(dict4['k1'][2]['k2'][1]['tough'][2], "\n")

print("Number 13: Can you sort a dictionary?")
print("No, because dictionaries are orderless and they are not sequences unlike tuples and lists", "\n")

print("Number 14: What is the difference between tuples and lists?")
print("Tuples are immutable which means that tuples values cannot be changed while lists are immutable", "\n")

print("Number 15: How do you create a tuple?")
print("Tuples can be created using parenthesis", "\n")

print("Number 16: What is unique about sets?")
print("There is no repetition of values in sets", "\n")

print("Number 17: Use a set to find unique values of the list below")
list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
print("Here is the value of list5", list5)
set1 = set(list5)
print("Here is list5 converted to a set", set1, "\n")

#2.4
print("Number 18: Is it true or false")

# false
2 > 3
print("2 > 3 = ", 2 > 3)

# false
3 <= 2
print("3 <= 2", 3 <= 2)

#false
3 == 2.0
print("3 == 2.0", 3 == 2.0)

#true
3.0 == 3
print("3.0 == 3", 3.0 == 3)

#false
4**0.5 != 2
print("4**0.5 != 2", 4**0.5 != 2)

print("What is the boolean output of the cell block below?")

l_one = [1, 2, [3, 4]]
l_two = [1, 2, {'k1': 4}]
# false 3 >= 4
l_one[2][0] >= l_two[2]['k1']
print("l_one[2][0] >= l_two[2]['k1'] or 3 >= 4", l_one[2][0] >= l_two[2]['k1'])





