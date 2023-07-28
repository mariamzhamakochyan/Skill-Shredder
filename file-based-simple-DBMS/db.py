# simple_db.py

import csv
import os

# Constants
DB_FILE = "database.txt"

def initialize_database():
    """Create the database file if it doesn't exist."""
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w"):
            pass

def add_record(record):
    """Add a new record to the database."""
    with open(DB_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(record)

def read_all_records():
    """Read all records from the database."""
    records = []
    with open(DB_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            records.append(row)
    return records

def update_record(record_id, updated_record):
    """Update a record in the database."""
    records = read_all_records()
    if 0 <= record_id < len(records):
        records[record_id] = updated_record
        with open(DB_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(records)
        return True
    return False

def delete_record(record_id):
    """Delete a record from the database."""
    records = read_all_records()
    if 0 <= record_id < len(records):
        del records[record_id]
        with open(DB_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(records)
        return True
    return False

