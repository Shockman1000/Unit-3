import csv
import os

election_csv = os.path.join("PyPoll", "election_data.csv")
analysis_output = os.path.join("PyPoll", "election_analysis.txt")

voter_id = []
candidates = []
candidate_number = {}
winner_vote = 0
results = []
with open(election_csv) as file_in:
    csvreader = csv.DictReader(file_in)
    for row in csvreader:
        candidate = row['Candidate']
        voter_id.append(row['Voter ID'])
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_number[candidate] = 1
        else:
            candidate_number[candidate] += 1
    total_votes = len(voter_id) # total number of votes
    candidate_percentage = {candidate : candidate_number[candidate]/total_votes \
        for candidate in candidates}
    for item in candidate_percentage.items():
        if item[1] > winner_vote:
            winner_vote = item[1]
            winner = item[0]
with open(analysis_output, "w") as txt_file:
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results)
    txt_file.write(election_results)

    for candidate in candidates:
        results.append("{}: ".format(candidate) + \
                        "{:.1%}".format(candidate_percentage[candidate]) + \
                        " ({})".format(candidate_number[candidate])) 
    for line in results:
        print(line)
        txt_file.write(line)
    winner_results = (
        f"-------------------------\n"
        f"Winner : {winner}\n"
        f"-------------------------\n")
    print(winner_results)
    txt_file.write(winner_results)