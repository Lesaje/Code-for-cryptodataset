'''
=============
This program process .csv file. 
It's produces binary dataset with 1 value
if 1 hour candlestick chart closing price
more then last, and -1 if less.
=============
'''

import csv

def create_dataset(input_f, output_f):                 
    input = open(input_f, 'r', newline='')
    my_csv_data = list(input)
    writing_list = list()
    close2 = 0.0
    close1 = 0.0
    for i in range(len(my_csv_data)):
        temp_list = list(my_csv_data[i].split(sep=','))
        close2 = close1
        close1 = float(temp_list[6])
        if (close1>close2):
            writing_list.append(1)
        else:
            writing_list.append(-1)
    with open(output_f, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for item in writing_list:
            csv_writer.writerow([item])
    input.close()

input_f = 'C:/Papers/RawData/1hdata/combined.csv'
output_f = 'C:/Papers/RawData/1hdata/binary_dataset.csv'
create_dataset(input_f, output_f)