import csv
import io

# Parse csv_file and return list of lists
def parse(csv_file, header):

    entries = []
    stream = io.StringIO(csv_file.stream.read().decode("UTF8"), newline=None)
    csv_input = csv.reader(stream)
    #print("file contents: ", file_contents)
    #print(type(file_contents))
    if header == 'True':
        csv_input = csv_input[1:]

    for row in csv_input:
        entries.append(row)
        # print("row in csv parser ", row)

    return entries