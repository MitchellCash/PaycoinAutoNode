#!/usr/bin/python
import os

def server_uptime():

     try:
         f = open("/proc/uptime")
         contents = f.read().split()
         f.close()
     except:
        return "Cannot open uptime file: /proc/uptime"

     total_seconds = float(contents[0])

     # Helper vars:
     MINUTE = 60
     HOUR = MINUTE * 60
     DAY = HOUR * 24

     # Get the days, hours, etc:
     days = int(total_seconds / DAY)
     hours = int((total_seconds % DAY) / HOUR)
     minutes = int((total_seconds % HOUR) / MINUTE)

     # Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
     string = ""
     if days > 0:
         string += str(days) + " " + (days == 1 and "day" or "days") + ", "
     if len(string) > 0 or hours > 0:
         string += str(hours) + " " + (hours == 1 and "hour" or "hours") + " and "
     if len(string) > 0 or minutes > 0:
         string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes")
     return string;
