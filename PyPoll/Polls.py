import csv
import os

election_csv = os.path.join("PyPoll", "election_data.csv")
analysis_output = os.path.join("PyPoll", "election_analysis.txt")

vote_counter = 0

candidate_options = []
candidate_votes = {}
candidate_percent = {}

winning_candidate = ""
winning_count = 0

with open(election_csv) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)

    for row in reader:
        vote_counter = vote_counter + 1

        candidate_name = str(row[2])

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open(analysis_output, "w") as txt_file:
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {vote_counter}\n"
        f"-------------------------\n")
    print(election_results)
    txt_file.write(election_results)

    for candidate in candidate_options:
        votes = candidate_votes.get(candidate)
        vote_percent = float(votes) / float(vote_counter) * 100

        votes_output = ('{}: {:.3f}% ({})\n'.format(candidate,vote_percent,votes))
        print(votes_output) 
        txt_file.write(votes_output)

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
    winner_results = (
        f"-------------------------\n"
        f"Winner : {winning_candidate}\n"
        f"-------------------------\n")
    print(winner_results)
    txt_file.write(winner_results)