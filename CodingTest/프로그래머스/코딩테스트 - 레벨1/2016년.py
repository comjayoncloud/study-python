from datetime import datetime

def solution(a, b):
    dateDict = {0: 'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
    date = f'2016-{a}-{b}'
    datetime_date = datetime.strptime(date, '%Y-%m-%d')

    return dateDict[datetime_date.weekday()]

solution(5,24)