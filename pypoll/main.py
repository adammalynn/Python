# import the os module
import csv
import os

# create file paths across operating systems,saved filepath as csvpath
csvpath=os.path.join("C:/Users","Adammalynn","Desktop","Practise","Python_hmwk","PyPoll","Resources","election_datat.txt")

# Open the file by Reading using csvmodule and store contents in csvfile
with open(csvpath,newline="")as csvfile:

    # csv reader specifies delimiter and variable that holds contents in csvreader
    pypoll = csv.reader(csvfile,delimiter=",")

    # read header row first
    poll_header=next(pypoll)
    # print(f"CSVHeader:{csv_header}")
    # set parameters

    count = 0
    sum_total = 0
    temp_list = []
    temp_list_of_candidates = []
    temp_list2 = []
    temp_list3 = []
    temp_dict = {}
    # create a list with row, while looping through pypoll data increment vote count or row as well
    for row in pypoll:
        temp_list.append(row)
        count = count + 1
        # create a list to hold unique candidates
        if row[2] not in temp_list_of_candidates:
            temp_list_of_candidates.append(row[2])
    # just with list
    for candidate in temp_list_of_candidates:
        candidate_count = 0
        for voter_rec in temp_list:
            # to increment count for each voter
            if candidate == voter_rec[2]:
                candidate_count = candidate_count + 1
        temp_list2.append(candidate_count)
    print(temp_list_of_candidates, temp_list2)
    print("Election Results")
    print("-------------------------")
    print("Total Votes: ", count)
    print("-------------------------")
    for item in range(len(temp_list2)):
        # first = (temp_list2[0]/count) * 100
        # second = (temp_list2[1] / count) * 100
        # third = (temp_list2[2] / count) * 100
        # fourth = (temp_list2[3] / count) * 10
        print(temp_list_of_candidates[item],": ", round(round((temp_list2[item]/count), 4)* 100,4),"% ", "(", temp_list2[item],")", sep="")
    print("--------------------------")
    print("Winner: ", temp_list_of_candidates[(temp_list2.index((max(temp_list2))))])
    print("--------------------------")