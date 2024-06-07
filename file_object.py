# File Objects
'''
f = open('test.txt','r')
# r = read 
# w = write 
# a = Appendong to file 
# r+ = read an write into file 
print(f.name) # name of the file 
print(f.mode) # what's the mode of the file 
f.close() # we need to explicily close the files that you opened 
# we can use context manager 

with open('test.txt','r') as f: # it will automatically close the file and it is considered as best
   #print(f.read()) # read the context of the file 
   #f_contents = f.read() # reads whole contents
   #f_contents = f.readlines() # read line by line showing line number 
   # f_contents = f.readline() # it reads one line 
   for line in f:
      print (line, end='')
   #print(f_contents)
  
   # we can specify how much data we need at a time then we can do that as well. 
with open('test.txt','r') as f:
    f_contents = f.read(100) # reads first 100 (words) characters from the file instead of printing all at time.
    print(f_contents) 
     
with open('test.txt','r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents,end='#')
        f_contents = f.read(size_to_read)

with open('test.txt','r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents,end='')
  
    f.seek(0) # starts from the first 
    f_contents = f.read(size_to_read)
    print(f_contents)
    print(f.tell()) # tells the cursor position 


# we will look into the Write mode 
# If file doesn't exist in the system it will create it and if the file is there t will override it. 
# so be careful while writing into the file. We can use the 'a' for appending to the file.
with open('test.txt','w') as f:
    #pass # we can create a file without entering anything 
    f.write('Test')
    f.seek(0)
    f.write('R')

# reading and writing simultaneously 
# copying the file from one to another file 
with open('test.txt','r') as rf:
    with open('test_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)

# If we need to copy the files in picture format
# we need to use the binary mode 
with open('pankaj.jpg','rb') as rf:
    with open('pic_copy.jpg','wb') as wf:
        for line in rf:
            wf.write(line)

# if we want to read in chunk formagt then we will read that much data 
with open('pankaj.jpg','rb') as rf:
    with open('pic_copy.jpg','wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0 :
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
'''
