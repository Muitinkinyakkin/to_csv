import csv
import re

# Function to extract 16-digit numbers from a string
def extract_16_digits(text):
    match = re.search(r"\b\d{16}\b", text)  # Match 16 consecutive digits
    if match:
        return match.group()
    else:
        return None

# Read the input CSV file
with open("file1.csv", "r", newline="") as input_file:
    reader = csv.DictReader(input_file)

    # Create a list to store the extracted data
    output_data = []

    for row in reader:
        preview = row["Preview"]
        cc = extract_16_digits(preview)

        if cc:
            output_data.append({"CC": cc, "Date": row["Date"], "Author": row["Author"]})

# Write the extracted data to a new CSV file
with open("Cfile1.csv", "w", newline="") as output_file:
    fieldnames = ["CC", "Date", "Author"]
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(output_data)

print("Data extraction complete! 16-digit numbers extracted to Cfile1.csv")
