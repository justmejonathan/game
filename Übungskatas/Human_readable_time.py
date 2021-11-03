# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
import math
def make_readable(seconds):
    clock_seconds = round(((seconds/60) - (math.floor(seconds/60)))*60) #amount of seconds in range of 60
    minutes = round((seconds/60) - ((seconds/60) - math.floor(seconds/60))) #amount of minutes
    clock_minutes = round(((minutes/60) - (math.floor(minutes/60)))*60) # amount of minutes in range of 60
    clock_hours = round((minutes/60) - ((minutes/60) - math.floor(minutes/60)))# amount of hours in range of 60
    # adding zeros when necessary
    if len(str(clock_seconds)) == 0:
        clock_seconds = "00"
    elif len(str(clock_seconds)) == 1:
        clock_seconds = "0"+str(clock_seconds)
    else:
        pass
    if len(str(clock_minutes)) == 0:
        clock_minutes = "00"
    elif len(str(clock_minutes)) == 1:
        clock_minutes = "0"+str(clock_minutes)
    else:
        pass
    if len(str(clock_hours)) == 0:
        clock_hours = "00"
    elif len(str(clock_hours)) == 1:
        clock_hours = "0"+str(clock_hours)
    else:
        pass
    print(str(clock_hours) + ":" + str(clock_minutes) + ":" + str(clock_seconds))


make_readable(277753)
