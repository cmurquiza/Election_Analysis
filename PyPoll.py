# The data we need to retrieve.
import os
# Module for reading csv files
import csv 

# Assign a variable to load a file from a path
file_to_load = os.path.join('Resources', 'election_results.csv' )

file_to_load = 'Resources/election_results.csv'

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis,txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Read the file object with the reader function
    headers = next(file_reader)
    print(headers)