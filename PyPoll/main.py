import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv) as csvfile:
    csvreader =  csv.reader(csvfile, delimiter=",")
    
    csvheader = next(csvreader)
    data = list(csvreader)

    total_votes = len(data)
    candidate_list= []
    stockham_votes = 0
    degette_votes  = 0
    doane_votes = 0

    for row in data:
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
    
    for row in data:
        if row[2] == str("Charles Casper Stockham"):
            stockham_votes = stockham_votes + 1
        elif row[2] == str("Diana DeGette"):
            degette_votes = degette_votes + 1
        else:
            doane_votes = doane_votes + 1

    stockham_percent = stockham_votes / total_votes
    degette_percent = degette_votes / total_votes
    doane_percent = doane_votes / total_votes

    votes_list = [stockham_votes, degette_votes, doane_votes]
    winner = votes_list.index(max(votes_list))

    print(
        "Election Results\n"
        "-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    print(f"Charles Casper Stockham: {stockham_percent:.3%} ({stockham_votes})")
    print(f"Diana DeGette: {degette_percent:.3%} ({degette_votes})")
    print(f"Raymon Anthony Doane: {doane_percent:.3%} ({doane_votes})")
    print("-------------------------")
    print(f"Winner: {candidate_list[winner]}")
    print("-------------------------")

output_file = os.path.join("Analysis","election_data.txt")

with open(output_file, "w") as txtfile:
    writer = csv.writer(txtfile)

    txtfile.write(
        "Election Results\n"
        "-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Charles Casper Stockham: {stockham_percent:.3%} ({stockham_votes})\n")
    txtfile.write(f"Diana DeGette: {degette_percent:.3%} ({degette_votes})\n")
    txtfile.write(f"Raymon Anthony Doane: {doane_percent:.3%} ({doane_votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {candidate_list[winner]}\n")
    txtfile.write("-------------------------")