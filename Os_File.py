import os 
from os import path 

import datetime 
from datetime import date, time, datetime 
import time 

def main():
    print (os.name);
    print ("File exists: ", str(path.exists("textfile.txt")))
    print ("Item is a File: ", str(path.isfile("textfile.txt")))
    print ("Item is a directory: ", str(path.isdir("C:\Java")))
    
    print ("The path of {} is " .format("textfile.txt"), 
           str(path.realpath("textfile.txt")))
    print("Path and name : ", str(path.split(path.realpath("textfile.txt"))))
    t = time.ctime(path.getmtime("textfile.txt"))
    print (t)
    print (datetime.fromtimestamp(path.getmtime("textfile.txt")))
    
    td = datetime.now() - datetime.fromtimestamp(path.getmtime("textfile.txt"))
    
    print ("This file was modified {} secs ago " .format(td))
    
    print ("0r, ", str(td.total_seconds()), "mins")
    
if __name__ == "__main__":
    main()