# This Python code snippet is importing the `timedelta` and `datetime` classes from the `datetime` module. It then gets the current date and time using `datetime.now()`, and calculates the date for yesterday by subtracting one day using `timedelta(days=1)`.
from datetime import timedelta
from datetime import datetime
today=datetime.now()
yesterday=today-timedelta(days=1)

print(today)
print(yesterday)

print('time defference : ',today-yesterday)
