from datetime import datetime
from datetime import timedelta 
from datetime import date


def main():
    x = 0 
    now = datetime.now()
    
    print (now.strftime("%I:%M:%S"))
    print (timedelta(days=365, hours = 5, minutes =1 ))
    
    print (str(datetime.now()))
    
    print ("One year from now: ", str(datetime.now()+ timedelta(days=365)))
    
    t = (datetime.now() - timedelta(weeks=1,days=2))
    s = t.strftime("%A, %B, %d, %Y")
    
    
    today = date.today()
    
    print("Today is: %d which is a monday "  .format(today))
    
    print (s)
if __name__ == "__main__":
    main()   