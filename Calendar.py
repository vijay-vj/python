import calendar

c = calendar.TextCalendar(calendar.MONDAY)
#str = c.formatmonth(2013,5,0,0);
#print (str)



#c = calendar.HTMLCalendar(calendar.MONDAY)
#str = c.formatmonth(2013,5);
#print (str)


#for i in c.itermonthdays(2013,5):
    #print (i)
    
    
#for day in calendar.day_name:
    #print (day)    
    

#for month in calendar.month_name:
    #print (month)        
    
    
for i in range(1,13):
    cal = calendar.monthcalendar(2013, i)
    weekone = cal[0]
    weektwo = cal[1]
    
    
    if weekone[calendar.FRIDAY] != 0: 
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
        
    print ("Meet day: ", calendar.month_name[i], meetday)    
    
    print ("{}10s ".format(calendar.month_name[i]))
        
    