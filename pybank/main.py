# import the os module
import csv
import os

# create file paths across operating systems, saved file path as csvpath
csvpath = os.path.join("C:/Users", "Adammalynn", "Desktop", "Practise", "Python_hmwk", "PyBank", "Resources", "budget_data.csv")

# Open the file by Reading using csv module and store contents in csvfile
with open(csvpath, newline="") as csvfile:

    # csv reader specifies delimiter and variable that holds contents in csvreader
    csvreader = csv.reader(csvfile, delimiter=",")

    # print(csvreader)

    # read header row first
    csv_header = next(csvreader)

    # set parameters
    count = 0
    sum = 0
    tracking_sum = 0
    # List to track row
    temp_list = []
    # Read each row of data after the header
    for row in csvreader:
        # append the rows to the temp_list list
        temp_list.append(row)
        sum = sum + float(row[1])
        count = count + 1
    # List to track ...
    temp_list2 = []
    track_list = []
    track_lists = []
    for tracker in range(len(temp_list) - 1):
        tracking_diff = float(temp_list[tracker + 1][1]) - float(temp_list[tracker][1])
        temp_list2.append(tracking_diff)
        tracking_sum = tracking_sum + tracking_diff
        if tracking_diff == float(max(temp_list2)):
            track_list = temp_list[tracker + 1]
        if tracking_diff == float(min(temp_list2)):
            track_lists = temp_list[tracker + 1]
    print("Financial Analysis")
    print("-----------------------------")
    print("Total Months: ", count)
    print("Total: $", sum, sep="")
    print("Average Change", round((tracking_sum / count), 2))
    print(track_list[0],"( $",max(temp_list2),")", sep="")
    print(track_lists[0], "( $",min(temp_list2), ")", sep="")

