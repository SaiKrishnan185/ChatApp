import datetime
from guide import modifiedGuideLine


def cleaner(currentTime, a):
    n = 10
    currentTimeC = currentTime.time()
    nextClean = currentTime + datetime.timedelta(minutes=n)
    timeC = currentTime
    print(f'{modifiedGuideLine[a.upper()]} at {currentTimeC.hour}:{currentTimeC.minute}')
    return nextClean, timeC


def newspaper(currentTime, day, a):
    if day != currentTime.day:
        print(modifiedGuideLine[a.upper()])
        day = currentTime.day
        return day
    else:
        print("I think you don't get another newspaper the same day")
        day = currentTime.day
        return day
