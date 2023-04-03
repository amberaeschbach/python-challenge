import csv

def main():
    with open(r"Resources\election_data.csv", "r") as file:
        reader = csv.DictReader(file)
        votes = 0
        candidates = {}

        for line in reader:
            votes += 1

            if line['Candidate'] not in candidates:
                candidates[line['Candidate']] = 1
            else:
                candidates[line['Candidate']] += 1

        
        print(f"Election Results")
        print(f"------------------------------")
        print(f"Total Votes: {votes}")
        print(f"------------------------------")

        for name, c_votes in candidates.items():
            print(f"{name}: {(c_votes/votes*100):.3f}% ({c_votes})")

        print(f"------------------------------")
        print(f"*** Winner: {sorted(candidates, key=candidates.get, reverse=True)[0]} ***")
        print(f"------------------------------")

if __name__ == "__main__":
    main()