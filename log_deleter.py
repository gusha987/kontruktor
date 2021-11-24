import os
#Finds the current directory
path = os.path.dirname(__file__)
#tries to delete file 'Actor.log' and 'Database.log' and prints the according results
try:
    os.remove((path)+ "\Actor.log")
    
    print('File "Actor.log" has succesfully been deleted')
except OSError as e:
    print('File "Actor.log" has already been deleted')

try:
    os.remove((path)+ "\Database.log")
    
    print('File "Database.log" has succesfully been deleted')
except OSError as e:
    print('File "Database.log" has already been deleted')
    