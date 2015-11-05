#!/usr/bin/python

import time

TIMEFORMAT = "%m/%d/%y %H:%M:%S"
INTERVAL = .5

def getTimeList():
    statFile = file("/proc/stat", "r")
    timeList = statFile.readline().split(" ")[2:6]
    statFile.close()
    for i in range(len(timeList))  :
        timeList[i] = int(timeList[i])
    return timeList

def deltaTime(interval)  :
    x = getTimeList()
    time.sleep(interval)
    y = getTimeList()
    for i in range(len(x))  :
        y[i] -= x[i]
    return y

def cputotal():
        dt = deltaTime(INTERVAL)
        timeStamp = time.strftime(TIMEFORMAT)
        cpuPct = 100 - (dt[len(dt) - 1] * 100.00 / sum(dt))
        total = str('%.0f' %cpuPct)
        return total
