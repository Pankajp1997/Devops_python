# It's an built in module you need not to do install library or Anything 
import os 
import datetime as datetime
import time 

''' 
print(dir(os))  # Prints all the commands Associated with the OS MOdule 

print (os.getcwd()) # Shows Current Working directory 

os.chdir ("P:\Devops\Python") # Chnages the Working Directory 

print(os.getcwd())

print(os.listdir()) # Prints the files in the folder

os.mkdir ('Os_module_test.txt') # Create the folder with the name given, not created subdirectory 

os.makedirs('Os_makedirs/subdir1')  # Creates the Subdirectories as well 

os.rmdir('Os_module_test.txt')

os.removedirs('Os_makedirs\subdir1')

os.rename('test','test1') # Renaming the folders as well as File names

print(os.stat('merging.py'))  #   os.stat gives the information about the File, date of time created  

print(os.stat('merging.py').st_size / 1000,end =" MB")   $ # Size

print(os.stat('merging.py').st_mtime)    # Gives the Time of creation in date and time format

mod_time = int (os.stat('merging.py').st_mtime)

#print(dir(datetime))

#print(dir(time))

print(time.ctime(mod_time))


# print all the inside folders and files from each directory 
we can use os.walk()
It traverse from top to down, it gives 3 value tuples
dirpath, dirnames, filenames 


for dirpath,dirnames,filenames in os.walk('P:\Devops\Python'):
    print(f'Found directory: {dirpath}')
    print(f'Found directory Name: {dirnames}')
    print(f'Found files: {filenames}')
    print()
# tried code for the Python    
import os

target_file = "grafana.logs"
for dirpath, dirnames, filenames in os.walk('P:\\Devops\\Python'):
    if target_file in filenames:
        print(f'Found file with directory in path: {dirpath} and path is {dirpath}')
        exit
else:
    print('Not found file')
'''
#os.makedirs('test1/test2/test3')
# print(os.environ.get('HOME'))

#file_path = os.path.join (os.environ.get('HOME'),'test.txt')
#print(file_path)

# print(os.path.basname('/tmp/test.txt')) #if false path is given you can check with os.path.exists --> test.txt 
# print(os.path.exists("/tmp/test.txt"))
# print(os.path.dirname('/tmp/test.txt '))
#print(os.path.isdir('/tmp/test.txt'))

