'''
=============
This program process .csv file. 
It's produces 5 or 15 (or any minute format, 120, 1440, whatever)
minute data from 1 minute format.
=============
'''

import csv

def create_csv(input_f, output_f, timeformat):                    #sort from old to new
    input = open(input_f, 'r', newline='')
    my_csv_data = list(input)
    high_list = list()
    low_list = list()
    writing_list = list()
    vol_USD = 0.0
    vol_crypto = 0.0
    for i in range(len(my_csv_data)):
        if (i%timeformat == 0 and i!=0):                                 #5th or 15th minute
            temp_list = list(my_csv_data[i].split(sep=','))
            unix = temp_list[0].replace('"', '')
            date = temp_list[1]
            symbol = temp_list[2]
            openp = temp_list[3]
            high_list.append(float(temp_list[4]))
            low_list.append(float(temp_list[5]))
            vol_USD += float(temp_list[7])
            vol_crypto += float(temp_list[8].replace('"\r\n', ''))
            writing_list.append(unix+','+date+','+symbol+','+openp+','
                                +str(max(high_list))+','+str(min(low_list))+
                                ','+close+','+str(vol_USD)+','+str(vol_crypto))
            temp_list.clear()
            high_list.clear()
            low_list.clear()
        else:
            temp_list = list(my_csv_data[i].split(sep=','))
            if(i%timeformat == timeformat-1):                   #4th or 14th minute
                close = temp_list[6]
            high_list.append(float(temp_list[4]))
            low_list.append(float(temp_list[5]))
            vol_USD += float(temp_list[7])
            vol_crypto += float(temp_list[8].replace('"\r\n', ''))
            temp_list.clear()
    with open(output_f, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for item in writing_list:
            csv_writer.writerow([item])
    input.close()

input_f = 'C:/Papers/RawData/BCH/BCHUSD_1m.csv'
timeformat = 15
output_f = 'C:/Papers/RawData/BCH/BCHUSD_15m.csv'
create_csv(input_f, output_f, timeformat)