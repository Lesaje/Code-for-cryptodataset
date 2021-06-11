'''
=============
This program process multiple .csv files. 
It's unites, delete non-relevant data (with wrong timestamps)
and sorts data from old to the new ones.

Data in input files should have this format for each row:
unixtimestamp,date,symbol,open,high,low,close,Volume USD,Volume EOS
instead EOS can be any other currency (and instead of the USD too).

In fact, it can process in aforementioned way any data, which
should be sorted by the first (integer) cell value

=============
'''

import os
import glob
import csv

os.chdir("C:/Papers/RawData/XRP")           #our folder with files
extension = 'csv'

def combine(extension):         #just combine multiple files in single one
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    combined_csv = '\n'.join([open(f, 'r', encoding='utf8').read().strip() for f in all_filenames ])
    with open("XRPUSD.csv", 'w') as f:
        f.write(combined_csv)

combine(extension)

def delete_time(input_f, output_f):             #delete data with non-relevant time values
    output = open(output_f, 'w', newline='')
    input = open(input_f, 'r', newline='')
    #output = open(output_f, 'w+b')
    writer = csv.writer(output)
    for row in csv.reader(input):
        if row[0]<'1622592000' and row[0]>'1527811200':     # 2021-06-02-00:00
            writer.writerow(row)                            # 2018-06-01-00:00
    input.close()
    output.close()

input_f = 'XRPUSD.csv'
output_f = 'XRPUSD_deltime.csv'
delete_time(input_f, output_f)

def sort_csv(input_f, output_f):                    #sort from old to new
    input = open(input_f, 'r', newline='')
    my_csv_data = list(input)
    dict_v = dict()
    for i in range(len(my_csv_data)):
        temp_list = list(my_csv_data[i].split(sep=','))
        dict_v.update({int(temp_list[0]):i})
    list_keys = list(dict_v.keys())
    list_keys.sort()
    sorted_csv_data = list()
    for i in list_keys:
        sorted_csv_data.append(my_csv_data[dict_v[i]])
    with open(output_f, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for item in sorted_csv_data:
            csv_writer.writerow([item])
    input.close()

input_f = 'XRPUSD_deltime.csv'
output_f = 'XRPUSD_sorted.csv'
sort_csv(input_f, output_f)