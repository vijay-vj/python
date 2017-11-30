

def main():
    # open takes two inputs -- one file name followed by permission 
    # w -- write, r -- read , a -- append  + is to say to create the file if not already
    #f = open("textfile.txt", "a+")
    
    #for i in range(10):
    #    f.write("This is line: {} \r\n " .format(i))
    
    #f.close()
   # f = open("textfile.txt","r")
    
    #if f.mode == 'r':
      #  contents = f.read()
     #   print(contents)
    
   # f = open("dates.py", "r")
    #if f.mode == 'r':
    #    fl = f.readlines()
    #    for x in fl:
    #        if x != '    main()': 
    #            print (x)
    
    f = open("C:\\Java\\textfile.txt","w+")
    f.write("Test")
    
    f.close()
if __name__ == "__main__": 
    main()   