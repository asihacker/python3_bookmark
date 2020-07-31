import datetime

now = datetime.datetime.now()
year = datetime.datetime.strftime(now, '%Y')
hms = datetime.datetime.strftime(now, '%H:%M:%S')
ebay_time = datetime.datetime.strptime(f'Mon 3 Aug {year} {hms}', '%a %d %b %Y %H:%M:%S')
print((ebay_time - now).days)
