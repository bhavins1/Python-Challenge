import os
import csv


csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    lines = len(list(csvreader))
    datacount = (
        f"Financial Analysis\n"
        f"---------------------------\n"
        f"Total Months: {str(lines)}\n"
    )
    # print(f"Financial Analysis\n"
    #     f"---------------------------\n"
    #     f"Total Months: {str(lines)}"
    # )
    print(datacount)
    csvfile.seek(0)
    total = 0
    csv_header = next(csvreader)
    for row in csvreader:
        total += int(row[1])
    datatotal = (
        f"Total: ${total}\n"
    )
    print(datatotal)
    #print("Total: $" + str(total))
    csvfile.seek(1)
    Month_list = []
    Monthly_PL_list = []
    Monthly_Change = []
    csv_header = next(csvreader)
    for row in csvreader:
        Month_list.append(str(row[0]))
        Monthly_PL_list.append(int(row[1]))
    
    for x in range(len(Monthly_PL_list)-1):
        Monthly_Change.append(Monthly_PL_list[x+1] - Monthly_PL_list[x])
          
    def mean(list):
        return round(sum(list)/len(list), 2)
    average = mean(Monthly_Change)
    dataaverage = (
        f"Average Change: ${average}\n"
    )
    print(dataaverage)
    #print(f"Average Change: ${average}")   
    Monthly_Change.insert(0, 0)

    Changebymonth = zip(Monthly_Change, Month_list)
    Monthly_Change_Max = max(Monthly_Change)
    for row in Changebymonth:
        if row[0] == Monthly_Change_Max:
            Dataincrease = (f"Greatest Increase in Profits: {str(row[1])} (${str(row[0])})\n")
            print(Dataincrease)
            #print("Greatest Increase in Profits: "+str(row[1])+" ""($"+str(row[0])+")")
    Changebymonth = zip(Monthly_Change, Month_list)
    Monthly_Change_Min = min(Monthly_Change)
    for row in Changebymonth:
        if row[0] == Monthly_Change_Min:
            Datadecrease = (f"Greatest Decrease in Profits: {str(row[1])} (${str(row[0])})")
            print(Datadecrease)
            #print("Greatest Decrease in Profits: "+str(row[1])+" ""($"+str(row[0])+")")

output_path = os.path.join('Analysis', 'results.txt')

with open(output_path, 'w') as newtextfile:
    newtextfile.write(datacount)
    newtextfile.write(datatotal)
    newtextfile.write(dataaverage)
    newtextfile.write(Dataincrease)
    newtextfile.write(Datadecrease)
