import csv

with open('names.csv', 'r') as csv_file:   #Open Original File
    csv_reader = csv.DictReader(csv_file)       #Create CSV variable to read csv file

    for line in csv_reader:
        print(line)

    # with open('new_names.cvs', 'w') as new_file:    #opening new file for writing
    #     csv_writer = csv.writer(new_file, delimiter='\t')
    #
    #     for line in csv_reader:
    #         csv_writer.writerow(line)