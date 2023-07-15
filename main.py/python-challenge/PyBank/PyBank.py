print("Finacial Analysis")
print('-------------------------')

import os
import csv


    
#Creating path for csv:
path = "Resources"
file_name= 'budget_data.csv'
file_path= os.path.join(path,file_name)
#Reads csv:
with open (file_path) as file:
    csvreader = csv.reader(file, delimiter=',')
    csv_header = next(csvreader)

# Empty lists to add csv values
    month = []
    profit = []
    change = []
    
#Ensures all values are accounted for and can be referenced later.   
    for row in csvreader:
        month.append(row[0])
        profit.append(int(row[1]))
    for x in range(len(profit)-1):
        change.append(profit[x+1]-profit[x])

#Analyze list for max and min values
increase = max(change)
decrease = min(change)

#According to the index:
month_increase = change.index(max(change))+1
month_decrease = change.index(min(change))+1

#Analyzing and printing data
print(f"Total Months: {len(month)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: ${round(sum(change)/len(change),2)}")
print(f"Greatest Increase in Profits: {month[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month[month_decrease]} (${(str(decrease))})")


