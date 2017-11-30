
from urllib.request import urlopen
import json

def printResults(data):
    theJson = json.loads(data)
    if "title" in theJson["metadata"]:
        print (theJson["metadata"]["title"])
        count = theJson["metadata"]["count"]
        print("event accoured are: ", str(count))
        
        for i in theJson["features"]:
            if i["properties"]["mag"] > 4: 
                print (i["properties"]["mag"]," mag at ", i["properties"]["place"])
        
        
        
def main():
   urldata = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson" 
   weburl = urlopen(urldata) 
   print(weburl.getcode())
   if (weburl.getcode()==200): 
       data = weburl.read()
       printResults(data)
   else:
       print("Got an error: ", weburl.getcode())    
    

if __name__ == "__main__":
    main()