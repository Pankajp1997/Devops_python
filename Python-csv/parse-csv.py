import csv
'''
with open('names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    #next(csv_reader) # skips the first row of the file 
    with open('new_names.csv','w') as new_files:
        csv_writer = csv.writer(new_files,delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line) 
'''
'''
with open("new_names.csv",'r') as rf:
    csv_reader = csv.reader(rf,delimiter="\t") # mention the delimeter param as the csv file only knows the , as delimeter 
    for line in csv_reader:
        print(line)
'''
'''
# with regular dictionary method 
with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('new_names.csv','w') as new_files:
        fieldnames = ['first_name','last_name','email']

        csv_writer = csv.DictWriter(new_files,fieldnames=fieldnames,delimeter="\t")
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)
'''
with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('new_names.csv','w') as new_files:
        fieldnames = ['first_name','last_name']

        csv_writer = csv.DictWriter(new_files,fieldnames=fieldnames,delimiter='\t')
        csv_writer.writeheader()
        for line in csv_reader:
            del line['email'] # Only delete the email row, check the fieldname variable as well 
            csv_writer.writerow(line)