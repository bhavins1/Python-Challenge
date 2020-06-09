import os
import csv


csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    lines = len(list(csvreader))
    datacount = (
        f"Election Results\n"
        f"---------------------------\n"
        f"Total Votes: {str(lines)}\n"
        f"---------------------------\n"
    )
    print(datacount)
    
    csvfile.seek(1)

    CountKhan = 0
    CountCorrey = 0
    CountLi = 0
    CountOTooley = 0
    
    for row in csvreader:
        if row[2] == "Khan":
            CountKhan = CountKhan + 1
        elif row[2] == "Correy":
            CountCorrey = CountCorrey +1
        elif row[2] == "Li":
            CountLi = CountLi + 1
        elif row[2] == "O'Tooley":
            CountOTooley = CountOTooley + 1

    Khanpercent = (CountKhan/lines)*100
    CorreyPercent = (CountCorrey/lines)*100
    LiPercent = (CountLi/lines)*100
    OTooleyPercent = (CountOTooley/lines)*100

    datatally = (
        f"Khan: {Khanpercent:.3f}% ({CountKhan})\n"
        f"Correy: {CorreyPercent:.3f}% ({CountCorrey})\n"
        f"Li: {LiPercent:.3f}% ({CountLi})\n"
        f"O'Tooley: {OTooleyPercent:.3f}% ({CountOTooley})\n"
    )
    print(datatally)

    if Khanpercent > (CorreyPercent and LiPercent and OTooleyPercent):
        winner = "Khan"
    elif CorreyPercent > (Khanpercent and LiPercent and OTooleyPercent):
        winner = "Correy"
    elif LiPercent > (Khanpercent and CorreyPercent and OTooleyPercent):
        winner = "Li"
    elif OTooleyPercent > (Khanpercent and CorreyPercent and LiPercent):
        winner = "O'Tooley"

    tallywinner = (f"---------------------------\n"
    f"Winner: {winner}\n"
    f"---------------------------"
    )
    print(tallywinner)
    
output_path = os.path.join('Analysis', 'results.txt')

with open(output_path, 'w') as newtextfile:
    newtextfile.write(datacount)
    newtextfile.write(datatally)
    newtextfile.write(tallywinner)