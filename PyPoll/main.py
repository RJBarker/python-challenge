# import os for file path
import os

# import csv for reading and interacting of csv file
import csv

# set the file path
datapath = os.path.join("Resources","election_data.csv")

# open the file
with open(datapath, 'r') as datafile:

    # create var for contents and set delimiter
    datareader = csv.reader(datafile, delimiter=",")

    # store the header row
    data_header = next(datareader)

    # Set initial var
    vote_count = 0      # Stores the count of votes
    cand = {}           # Dict to store Candidate names

    ## Get candidates
    for row in datareader:
        
        ## For each row + 1 to the vote_count variable
        vote_count += 1

        ## Check if candidate name is in the cand dict, if not add it with a count value of 1
        ## If it is already in the dict then +1 to the count
        # This concise code was used from: https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
        if row[2] not in cand:
            cand.update({row[2] : 1})
        else: cand[row[2]] += 1

    ## Once all votes counted. Calculate the percentage for each candidate
    # Create a function to calculate the percentage and call this function when required
    def percent(number):
        return round(float((number / vote_count) * 100),3)


## Print results to the terminal
print()
print("Election Results")
print("-------------------------")
print(f"Total Votes: {vote_count}")
print("-------------------------")
## Loop through the cand dict to print the candidate name, their % of votes using the function created, and their total vote count
## Use an if statement to evaluate the number of votes a candidate received. If greater than the max_votes var, store the vote count and cand_name in the winner variable
max_votes = 0
for cand_name in cand:
    print(f"{cand_name}: {percent(cand[cand_name])}% ({cand[cand_name]})")
    if cand[cand_name] > max_votes:
        max_votes = cand[cand_name]
        winner = cand_name
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


## Write the results to a text file
output_path = os.path.join('Analysis', 'election_results.txt')

with open(output_path, 'w') as txtfile:
    txtfile.write('Election Results\n')
    txtfile.write('----------------------------\n')
    txtfile.write(f'Total Votes: {vote_count}\n')
    txtfile.write('----------------------------\n')
    ## This loop is the same as the terminal, but with the if conditional removed as the winner has already been identified
    for cand_name in cand:
        txtfile.write(f"{cand_name}: {percent(cand[cand_name])}% ({cand[cand_name]})\n")
    txtfile.write('----------------------------\n')
    txtfile.write(f'Winner: {winner}\n')
    txtfile.write('----------------------------\n')
    txtfile.close
# %%
