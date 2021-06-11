'''
=============
This program process.csv file. 
It's corrects a recording error
made at the first stage of data processing. 
Removes \r\n (and other minor improvement) at the end 
of files and generally does everything 
right and beautifully. Don't ask how.
=============
'''

import csv

def rewrite_csv(input_f, output_f):
    input = open(input_f, 'r', newline='')
    my_csv_data = list(input)
    writing_list = list()
    for i in range(len(my_csv_data)):
        temp = my_csv_data[i]
        temp = temp.replace('"', '')
        temp = temp.replace('\r\n', '')
        if temp!='':
            writing_list.append(temp)
    with open(output_f, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for item in writing_list:
            csv_writer.writerow([item])

input_f = 'C:/Papers/RawData/XRP/XRPUSD_1m.csv'
output_f = 'C:/Papers/RawData/XRP/XRPUSD_1m_2.csv'
rewrite_csv(input_f, output_f)
