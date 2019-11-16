import csv
import os
# create file path and save as file
file =os.path.join('Resources','election_data.csv')
file_to_output = "election_poll.txt"
# condidate = []
candidate = []
total_vote_cast = 0
# number_vote=[]
candidate_votes = {}
winner_count = 0
with open(file ,'r') as csvfile:
    csvread = csv.reader(csvfile)
    header = next(csvread)
    for row in csvread:
        candidate_name = row[2]
        if candidate_name not in candidate:
            candidate.append(candidate_name)
            candidate_votes[candidate_name] = 0
        # number_vote=[].append(row[0])
        # candidate.append((row[2]))
    #find The total number of votes cast
        # number_vote=[]= len(vote_cast)
        # Total_vote_cast += vote_cast[r]
        total_vote_cast = total_vote_cast + 1
    #A complete list of candidates who received votes
        # condidate = len(candidate_liste)
    # for r in range(len(candidate_list)):
    # if candidate in candidates:
    #    candidate = candidate then
    #    vote_cast[candidate]=vote_cast[candidate]+1
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
results = []
results.append("\n")
results.append("Election Results")
results.append("=====================")
results.append(f"Total Votes: {total_vote_cast}")
results.append("=====================")
results.append("")
#The percentage of votes each candidate won
#     percentage =[]
#     maxvote = number_vote=[]
#     maxvote = 0
#  for r in range(len(candidate_liste)):
#     percentage_vote = (vote_cast/total_vote_cast)*100
#      percentages.append(vote_percentage)
#     if vote_counts[count] > max_votes:
#         max_votes = vote_counts[count]
#         print(max_votes)
#         max_index = count
# winner = candidates[max_index]
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    percentage = (votes / total_vote_cast) * 100
    if votes > winner_count:
        winner_count = votes
        winner = candidate
    results.append(f"{candidate}: {percentage:.0f}% ({votes})")
# #print results
# print("Election Results")
# print("--------------------------")
# print(f"Total Votes: {num_votes}")
# for count in range(len(candidates)):
#     print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
# print("---------------------------")
# print(f"Winner: {winner}")
# print("---------------------------")
results.append("")
results.append("=====================")
results.append(f"Winner: {winner}")
results.append("=====================")
results = "\n".join(results)
print(results)
with open(file_to_output, "w") as txt_file:
    txt_file.write(results)