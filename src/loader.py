import csv
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/app_logs.csv")

def load_logs():
    logs = []
    try:
        with open(DATA_FILE, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                logs.append(row)
        if not logs:
            print("Warning: CSV is empty!")
    except FileNotFoundError:
        print(f"File {DATA_FILE} not found!")
    return logs


if __name__ == "__main__":
    logs = load_logs()
    print(f"Total logs loaded: {len(logs)}")
