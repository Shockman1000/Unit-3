import csv
import os
Budget_csv = os.path.join("Resources", "budget_data.csv")
txt_file = os.path.join("analysis", "budget_analysis.txt")

month_year_list = []
revenue_list = []
tot_revenue = 0
tot_change = 0
change_max = ['', 0]
change_min = ['', 0]


with open(Budget_csv) as file_in:
    reader = csv.reader(file_in)
    next(reader)
    for row in reader:
        month_year = row[0]
        revenue = float(row[1])
        month_year_list.append(month_year)
        revenue_list.append(revenue)
        tot_revenue += revenue

    tot_month = len(month_year_list)
    for i in range(1, len(month_year_list)):
        change = revenue_list[i] - revenue_list[i-1]
        tot_change += change
        if change > change_max[1]:
            change_max = [month_year_list[i], change]
        if change < change_min[1]:
            change_min = [month_year_list[i], change]
    change_average = tot_change / tot_month

output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {tot_month}\n"
    f"Total: ${tot_revenue}\n"
    f"Average  Change: ${change_average:.2f}\n"
    f"Greatest Increase in Profits: {change_max[0]} (${change_max[1]})\n"
    f"Greatest Decrease in Profits: {change_min[0]} (${change_min[1]})\n")

print(output)

with open(analysis_txt, "w") as txt_file:
    txt_file.write(output)