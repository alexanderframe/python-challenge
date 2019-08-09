#!/usr/bin/env python
# coding: utf-8

# In[21]:


import os
import csv

pyPollPath = os.path.join('Resources', 'election_data.csv')
outputPath = os.path.join('afPyPollOutput.txt')


# In[22]:


totalVotes = 0

# create list for candidate options an dict for candidate vote counters
candidates = []
candidateVotes = {}

# variables for winning candidate and winning vote count
winner = ''
winningCount = 0


# In[23]:


with open(pyPollPath, 'r') as pollData:
    csvReader = csv.DictReader(pollData, delimiter=',')
    
    for row in csvReader:
        
        # add one to the total votes tally for each row
        totalVotes += 1
        candidateName = row['Candidate']
        
        # add candidate if not in list already
        if candidateName not in candidates:
            candidates.append(candidateName)
            candidateVotes[candidateName] = 0
         
        # add one vote to individual candidate vote tally
        candidateVotes[candidateName] += 1


# In[24]:


# print the results and export the data
with open(outputPath, 'w') as txtFile:
    electionResults = (
        'Election Results \n'
        '------------------- \n'
        f'Total Votes: {totalVotes} \n'
        '------------------- \n'
    )
    
    print(electionResults)
    txtFile.write(electionResults)

    # get vote count for each candidate and print results
    for candidate in candidateVotes:
        votes = candidateVotes.get(candidate)
        votePercentage = round(((votes / totalVotes) * 100), 3)
        candidateOutput = f'{candidate}: {votePercentage}% ({votes}) \n'
        
        print(candidateOutput)
        txtFile.write(candidateOutput)
        
        #find winner
        if votes > winningCount:
            winningCount = votes
            winner = candidate
            
    # print winning results
    winningResults = (
        '------------------- \n'
        f'Winner: {winner} \n'
        '------------------- \n'
    )
    
    print(winningResults)
    txtFile.write(winningResults)
        
    


# In[ ]:




