import csv
import os

#assign variable to load a file
file_to_load = os.path.join("resources","election_results.csv")
#assign variable to save a file
file_to_save = os.path.join("analysis","election_analysis.txt")

#total votes counter
total_votes = 0
#list each candidate
candidates_options = []
#lists each candidate and their votes
candidate_votes = {}
#winning candidate variable
winning_candidate = ""
#winning number of votes
winning_count = 0
#winning percentage
winning_percentage = 0

#opens election results
with open(file_to_load) as election_data:
    #reads election results
    file_reader = csv.reader(election_data)
    
    #reads headers and removes row from file_reader
    headers = next(file_reader)
    
    #goes through all rows in file
    for row in file_reader:
        #sums rows to get total votes
        total_votes += 1
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

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #goes through each candidate
    for candidate_name in candidate_votes:
        #gets # of votes for candidate
        votes = candidate_votes[candidate_name]
        # calculates vote percentage
        vote_percentage = float(votes) / float(total_votes) * 100

        #prints each candidate's name, vote count, and vote percentage
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)

        #saves candidate results to text file
        txt_file.write(candidate_results)
        
        #determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        
    #prints winning candidate's results
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)

    #saves winning candidate's results to text file
    txt_file.write(winning_candidate_summary)