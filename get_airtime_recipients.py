import csv
import sys
import pprint


def recipients(variables_file):

    reader = csv.DictReader(open(variables_file, 'rb'))
    # Initialize an empty list
    dict_list = []

    # read all contents in ti a dictionary
    for line in reader:
        dict_list.append(line)

    # loop through the list of dicts
    for index in dict_list:
        # Dispose Employee- Name nad format the keys
        index['amount'] = index.pop('Amount')
        index['phoneNumber'] = index.pop('Phone-Number')
        index.pop('Employee-Name')

    return dict_list


# airtime_receivers = recipients('employee.csv')

# pprint.pprint(airtime_receivers)
