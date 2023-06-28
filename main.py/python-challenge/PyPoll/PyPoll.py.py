import os
import csv
import collections 
import sys                                                                
#opening csv file:
path = "C://Users//kayvb//OneDrive//Desktop//main.py//python-challenge//PyPoll//Resources"
file_name = 'election_data.csv'
file_path = os.path.join(path, file_name)
with open (file_path) as file:            
            csvreader = csv.DictReader(file, delimiter = ',')  #itrating csv file into a dict
            csv_header = next(csvreader)

            #Creating dict and values:
            counts = {
                'Charles Casper Stockham': 0,
                    'Diana DeGette': 0,
                    'Raymon Anthony Doane': 0
                    }
                

        #adding count to analyze data: 
            for line in csvreader:
                counts[line['Candidate']] +=1

#Equations for data analysis:
total = counts['Charles Casper Stockham']+ counts['Diana DeGette'] + counts['Raymon Anthony Doane']

pct0 = (counts['Charles Casper Stockham']/ total)*100
pct0 = round(pct0, 3)

pct1 = (counts['Diana DeGette']/ total)*100
pct1 = round(pct1, 3)

pct2 = (counts['Raymon Anthony Doane']/ total)*100
pct2 = round(pct2, 3)

#creating a function to analyze winner:
def winner(file):
    #opening csv file
    with open("C://Users//kayvb//OneDrive//Desktop//main.py//python-challenge//PyPoll//Resources//election_data.csv", 'r') as file:
    #iterating over csv 
        reader = csv.reader(file)
        #creating list for canidiates
        winner = []
        #Reading over column 
        for row in reader:
            winner.append(row[2])
        #Defining function for winner analysis:
        winner_count = collections.Counter(winner)
        return winner_count.most_common(1)[0][0]

#Printing results
print("Election Results")
print('-------------------------')
print("Total Votes:", total)
print('-------------------------')
print(f"Charles Casper Stockham:  {pct0}% ({(counts['Charles Casper Stockham'])})")
print(f"Diana DeGette: {pct1}% ({(counts['Diana DeGette'])})")
print(f"Raymon Anthony Doane: {pct2}% ({(counts['Raymon Anthony Doane'])})")
print('-------------------------') 
print("Winner:", winner("election_data.csv"))           
print('-------------------------')

#Open a text file to store results.
sys.stdout=open ('pypoll.txt', 'wt')
  
print("Election Results")
print('-------------------------')
print("Total Votes:", total)
print('-------------------------')
print(f"Charles Casper Stockham:  {pct0}% ({(counts['Charles Casper Stockham'])})")
print(f"Diana DeGette: {pct1}% ({(counts['Diana DeGette'])})")
print(f"Raymon Anthony Doane: {pct2}% ({(counts['Raymon Anthony Doane'])})")
print('-------------------------')
print("Winner:", winner("election_data.csv"))
print('-------------------------')
    


