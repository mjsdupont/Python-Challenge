import csv
import os.path

# Initialize variables
total_months = 0
net_total = 0
prev_profit_loss = 0
profit_loss_delta = []
dates = []

userhome = os.path.expanduser('~')
csvfile = os.path.join(userhome, 'Desktop', 'Python-Challenge', 'PyBank', 'Resources', 'budget_data.csv')
txt_file = os.path.join(userhome, 'Desktop', 'Python-Challenge', 'PyBank', 'Analysis', 'Financial_Analysis.txt')

# open csv file
with open(csvfile, newline='') as file: 
    pybankreader = csv.reader (file, delimiter= ",")

    # Skip the header row
    header = next(pybankreader)

    # Loop csv file
    for row in pybankreader: 
        # Extract date and profit losses and values 
        date = row[0]
        profit_loss= int(row[1])

        # Count total number of months
        total_months = total_months + 1

        # Calculate the net total amount
        net_total = net_total + profit_loss
        
        # Calculate changes in profit and losses
        if total_months > 1:
            change = profit_loss - prev_profit_loss 
            profit_loss_delta.append(change)
            dates.append(date)

        # Update previous profit and losses for the next iteration
        prev_profit_loss = profit_loss

    # Calculate the average change in profit and losses
    average_change = sum(profit_loss_delta) / (total_months - 1)
    
    # Calculate the greatest increase in profits (date and amount)
    greatest_increase = max(profit_loss_delta)
    greatest_increase_date = dates[profit_loss_delta.index(greatest_increase)]

    # Calculate the greatest decrease in profits (date and amount)
    greatest_decrease = min(profit_loss_delta)
    greatest_decrease_date = dates[profit_loss_delta.index(greatest_decrease)]

# Print the analysis results
print("Financial Anlysis")
print("----------------------")
print("Total Months: " , total_months)
print("Total: " , net_total)
print("Average Change: " , "$" , "{:.2f}".format(average_change))
print("Greatest Increase in Profits: " , greatest_increase_date , " $" , "(" , greatest_increase , ")")
print("Greatest Decrease in Profits: " , greatest_decrease_date , " $" , "(" , greatest_decrease , ")")

# Save the analysis results to a text file
with open(txt_file, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${net_total}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")