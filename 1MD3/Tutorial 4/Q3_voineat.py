def main():
    month, day, year = eval(input("Please enter month, day, year"))
    print(date(month, day, year))
def date(month, day, year):
    m = ('Jan ', 'Feb ', 'Mar ', 'Apr ', 'May ', 'Jun ', 'Jul ', 'Aug ', 'Sep ', 'Oct ', 'Nov ', 'Dec ')
    return (str(m[month - 1]) + str(day) + ", " + str(year))
main()
