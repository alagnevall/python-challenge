#put modules in
import os
import csv

#create paths to resources 
csvpath = os.path.join('Resources','budget_data.csv')

#variable for total number of months
Months = 0
Total =0
change = []
date = []
with open(csvpath) as csvfile:
    next(csvfile)
    csvreader = csv.reader(csvfile, delimiter="," )
    
#find total amount of months
    for month in csvreader:
        Months += 1
        Total += int(month[1])
        change.append(int(month[1]))
        date.append(month[0])

    print(f"Total Months: {Months}")
    print(f'Total: ${Total}')
#Net total of Profit/Loss over the whole period

    
#Changes in Profit/Loss  over the entire period
    print(f'Average change: ${round((change[0]-change[-1])/Months, 2)}')

    #average of those changes

#Find the greatest increase in profit over the whole period
    print(f'Greatest Increase in Profits: {date[change.index(max(change))]} (${max(change)})')
    #amount

#Find the greatest decrease in losses over the whole period
    print(f'Greatest Decrease in Profits: {date[change.index(min(change))]} (${min(change)})')
    #date
    #amount

#Print the analysis to the terminal()

#Export a text file with the results


