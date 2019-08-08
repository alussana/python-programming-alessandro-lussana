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
                #period.append(values[1])
                period[i] = values[1]
            elif values[0] == '"day"':
                date = values[1].split('T')
                #day.append(date[0][1:])
                day[i] = date[0][1:]
            elif values[0] == '"pain"':
                #pain.append(values[1])
                pain[i] = values[1]

    return(day, period, pain)

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

## TODO
## o   Pain day predictor
## o   Period start day predictor
## o   Period length predictor