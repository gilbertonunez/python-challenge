import os
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')

months = []
totalnet = []
changes = []
previous_row = 0

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvfile)

    for row in csvreader:
        months.append(row[0])

        totalnet.append(int(row[1]))

        changes.append(int(row[1]) - previous_row)
        previous_row = int(row[1])

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {len(months)}')
print(f"Total: ${sum(totalnet)}")

changes.pop(0)

average_changes = sum(changes) / (len(months) - 1)
average_changes = "{:.2f}".format(average_changes)
print(f"Average change ${average_changes}")

max_date = months[changes.index(max(changes)) + 1]
min_date = months[changes.index(min(changes)) + 1]
print(f"Greatest Increase in Profits: {max_date} (${max(changes)})")
print(f"Greatest Decrease in Profits: {min_date} (${min(changes)})")

output_file = os.path.join('Analysis',"budget.txt")

with open(output_file, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {len(months)}\n")
    txtfile.write(f"Total: ${sum(totalnet)}\n")
    txtfile.write(f"Average change: ${average_changes}\n")
    txtfile.write(f"Greatest Increase in Profits: {max_date} (${max(changes)})\n")
    txtfile.write(f"Greatest Decrease in Profits: {min_date} (${min(changes)})\n")
