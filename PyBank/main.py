import os
import csv

DATA_FILENAME = os.path.join(os.path.dirname(__file__), r'Resources\budget_data.csv')
OUTPUT_FILENAME = os.path.join(os.path.dirname(__file__), r'Analysis\output.txt')

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

        print(f"Total Months: {months}")
        print(f"Total: ${net_value}")
        print(f"Average change: ${sum(changes)/len(changes):.2f}")
        print(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Increase']})")
        print(f"Greatest Descrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Decrease']})")

        # Create output dir if it doesn't exit
        os.makedirs(os.path.dirname(OUTPUT_FILENAME), exist_ok=True)
        # Save to file in a 'fancy' way
        with open(OUTPUT_FILENAME, "w") as output:
            print(f"Total Months: {months}", file=output)
            print(f"Total: ${net_value}", file=output)
            print(f"Average change: ${sum(changes)/len(changes):.2f}", file=output)
            print(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Increase']})", file=output)
            print(f"Greatest Descrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Decrease']})", file=output)

if __name__ == "__main__":
    main()


