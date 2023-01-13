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

#datetime
import datetime
t1 = datetime.time(4, 20, 1)
t2 = datetime.time(6, 20, 1)
print(t1)
print("hour :", t1.hour)
print("minute:", t1.minute)
print("second :", t1.second)
print("microsecond :", t1.microsecond)
print("tzinfo :", t1.tzinfo)

#timedelta
import datetime
t1 = datetime.time(8,0,0) 
print('Start time.... ', t1)
t2 = datetime.time(12,0,0) 
print('End time.... ', t2)
dt1 = datetime.timedelta(hours=t1.hour, minutes=t1.minute, seconds=t1.second, microseconds=t1.microsecond)
dt2 = datetime.timedelta(hours=t2.hour, minutes=t2.minute, seconds=t2.second, microseconds=t2.microsecond)

print('Time Difference... ', dt2-dt1)

#Voting Shit
from collections import Counter

class Candidate(object):
    # class attribute
    votes = []
    def __init__(self, name, position):
        # constructor/initialization of class Candidate
        self.name = name
        self.position = position

    def setVotes(self, vote):
        # method to set votes data
        self.votes.append(vote)

    def getVotes(self):
        # method to get votes data
        return self.votes

    def dispCandid(self):
        # method for interface
        print(f"Name: {self.name}\nPosition: {self.position}")

# instantiate objects of Candidates
candi1 = Candidate("John Doe", "President")
candi2 = Candidate("Jane Smith", "Vice President")
candi3 = Candidate("Bob Johnson", "Secretary")

# display candidate information
candi1.dispCandid()
candi2.dispCandid()
candi3.dispCandid()

for x in range(10):
    voteCast = int(input('Enter code to cast your vote: '))
    # set vote
    candi1.setVotes(voteCast)
    # get vote
print(candi1.getVotes())

# create a dictionary of votes
d = dict(Counter(Candidate.votes))

# display the results
for key, value in d.items():
    print(f"Candidate {key} received {value} votes.")
