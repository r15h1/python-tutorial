# Datetime Module
from datetime import datetime

now = datetime.now()

print(now.date())

print(now.year)

print(now.month)

print(now.hour)

print(now.minute)

print(now.second)

print(now.time())

# Getting more control over formatting
# %a abbreviated day of the week: Mon, Tues, Wed
# %A full name of the day of week: Monday, Tuesday, Wednesday
# %d day of month: number 10 for 10th of January
# %b abbreviated month name: Jan, Feb, Mar
# %B full month name: January
# %m month as number: 01 for Jan
# %H hours
# %M minutes
# %S seconds
# %p AM or PM
# %y two number year
# %Y four number year

from datetime import datetime

now = datetime.now()

print(now.strftime("%a %A %d"))

print(now.strftime("%b %B %m"))

print(now.strftime("%A %B %d"))

print(now.strftime("%H : %M : %S %p"))

print(now.strftime("%y %Y"))