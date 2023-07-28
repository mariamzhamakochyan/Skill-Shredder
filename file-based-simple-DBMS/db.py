import csv
import os

DB_FILE = "database.txt"

def initialize_database():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w"):
            pass

def add_record(record):
    with open(DB_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(record)

def read_all_records():
    records = []
    with open(DB_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            records.append(row)
    return records

def update_record(record_id, updated_record):
    records = read_all_records()
    if 0 <= record_id < len(records):
        records[record_id] = updated_record
        with open(DB_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(records)
        return True
    return False

def delete_record(record_id):
    records = read_all_records()
    if 0 <= record_id < len(records):
        del records[record_id]
        with open(DB_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(records)
        return True
    return False

