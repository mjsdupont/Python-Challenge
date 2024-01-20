import csv
import os.path

userhome = os.path.expanduser('~')
csvfile = os.path.join(userhome, 'Desktop', 'Python-Challenge', 'PyPoll', 'Resources', 'election_data.csv')
txt_file = os.path.join(userhome, 'Desktop', 'Python-Challenge', 'PyPoll', 'Analysis', 'Election_Results.txt')

# Read the csv file and store the data in a list
with open(csvfile, newline= '') as file: 
    lines = file.readlines()

    # Extract header and data
    header = lines[0].strip().split(",")
    data = [line.strip().split(",") for line in lines [1:]]

    # Calculate the total number of votes cast 
    total_votes = len(data)

    # Store candidate votes
    candidate_votes = {}

    # Count votes for each candidate
    for row in data:
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1 
        else:
            candidate_votes[candidate] = 1 
        
    # Calculate the percentage of votes each candidate won
    percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

    # Find the winner of the election based on popular vote
    winner = max(candidate_votes, key = candidate_votes.get)

# Print the analysis results
print("Election Results")
print("-" * 30)
print(f"Total Votes: {total_votes}")
print("-" * 30)

for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {percentages[candidate]:.3f}% ({votes})")

print("-" * 30)
print(f"Winner: {winner}")
print("-" * 30)

# Save the analysis results to a text file
with open(txt_file, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-" * 30)
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-" * 30)

    for candidate, votes in candidate_votes.items():
        txt_file.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n")

    txt_file.write("-" * 30)
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-" * 30)