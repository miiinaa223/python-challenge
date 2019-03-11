import os
import csv


# Identifies file with poll data
file = os.path.join("/Users/miiinaa223/Desktop/NUCHI201902DATA3/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")

# Creates dictionary to put candidates name and vote counts
election = {}
# set total votes starts 0
votes_total = 0

# read csv
with open(file, newline="") as csvfile:
    csvread = csv.reader(csvfile,delimiter=",")
    

    # skips header
    next(csvread, None)

    # counts votes by candidates
    for row in csvread: # can pull the data in csv by row
        votes_total += 1
        if row[2] in election.keys(): # .keys() is the method to pull keys from the dictionary. e.g If we already counted Khan in the dictionary ..
            election[row[2]] = election[row[2]] + 1 # count votes
        else:
            election[row[2]] = 1 # e.g If Khan does not include in the dictionary yet, starts from 1.
 
#create empty list for candidates and their counts
candidates = []
votes = []

# put their keys (candidates) and their values (votes) in to the dictionary
for key, value in election.items():
    candidates.append(key) # show the names
    votes.append(value) # show the number of their votes

# creates vote percent list
vote_percentage = []
for i in votes:
    vote_percentage.append(i/votes_total*100)

# create new list with zip
summary_list = list(zip(candidates, votes, vote_percentage)) # zip: gets more than one elements at that same time

#creates winner_list 
winner_list = []

for candidates in summary_list:
    if max(votes) == candidates[1]:
        winner_list.append(candidates[0])

# makes winner_list a str with the first entry
winner = winner_list[0]

#prints to file
filename = "PyPoll.txt"
with open(filename, 'w') as txtwrite:
    txtwrite.write('\n')

# output
print('Election Results \n------------------------- \nTotal Votes: ' + str(votes_total) + 
      '\n-------------------------')
for entry in summary_list:
    print(entry[0] + ': ' + str(round(entry[2],1)) +'%  (' + str(entry[1]) + ')')

print('------------------------- \nWinner: ' + winner + '\n-------------------------')