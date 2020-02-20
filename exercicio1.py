import datetime as dt

def dias_de_vida():
    year = int(input('Enter a year: '))
    month = int(input('Enter a month: '))
    day = int(input('Enter a day: '))
    date1 = dt.date(year, month, day)
    total_dias = dt.date(2020, 10, 15) - date1
    return print('Seu total de dias de vida é: ',total_dias)

dias_de_vida()
