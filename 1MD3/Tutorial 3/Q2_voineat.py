def minutes(days, hours, minutes):
    print( "Minutes: " , (days * 24 * 60) + (hours * 60) + minutes )
def daysHoursMinutes(minutes):
    days = minutes // (24 * 60)
    hours = (minutes - (days * 24 * 60)) // 60
    minutes = (minutes - (days * 24 * 60)) % 60
    print( "Days: " , days , " Hours: " , hours , " Minutes: " , minutes)
def main():
    m2d = eval(input("Enter minutes to convert to days"))
    daysHoursMinutes(m2d)
    d, h, m = eval(input("Enter days, hours, minutes to convert to minutes"))
    minutes(d, h, m)
main()
#Tested 1563 minutes converted to 1 day, 2 hours, 3 minutes
#Tested 1 day, 2 hours, 3 minutes, converted to 1563 minutes
#Compared results to website http://www.easysurf.cc/utime.htm#dhmtom
#Confirmed correct
