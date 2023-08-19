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

# os for file path
import os
# csv for reading and working with csv file
import csv

# path to dataset (ref1)
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as dataset:
    
    # Set the delimiter for the file
    datareader = csv.reader(dataset, delimiter=',')

    # Skip and store the header row
    dataheader = next(datareader)

    # # Print the rows to test the file is being read correctly. Comment out once checked and confirmed
    # print(dataheader)
    # for row in datareader:
    #     print(row)

    
    # Set initial var
    totalmonths = 0     # Used to store count of months
    prof_loss_tot = 0   # Used to calculate the total of prof/loss
    chnge_dict = {}     # Dictionary to store Date as the key and calculated change as the value
    prev_row = ""       # Stores the prev months profit/loss value to be used for calculating the change. Empty string used to avoid calculating the first month with 0
    inc_val = 0         # Var to store the greatest increase value
    dec_val = 0         # Var to store the greatest decrease value
    inc_dte = ""        # Var to store the greatest increase date 
    dec_dte = ""        # Var to store the greatest decrease date

    for row in datareader:

        ## 1 - Get total number of months in the dataset
        # For each row (not incl. header) +1 to get count of months
        totalmonths += 1
        
        ## 2 - The net total amount of "Profit/Losses" over the entire period
        # For each row add the profit/loss to the running total
        prof_loss_tot += int(row[1])
        

        # If prev_row = "" then this is the first row so do not calculate
        # If prev_row contains integer then update the chnge_dict with: row[0] as the key and calculated change as the value
        if prev_row != "":
            chnge_dict.update({row[0]: int(row[1]) - int(prev_row)})
        # Update the var to row[1] value ready for next calculation
        prev_row = int(row[1])

    ## 3 - The changes in "Profit/Losses" over the entire period, and then the average of those changes
    # Using the values in the dictionary, calculate the avg change as a float and round to 2 decimal places    
    avg_chnge = round(float((sum(chnge_dict.values()) / len(chnge_dict.values()))),2)    # 

    ## 4 - The greatest increase in profits (date and amount) over the entire period
    ## 5 - The greatest decrease in profits (date and amount) over the entire period
    # Using the dictionary, iterate through each value to find if it's the greatest increase or decrease and store the value and date key
    for key in chnge_dict:
        if chnge_dict[key] > inc_val:
            inc_val = chnge_dict[key]
            inc_dte = key
        elif chnge_dict[key] < dec_val:
            dec_val = chnge_dict[key]
            dec_dte = key
   
## Write the results to a text file
output_path = os.path.join('Analysis', 'analysis_results.txt')

with open(output_path, 'w') as txtfile:
    txtfile.write('Financial Analysis\n')
    txtfile.write('\n')
    txtfile.write('----------------------------\n')
    txtfile.write('\n')
    txtfile.write(f'Total Months: {totalmonths}\n')
    txtfile.write(f'Total: ${prof_loss_tot}\n')
    txtfile.write(f'Average Change: ${avg_chnge}\n')
    txtfile.write('Greatest Increase in Profits: ' + inc_dte + ' ($' + str(inc_val) + ')\n')
    txtfile.write('Greatest Decrease in Profits: ' + dec_dte + ' ($' + str(dec_val) + ')\n')
    txtfile.close

## Print the results to the terminal
print("Financial Analysis")
print("")
print("----------------------------")
print("")
print(f'Total Months: {totalmonths}')
print(f'Total: ${prof_loss_tot}')
print(f'Average Change: ${avg_chnge}')
print('Greatest Increase in Profits: ' + inc_dte + ' ($' + str(inc_val) + ')')
print('Greatest Decrease in Profits: ' + dec_dte + ' ($' + str(dec_val) + ')')