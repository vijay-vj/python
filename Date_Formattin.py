
from datetime import datetime

def main():
    x = 0 
    print (x)
    now = datetime.now();
    print (now.strftime("%Y"))
    # %a/ %A  -- weeday 
    # d/ D -- Day 
    # b/ B -- Month 
    # y/ Y -- Year 
    # c -- Local date and time 
    # x -- Local date 
    # X -- Local time 
    # 
    print (now.strftime("%A, %d, %B, %Y"))
    print (now.strftime("%c, %x, %X"))
    # I/ H -- 12/ 24, M - Minutes, S - Seconds, p -- AM/ PM
    print (now.strftime("%I:%M:%S %p"))
    print (now.strftime("%H:%M"))
    
if __name__ == "__main__": 
    main()
