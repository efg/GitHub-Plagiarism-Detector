import csv
import io
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# Parse csv_file and return rows as list of lists
def parse(csv_file, header):
    entries = []
    stream = io.StringIO(csv_file.stream.read().decode("UTF8"), newline=None)
    csv_input = csv.reader(stream, skipinitialspace=True,
                           delimiter=',', quoting=csv.QUOTE_NONE)
    # Filter out header row if any
    if header == 'True':
        csv_input = csv_input[1:]
    # Iterate over each row in the csv file
    for row in csv_input:
        entries.append(row)
    logger.info(f"No of entries in the csv: {len(entries)}")
    return entries
