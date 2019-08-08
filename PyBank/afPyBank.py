import os
import csv

pyBankPath = os.path.join('Resources', 'budget_data.csv')
outputPath = os.path.join('afPyBankOutput.txt')

totalMonths = 0
totalPL = 0
plChange = 0
previousPL = 0
greatestIncrease = 0
greatestDecrease = 0

with open(pyBankPath, 'r') as budgetData:
    csvReader = csv.DictReader(budgetData, delimiter=',')
    for row in csvReader:
        totalMonths += 1
        totalPL += int(row['Profit/Losses'])
        
        plChange = int(row['Profit/Losses']) - previousPL
        previousPL = int(row['Profit/Losses'])
        
        if plChange > greatestIncrease:
            greatestIncrease = plChange
            greatestMonth = row['Date']
        elif plChange < greatestDecrease:
            greatestDecrease = plChange
            leastMonth = row['Date']
            
    averageChange = round((totalPL/totalMonths), 2)


output = (
'Financial Analysis \n'
'-------------------- \n'
f'Total Months: {totalMonths} \n'
f'Total: ${totalPL} \n'
f'Average Change: ${averageChange} \n'
f'Greatest Increase in Profits: {greatestMonth}, (${greatestIncrease}) \n'
f'Greatest Decrease in Profits: {leastMonth}, (${greatestDecrease}) \n'
)

print(output)

with open (outputPath, 'w') as txtFile:
    txtFile.write(output)





