#put modules in
import os
import csv

#create paths to resources 
csvpath = os.path.join('Resources','budget_data.csv')
file = open("PyBank_results.txt","w")

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
    file.write(f"Total Months: {Months}\n")
    print(f'Total: ${Total}')
    file.write(f'Total: ${Total}\n')
#Net total of Profit/Loss over the whole period

    
#Changes in Profit/Loss  over the entire 
    change1=[] #this is the rate of change between the months
    for x in range(len(change)):
        if x != 0:
            # change1.append(change[x])
            change1.append(change[x]-change[x-1])

    # print(sum(change1)) #--------used to help debug
    print(f'Average change: ${round(sum(change1)/len(change1), 2)}')
    file.write(f'Average change: ${round(sum(change1)/len(change1), 2)}\n')
    #average of those changes

#Find the greatest increase in profit over the whole period
    increase = 0
    highROC = 0
    for x in range(len(change)):
        if (change[x] - change[x-1]) > increase:  
            increase = (change[x] - change[x-1])
            highROC = x
    # print(increase) #--------used to help debug       
    print(f'Greatest Increase in Profits: {date[highROC]} (${increase})')
    file.write(f'Greatest Increase in Profits: {date[highROC]} (${increase})\n')
    #amount

#Find the greatest decrease in losses over the whole period
    decrease = 0
    lowROC = 0
    for x in range(len(change)):
        if (change[x] - change[x-1]) < decrease:  
            decrease = (change[x] - change[x-1])
            lowROC = x
    print(f'Greatest Decrease in Profits: {date[lowROC]} (${decrease})')
    file.write(f'Greatest Decrease in Profits: {date[lowROC]} (${decrease})\n')
    
file.close()
#Print the analysis to the terminal()

#Export a text file with the results


