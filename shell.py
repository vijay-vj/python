
import os 
import shutil
from os import path 
from shutil import make_archive
from zipfile import ZipFile

def main():
    if path.exists("newfile.txt"):
        src = path.realpath("newfile.txt")
        print (src)
        head, tail = path.split(src)
        print ("path is: ", head)
        print (tail)
    
        #dest = src + ".bak"
        #shutil.copy(src,dest)
        
        #shutil.copystat(src,dest)
        
        #os.rename("textfile.txt","newfile.txt")
        #root_dir, tail = path.split(src)
        
        #shutil.make_archive("archive","zip", root_dir)
        
        
        with ZipFile("testzip.zip","w")as newzip:
            newzip.write("newfile.txt")
    
if __name__ == "__main__":
    main()