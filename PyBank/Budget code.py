import csv
import os
Budget_csv = os.path.join("PyBank","budget_data.csv")
analysis_txt = os.path.join("PyBank","budget_analysis.txt")

total_months = 0
total_money = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999]


with open(Budget_csv) as budget_data:
    reader = csv.reader(budget_data)

    header = next(reader)

    first_row = next(reader)
    total_months = total_months + 1
    total_money = total_money + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        total_months = total_months + 1
        total_money = total_money + int(row[1])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

net_monthly_avg = sum(net_change_list) / len(net_change_list)

output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_money}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)

with open(analysis_txt, "w") as txt_file:
    txt_file.write(output)