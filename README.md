# python-challenge
#below is the code for PyPoll
#import csv for the data we need
#in the below code, i used examples from class as well as help from my tutor on how to set the paths and create a new path for a text file
import os
import csv
#setting paths for the file and the new output file
DATA_FILENAME = os.path.join(os.path.dirname(__file__), r"Resources\election_data.csv")
OUTPUT_FILENAME = os.path.join(os.path.dirname(__file__), r'Analysis\output.txt')
#in the below code, i used help from my tutor to create these for loops
def main():
    with open(DATA_FILENAME, "r") as file:
        reader = csv.reader(file)
        votes = 0
        candidates = {}

        header = next(reader)
#using a for loop to find the candidates that received votes
        for line in reader:
            votes += 1

            if line[2] not in candidates:
                candidates[line[2]] = 1
            else:
                candidates[line[2]] += 1

        
        print(f"Election Results")
        print(f"------------------------------")
        print(f"Total Votes: {votes}")
        print(f"------------------------------")
#using a for loop to find the percentage of votes for each candidate and then finding a winner
        for name, c_votes in candidates.items():
            print(f"{name}: {(c_votes/votes*100):.3f}% ({c_votes})")

        print(f"------------------------------")
        print(f"*** Winner: {sorted(candidates, key=candidates.get, reverse=True)[0]} ***")
        print(f"------------------------------")
#creating an output for a text file that will print the results
#i looked at examples from class and chatGPT to help me with the below code 
        os.makedirs(os.path.dirname(OUTPUT_FILENAME), exist_ok=True)
        with open(OUTPUT_FILENAME, "w") as output:
            output.write(f"Election Results\n")
            output.write(f"------------------------------\n")
            output.write(f"Total Votes: {votes}\n")
            output.write(f"------------------------------\n")

            for name, c_votes in candidates.items():
                output.write(f"{name}: {(c_votes/votes*100):.3f}% ({c_votes})\n")

            output.write(f"------------------------------\n")
            output.write(f"*** Winner: {sorted(candidates, key=candidates.get, reverse=True)[0]} ***\n")
            output.write(f"------------------------------\n")

if __name__ == "__main__":
    main()
    
    
#below is the code for PyBank
#import the csv file with the data we want
import os
import csv
#here i used help from my tutor and examples from class to create the correct paths
#set the path for the file and the output file
DATA_FILENAME = os.path.join(os.path.dirname(__file__), r'Resources\budget_data.csv')
OUTPUT_FILENAME = os.path.join(os.path.dirname(__file__), r'Analysis\output.txt')
#below i got help from my tutor with creating the variables and the for loop 
#creating variables and reading the csv file
def main():
    with open(DATA_FILENAME, "r") as file:
        reader = csv.DictReader(file)
        changes = []
        greatest_increase = {}
        greatest_decrease = {}

        previous_profit_losses = 0

        line = next(reader)
        months = 1
        value = int(line['Profit/Losses'])
        previous_profit_losses = value
        net_value = value

#using a for loop to find the greatest increase/decrease between the months
        for line in reader:
            months += 1
            value = int(line['Profit/Losses'])

            change = -(previous_profit_losses - value)
            previous_profit_losses = value
            changes.append(change)

            net_value += value

            if not greatest_increase or change > int(greatest_increase['Increase']):
                greatest_increase = {"Date": line['Date'], "Increase": change}
                
            if not greatest_decrease or change < int(greatest_decrease['Decrease']):
                greatest_decrease = {"Date": line['Date'], "Decrease": change}
#printing the results in the terminal
        print(f"Total Months: {months}")
        print(f"Total: ${net_value}")
        print(f"Average change: ${sum(changes)/len(changes):.2f}")
        print(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Increase']})")
        print(f"Greatest Descrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Decrease']})")
#below i used chatgpt to help me write to a text file
        # create output dir if it doesn't exit for a text file with the results
        os.makedirs(os.path.dirname(OUTPUT_FILENAME), exist_ok=True)
        # save to file in a way
        with open(OUTPUT_FILENAME, "w") as output:
            print(f"Total Months: {months}", file=output)
            print(f"Total: ${net_value}", file=output)
            print(f"Average change: ${sum(changes)/len(changes):.2f}", file=output)
            print(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Increase']})", file=output)
            print(f"Greatest Descrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Decrease']})", file=output)

if __name__ == "__main__":
    main()
