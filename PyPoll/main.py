import os
import csv

DATA_FILENAME = os.path.join(os.path.dirname(__file__), r"Resources\election_data.csv")
OUTPUT_FILENAME = os.path.join(os.path.dirname(__file__), r'Analysis\output.txt')

def main():
    with open(DATA_FILENAME, "r") as file:
        reader = csv.reader(file)
        votes = 0
        candidates = {}

        header = next(reader)

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

        for name, c_votes in candidates.items():
            print(f"{name}: {(c_votes/votes*100):.3f}% ({c_votes})")

        print(f"------------------------------")
        print(f"*** Winner: {sorted(candidates, key=candidates.get, reverse=True)[0]} ***")
        print(f"------------------------------")

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