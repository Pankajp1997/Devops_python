# This code works like, I have a csv files in a folder and I want to rename those according to the values present in it. 
# it's like a logs i have and exported it from any application, I want to rename it. 

import os 
import glob
import csv 
f = glob.glob('*.csv')
#print(f)

for i in f:
    #print(i)
    with open(i,'r') as file:
        csv_reader = csv.reader(file,delimiter=',')
        next(csv_reader)
        first_line = file.readline()
        data_list = first_line.split(',')
        #print(data_list[2])
        new_name = data_list[2] + '_Full' + '.csv' 
        print(new_name)
    file.close()
    os.rename(i,new_name)
    