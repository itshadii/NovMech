# importing csv module
import csv

x= input("Please Enter file name:" )
filename = x+'.csv'
try:
    x=open(x+'.csv')
except:
    print('can not be found', x)
    exit()
fn=filename[:8]
# initializing the titles and rows list
fields = []
rows = []
lst =[]
# reading csv file
with open(filename, 'r') as csvfile:
	# creating a csv reader object
	csvreader = csv.reader(csvfile)
	# extracting field names through first row
	fields = next(csvreader)
	# extracting each data row one by one
    # Removing blanks
	for row in csvreader:
         while '' in row:
            row.remove('')
         rows.append(row)
# Creating CSV file
with open(fn+" Arena Ready.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Level", "item_number","quantity"])
    writer.writerow([0,fn,1])
    for row in rows:
        writer.writerow([1,row[1],row[-1]])
