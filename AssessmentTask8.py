from collections import Counter
myString = 'To understand the need for creating a class let us consider an example: Let\
uss say that you wanted to track the number of dogs which may have different attributes\
like breed, and age. If a list is used, the first element could be the dog’s breed while the\
second element could represent its age. Let’s suppose there are 100 different dogs, then\
how would you know which element is supposed to be which? What if you wanted to add\
other properties to these dogs? This lacks organization and it’s the exact need for classes.'

str = dict(Counter(myString.split()))
strmostcommon = Counter(myString.split())
print(str)
print(strmostcommon.most_common(5))
print(f'There are {len(str)} words in the sentence.')
print(str)
print(str['the'])




