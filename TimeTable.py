# main{
#
# getDate()                        (Date)
# getTime()                        (Time)
# GetDay(Date)                     (Day)
# FindPeriod(Time)                 (PeriodNum) 
# FindSubject(Period)              (ThisPeriodStr)
# findSubject(period+1)            (NextPeriodStr)    //Next Period = (Current Period + 1)
# getTimmings(Period)              (ThisPeriodTime)
# getTimmings(period+1)            (NextPeriodTime)
# Output(Date, Time, Day, ThisPeriodStr,ThisPeriodTime, NextPeriodStr, NextPeriodTime)
#
# }

def getDate():
    from datetime import date 

    today = date.today()

    # dd/mm/yyyy
    d1 = today.strftime("%d/%m/%Y")
    return d1

def getTime():
    from datetime import datetime

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    return (current_time)

def getDay(date):
    import datetime
    date = ""
    date += getDate()
    day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
    day = datetime.datetime.strptime(date, '%d/%m/%Y').weekday()
    return (day_name[day])

def getPeriodID(time):

    time = int(time.replace(":", ""))

    if(70000<time<90000):
        return 1    #No class  is going on
    elif(90000<time<94000):
        return 2    #Period 1
    elif(94000<time<94500):
        return 3    #Break 1
    elif(94500<time<102500):
        return 4    #Period 2
    elif(102500<time<103500):
        return 5    #Break 2
    elif(103500<time<111500):
        return 6    #Period 3
    elif(111500<time<112000):
        return 7    #Break 3
    elif(112000<time<120000):
        return 8    #Period 4
    else:           #(120000<time<180000)
        return 9    #No more classes today

def getSubject_ById(ID, day):
    try:
        if (day=="Monday"):
            with open('E:\Programming\On-Going\Python Project\John\Time Table\Database\Mondayv') as database: 
                Lines=database.readlines()
                return(Lines[ID])

        elif (day=="Tuesday"):
            with open('E:\Programming\On-Going\Python Project\John\Time Table\Database\Tuesday') as database:
                Lines=database.readlines()
                return(Lines[ID])

        elif (day=="Wednesday"):
            with open('E:\Programming\On-Going\Python Project\John\Time Table\Database\Wednesday') as database:
                Lines=database.readlines()
                return(Lines[ID])

        elif (day=="Thursday"):
            with open('E:\Programming\On-Going\Python Project\John\Time Table\Database\Thursday') as database:
                Lines=database.readlines()
                return(Lines[ID])
        
        elif (day=="Friday"):
            with open('E:\Programming\On-Going\Python Project\John\Time Table\Database\Friday') as database:
                Lines=database.readlines()
                return(Lines[ID])

        else:
            return("You have no class today")
    
    except:
        print("You have no class after 12'noon nor before 9:00 AM")
        return ("#")

def getTimming(line):
    with open('E:\Programming\On-Going\Python Project\John\Time Table\Database\TIMINGS') as database:
        try:
            Lines=database.readlines()
            return(Lines[line])
        except IndexError:
            return("#")

def getLateTime(time, ID):
    CTime = int(time.replace(':', ''))
    if (90000<CTime<120000):
        with  open('E:\Programming\On-Going\Python Project\John\Time Table\Database\late.txt') as lateData:
            lines=lateData.readlines()
            STime= int(lines[ID])
            late_time = CTime-STime   #gets result in seconds
            #min1 = int(sec/60)
            #sec = int(sec%60)
            #return str("{min}:{sec}".format(min = min1, sec = sec))
            return late_time
    else:
        return (0)

def Output (Date, Time, Day, ThisPeriod, ThisPeriodTime, Late, NextPeriod, NextPeriodTime):

    print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print (" Date        : ", Date)  
    print (" Time        : ", Time)
    print (" Day         : ", Day)
    print ("------------------------------------------------------")
    print (" On-Going    : ", ThisPeriod, " ; Duration : ", ThisPeriodTime, " ; ", Late, "sec have been elapsed!")
    print (" Next Period : ", NextPeriod, " ; Duration : ", NextPeriodTime)
    print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    return

def Quit():
    user_input = input('Quit ?')
    if user_input == 'yes':
        quit
    elif user_input == '1':
        quit
    else:
        if user_input == 'no':
            main()
        elif user_input == '0':
            main()
        else:
            print('Invalid Command, please try again')
            Quit()

def main():
    date                      = getDate()
    Current_time              = getTime()
    day                       = getDay(date)
    ID                        = getPeriodID(Current_time)
    Current_Subject           = getSubject_ById(ID, day)
    Next_Subject              = getSubject_ById((ID+1), day)  #Next_Subject_ID = Current_Subject_ID + 1
    Current_Subject_Duration  = getTimming(ID)
    late                      = getLateTime(Current_time, ID)
    Next_Subject_Duration     = getTimming(ID+1)     #Next_Subject_ID = Current_Subject_ID + 1

    Output (
        date, Current_time, day, Current_Subject, 
        Current_Subject_Duration, late, Next_Subject, 
        Next_Subject_Duration)
    Quit()
main()

# 06/08/2020
# 10:25:51
# Thursday
