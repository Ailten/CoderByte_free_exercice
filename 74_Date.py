
# Date (None).
# (None)

# use Date.

import datetime
d = datetime.datetime.now()  # get obj datetime (now).
print(f'datetime: {d}')  # print datetime (repr), default format.
print(f'year: {d.year}')  # print year.
print(f'minyear: {datetime.MINYEAR}')  # min year (can be store in datetime).
print(f'maxyear: {datetime.MAXYEAR}')

d = datetime.datetime.today()  # same as .now().
print(f'today: {d}')
d = datetime.date(  # get a date by sending all params.
    year=2010, 
    month=1, 
    day=25
)
print(f'year: {d.year}')  # get year from a date (1~9999).
print(f'month: {d.month}')  # get month from a date (1~12).
print(f'day: {d.day}')  # get day from a date (1~31).
print(f'dayOfWeek: {d.weekday()}')  # return the index day on the week (0~6).
# d.isoweekday()  # same, but from 1 (1~7).
d.replace(day=12)  # edit day, month or year on a date obj (set value).
str_d = d.strftime("%d/%m/%Y")  # format a date in string.
print(f'strdate: {str_d}')
d = datetime.date.today()  # today in date format.
#d = datetime.date.fromtimestamp(timestamp)  # cast a timestamp into date (need a timestamp).

# d - d  # return a timestamp (or deltatime).
# d < d  # return a bool.

# datetime.date  # date (without time).
# datetime.time  # time (without date).
# datetime.timedelta  # delay between two obj (date, datetime, time).

delta = datetime.timedelta(  # set a delay (timedelta), with all params (additiv).
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(f'timedelta: {delta}')
print(f'days: {delta.days}')  # get days from timedelta.
print(f'sec: {delta.seconds}')  # get sec from timedelta (only those under days values, like modulo (?)).
print(f'sectotal: {delta.total_seconds()}')  # get all sec from timedelta.

print(f'maxdelta: {datetime.timedelta.min}')  # min value for a deltatime.
print(f'maxdelta: {datetime.timedelta.max}')  # max value for a deltatime.


# impor time.
# dt.date.fromtimestamp(time.time())  # get today date, from time now.