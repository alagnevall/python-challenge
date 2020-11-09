#put modules in
import os
import csv

#create paths to resources 
csvpath = os.path.join('Resources','election_data.csv')
total = 0

with open(csvpath) as csvfile:

    #pass the header row
    next(csvfile)
    csvreader = csv.reader(csvfile, delimiter="," )

#create an empty lists for candidate options. 1 without duplicates and 1 full list
    candidate = []
    candidate2 =[]

#create for loop to grab total votes
    for row in csvreader:
        total += 1 #this is the same as total = total + 1

        #get rid of the duplicate candidates and append into empty list
        if row[2] not in candidate:
            candidate.append(row[2])

        #full list of candidates to tally up votes    
        candidate2.append(row[2])  

    #print the total amount of votes      
    print("-"*30)        
    print(f'Total amount of vote: {total}')
    print("-"*30)   

#create for loop to calculate percentage of votes and the total amount of votes using the f function
    for name in candidate:
        print(f'{name}: {round((candidate2.count(name)/total)*100, 2)}%  ({candidate2.count(name)})')  

#print the winner but finding the most commonly used variable in the full list       
    print("-"*30) 
    print(f'Winner is: {max(set(candidate2), key=candidate2.count)}')
    print("-"*30) 
  
  







