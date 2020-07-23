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

#opens election results and reads file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #reads headers and removes row from file_reader
    headers = next(file_reader)
    
    #counts each row
    for row in file_reader:
        total_votes +=1

print(total_votes)

