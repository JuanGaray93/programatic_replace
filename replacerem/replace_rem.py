import os
import re
import sys

directory = "./"

rem_multiple = 11.0 / 16.0



def get_processed_number_from_rem(rem_occurrence):
    rem_number = re.findall(r"(\d+(\.\d+)?)", rem_occurrence)[0][0]
    rem_number = float(rem_number)
    rem_number = rem_number * rem_multiple
    rem_number = round(rem_number, 2)
    return "{}rem".format(rem_number)


def get_processed_line(line):
    processed_line = line
    rem_occurrences = re.findall(r"(\d+(?:\.\d+)?rem)", line)
    for rem_occurrence in rem_occurrences:
        rem_number = get_processed_number_from_rem(rem_occurrence)
        processed_line = line.replace(rem_occurrence, rem_number)
    return processed_line


def process_file(file_name):
    processed_lines = []
    with open(file_name, "r") as file:
        line = file.readline()
        while line:
            processed_line = get_processed_line(line)
            processed_lines.append(processed_line)
            line = file.readline()
    with open(file_name, "w") as file:
        file.writelines(processed_lines)
        

for root, dirs, file_names in os.walk(directory):
    # for file_name in file_names:
        # if file_name.endswith(".scss"):
        #   process_file( os.path.join(root, file_name))
    for file_name in sys.argv:
        process_file( os.path.join(root, file_name))
