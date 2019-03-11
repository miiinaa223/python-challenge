import os
import csv

# Set path for file
csvpath = os.path.join("/Users/miiinaa223/Desktop/NUCHI201902DATA3/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv")


# Set the title
print("Financial Analysis")


# Open the csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    # skip header 
    csv_header = next(csvfile)


    # make a new list by row to show [[row1],[row2],[row3]]..
    list_profitloss = list()

    for row in csvreader:
        list_profitloss.append(row)
    
    


# count
count_profitloss = len(list_profitloss)


# total change
# in case, you don't need like int(total_profitloss(row[1])
total_profitloss = 0
for row in list_profitloss:
    total_profitloss = total_profitloss + int(row[1])


# the greatest increase
# [[month0],[value0],[month1],[value1]... value1 - value0 in the case month = value 1 = i + 1
# wo int, python tries to calculate as list which causes an error
greatest_increase_amount = 0
greatest_decrease_amount = 0
total_variance_change = 0
for i in range(count_profitloss-1):
    months_variance = int(list_profitloss[i+1][1]) - int(list_profitloss[i][1])

    if months_variance >= greatest_increase_amount:
        greatest_increase_amount = months_variance # amount
        greatest_increase_month = list_profitloss[i+1][0] # month

    if months_variance < greatest_decrease_amount:
        greatest_decrease_amount = months_variance # amount
        greatest_decrease_month = list_profitloss[i+1][0] # month

    # total variance change *indent matters to show the result of loop?
    total_variance_change = total_variance_change + months_variance

# the average of change * not total average of sum
average_profitloss = total_variance_change/(count_profitloss-1)


#prints to file
filename = "PyBank.txt"
with open(filename, 'w') as txtwrite:
    txtwrite.write('\n')

# output
print("---------------------")
print("Total Months: " + str(count_profitloss))
print("Total: " + str(total_profitloss))
print("Average Change: " + str(average_profitloss))
print("Greatest Increase in Profits: " + str(greatest_increase_month) + " (" + str(greatest_increase_amount) + ")")
print("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " (" + str(greatest_decrease_amount) + ")")