
# dealing with dates and times 


from datetime import date 
from datetime import time 
from datetime import datetime 


def main():
    today1 = date.today();
    print ("Today's date is: ", today1)
    
    print (today1.day, " ", today1.month, " ", today1.year)
    
    print ("Weekly date: ", today1.weekday())
    
    
    time = datetime.now();
    print ("Time now is: ", time)
    
    t = datetime.time(datetime.now())
    print ("Current time is: ", t)
    
    wd = date.weekday(today1);
    days = ["mon", "Tue","Wed", "Thur","Fri","Sat","Sun"]    
    print ("Today is: "  . format(wd))
    print (" which is: ", days[3])
    
    
if __name__ ==  "__main__":
    main()