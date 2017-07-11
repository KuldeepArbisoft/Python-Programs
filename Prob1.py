
# coding: utf-8

# In[141]:


def CheckLeapYear(year):
    if year % 100 == 0:
        if year % 4 == 0 and year % 400 == 0:
            return True
        return False
    elif year % 4 == 0:
        return True
    return False


# In[142]:


def daysBetweenDates(year1, month1, day1, year2, month2, day2):

    daysTillMonth1 = 0;
    daysTillMonth2 = 0;
    monthsDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for i in range(month1 - 1):
        daysTillMonth1 = daysTillMonth1 + monthsDays[i];
    
    for i in range(month2 - 1):
        daysTillMonth2 = daysTillMonth2 + monthsDays[i];

    
    days = (year2 - year1) * 365 + days_of_month(month2) - days_of_month(month1) + day2 - day1

    yeartemp = year1;
   
    while(yeartemp < year2+1):
        if CheckLeapYear(yeartemp):
            days += 1;
            yeartemp += 1;
        else:
            yeartemp += 1; 
            
    if CheckLeapYear(year1):
        if month1 > 2:
            days = days - 1
    if CheckLeapYear(year2):
        if month2 < 3:
            days = days - 1        
            
    return days


# In[143]:


day = daysBetweenDates(2011,1,1,2012,8,8)


# In[144]:


def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"


test()





