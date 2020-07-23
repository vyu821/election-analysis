# Count number of rows
# Go through all rows, looking for unique candidates, put into list
# Divide each candidates votes by total number of votes
# Count all rows that have candidates name, do for each candidate
# Find highest percentage

import csv
import os

#assign variable to load a file
file_to_load = os.path.join("resources","election_results.csv")
#assign variable to save a file
file_to_save = os.path.join("analysis","election_analysis.txt")

total_votes = 0
candidates_options = []
candidate_votes = {}

#opens election results
with open(file_to_load) as election_data:
    #reads election results
    file_reader = csv.reader(election_data)
    
    #reads headers and removes row from file_reader
    headers = next(file_reader)
    
    #goes through all rows in file
    for row in file_reader:
        #sums rows to get total votes
        total_votes +=1
        #gets candidates name
        candidate_name = row[2]

        #only adds unique candidates
        if candidate_name not in candidates_options:
            #adds candidate_name to candidate_options
            candidates_options.append(candidate_name)
            #creates each candidate as a key, set each value to 0 to start counter
            candidate_votes[candidate_name] = 0
        
        #adds a vote to candidate's count
        candidate_votes[candidate_name] += 1

print(candidate_votes)

