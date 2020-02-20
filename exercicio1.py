import datetime as dt

def dias_de_vida():
    year = int(input('Enter a year: '))
    month = int(input('Enter a month: '))
    day = int(input('Enter a day: '))
    date1 = dt.date(year, month, day)
    total_dias = dt.date(2020,2,20) - date1
    return print('Your total of life days is: ',total_dias)

dias_de_vida()
