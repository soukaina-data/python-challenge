import csv 
import os
# create file path and save as file 
file =os.path.join('Ressources','election_data.csv')

condidate = []
total_vote_cast = 0
number_vote=[]

with open(file ,'r') as csvfile:
    csvread = csv.reader(csvfile)
for row in csvread:
        number_vote=[].append(row[0])
        candidate.append((row[2]))
#find The total number of votes cast
    number_vote=[]= len(vote_cast)
    Total_vote_cast += vote_cast[r]

#A complete list of candidates who received votes
    condidate = len(candidate_liste)
for r in range(len(candidate_liste)):
if candidate in candidates:
   candidate = candidate then 
   vote_cast[candidate]=vote_cast[candidate]+1

#The percentage of votes each candidate won
    percentage =[]
    maxvote = number_vote=[]
    maxvote = 0
 for r in range(len(candidate_liste)):  
    percentage_vote = (vote_cast/total_vote_cast)*100
     percentages.append(vote_percentage)
   
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]
#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {num_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")


  
    

