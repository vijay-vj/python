
from urllib.request import urlopen
import json

def main():
    weburl = urlopen("https://trypyramid.com/")
    print("Result code: ", str(weburl.getcode()))
    #data = weburl.read()
    #print(data) 
    
    
if __name__ == "__main__":
    main()