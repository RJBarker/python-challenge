#%%

# Overall Task: Analyze the finanaces of your company.
# Dataset contains two columns: Date and Profit/Losses
#----------------------------#
# Tasks:
    # 1 - Get total number of months in the dataset
    # 2 - The net total amount of "Profit/Losses" over the entire period
    # 3 - The changes in "Profit/Losses" over the entire period, and then the average of those changes
    # 4 - The greatest increase in profits (date and amount) over the entire period
    # 5 - The greatest decrease in profits (date and amount) over the entire period

#----------------------------#
# Code Start
#----------------------------#

# Import required modules

# os for file path sourcing
import os
# csv for reading and working with csv file
import csv

# path to dataset (ref1)
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as dataset:
    
    # Set the delimiter for the file
    datareader = csv.reader(dataset, delimiter=',')

    # Skip the header row
    next(datareader)

    # # Print the rows to test the file is being read correctly. Comment out once checked and confirmed
    # for row in datareader:
    #     print(row)

    ## 1 - Get total number of months in the dataset
    # Set initial var
    totalmonths = 0
    prof_loss_tot = 0
    chnge_dict = {}
    prev_row = 0
    inc_val = 0
    dec_val = 0
    inc_dte = ""
    dec_dte = ""

    for row in datareader:
        totalmonths += 1
        prof_loss_tot += int(row[1])
        
        if prev_row != 0:
            chnge_dict.update({row[0]: int(row[1]) - int(prev_row)})
        prev_row = int(row[1])
        
    # if int(row[1]) > inc_val:
    #     inc_val = int(row[1])
    #     inc_dte = row[0]
    # elif int(row[1]) < dec_val:
    #     dec_val = int(row[1])
    #     dec_dte = row[0]

    for val in chnge_dict:
        if chnge_dict[val] > inc_val:
            inc_val = chnge_dict[val]
            inc_dte = val
        elif chnge_dict[val] < dec_val:
            dec_val = chnge_dict[val]
            dec_dte = val

    

avg_chnge = round(float((sum(chnge_dict.values()) / len(chnge_dict))),2)



    # ## 2 - The net total amount of "Profit/Losses" over the entire period
    # # Set initial var
    # for row in datareader:
    #     prof_loss_list.append(int(row[1]))
    #print(prof_loss_list)


print(f'Total months in data set = {totalmonths}')
print('----------------------------')
print(f'The Total prof/loss = ${prof_loss_tot}')
print('----------------------------')
print(f'The average change is: ${avg_chnge}')
print('----------------------------')
print('The Greatest Increase in Profits: ' + inc_dte + ' ($' + str(inc_val) + ')')
print('----------------------------')
print('The Greatest Decrease in Profits: ' + dec_dte + ' ($' + str(dec_val) + ')')
print('----------------------------')
print("File complete")