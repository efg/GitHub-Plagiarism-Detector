import csv
import io

# Parse csv_file and return rows as list of lists
def parse(csv_file, header):

    entries = []
    stream = io.StringIO(csv_file.stream.read().decode("UTF8"), newline=None)
    csv_input = csv.reader(stream)
    
    # Filter out header row if any
    if header == 'True':
        csv_input = csv_input[1:]

    # Iterate over each row in the csv file
    for row in csv_input:
        entries.append(row)
    print(entries)
    return entries