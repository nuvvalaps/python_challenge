import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvfile)

    row = 0
    total_months = 0
    months = []
    net_total = 0
    daily_changes = []
    average_change = 0
    greatest_increase_value = 0
    greatest_increase_month = ''
    greatest_decrease_value = 0
    greatest_decrease_month = ''
    previous_day = 0

    for x in csvreader:
        row = row + 1
        # Calculate the total number of months in the dataset
        if x not in months:
            months.append(x[0])
            total_months = total_months + 1
       # Calculate the net total amount of "Profit/Loss" over the entire time period
        net_total = net_total + int(x[1])
        # Calculate the daily change in value from the previous day
        change = int(x[1]) - previous_day
        daily_changes.append(change)
        previous_day = int(x[1])
       # Calculate the average of all daily changes over the entire time period
        average_change = sum(daily_changes)/row
        # Use a conditional statement to find the greatest individual increase and decrease
        if int(x[1]) > 0:
            if int(x[1]) > greatest_increase_value:
                greatest_increase_value = int(x[1])
                greatest_increase_month = x[0]
        elif int(x[1]) < 0:
            if int(x[1]) < greatest_decrease_value:
                greatest_decrease_value = int(x[1])
                greatest_decrease_month = x[0]

            
    # Print results to terminal
    print(f"Financial Analysis")
    print(f"Total Months: {total_months}")
    print(f"Net Profit/Loss: ${net_total}")
    print(f"Average Daily Change: ${round(average_change,2)}")
    print(f"Greatest Daily Profit: {greatest_increase_month} (${greatest_increase_value})")
    print(f"Greatest Daily Loss: {greatest_decrease_month} (${greatest_decrease_value})")

# Export Results to Txt File
output_path = os.path.join('Analysis', 'financial_analysis.txt')
output_results = open(output_path, 'w')
output_results.write(f"Financial Analysis \n")
output_results.write(f"Total Months: {total_months} \n")
output_results.write(f"Net Profit/Loss: ${net_total} \n")
output_results.write(f"Average Daily Change: ${round(average_change,2)} \n")
output_results.write(f"Greatest Daily Profit: {greatest_increase_month} (${greatest_increase_value}) \n")
output_results.write(f"Greatest Daily Loss: {greatest_decrease_month} (${greatest_decrease_value}) \n")
output_results.close()

    



    
    
