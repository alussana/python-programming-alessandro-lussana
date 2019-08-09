import datetime

def getLog(cluedata):
    '''
    Read the complete log from cluedata file
    '''
    # read raw data
    rawdata = open(cluedata)
    data = rawdata.read()
    # exclude environment metadata and get log data
    data = data.split(',"data":[{')
    data = data[1]
    
    return(data)

def getDayPeriodPain(log):
    '''
    Scan the output of getLog(); create arrays day, period, pain 
    '''    
    # split daily records
    data = log.split('},{')
    
    n = len(data) - 1
    day = ['NA'] * n
    period = ['NA'] * n
    pain = ['NA'] * n

    # append data to arrays day, period, pain
    for i in range(len(data)):
        record = data[i]
        infolist = record.split(',')

        for info in infolist:
            values = info.split(':')
            if values[0] == '"period"':
                period[i] = values[1]
            elif values[0] == '"day"':
                date = values[1].split('T')
                day[i] = date[0][1:]
            elif values[0] == '"pain"':
                pain[i] = values[1]

    return(day, period, pain)

def countDays(date1, date2):
    """
    Count the number of days between two dates in the form "yy-mm-dd"
    """
    date1 = date1.split("-")
    date2 = date2.split("-")
    day1 = datetime.datetime(year = int(date1[0]), \
        month = int(date1[1]), day = int(date1[2]))
    day2 = datetime.datetime(year = int(date2[0]), \
        month = int(date2[1]), day = int(date2[2]))
    num_of_days = abs(day2 - day1)
    num_of_days = str(num_of_days)
    num_of_days = num_of_days.split(" ")
    num_of_days = num_of_days[0]
    return(num_of_days)

if __name__ == '__main__':
    import sys
    if sys.argv[1]:
        cluedata = sys.argv[1]
    else:
        cluedata = input("Insert cluedata file path:")
    
    # testing some functions
    log = getLog(cluedata)
    day, period, pain = getDayPeriodPain(log)
    print(len(day), len(period), len(day))
    print(len(log.split('},{')))
    for i in range(len(day)):
        print(day[i], period[i], pain[i])
    date1 = "2019-07-13"
    date2 = "2019-07-17"
    print(countDays(date2, date1))

## TODO
## o   Pain day predictor
## o   Period start day predictor
## o   Period length predictor