import os
import csv

DATA_FILENAME = os.path.join(os.path.dirname(__file__), r'Resources\budget_data.csv')

def main():
    with open(DATA_FILENAME, "r") as file:
        reader = csv.DictReader(file)
        months = 0
        net_value = 0
        greatest_increase = {}
        greatest_decrease = {}

        for line in reader:
            months += 1
            value = int(line['Profit/Losses'])
            net_value += value

            if not greatest_increase or value > int(greatest_increase['Profit/Losses']):
                greatest_increase = line
                
            if not greatest_decrease or value < int(greatest_decrease['Profit/Losses']):
                greatest_decrease = line

        print(f"Total Months: {months}")
        print(f"Total: ${net_value}")
        print(f"Average change: ${int(net_value/months)}")
        print(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Profit/Losses']})")
        print(f"Greatest Descrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Profit/Losses']})")

if __name__ == "__main__":
    main()


