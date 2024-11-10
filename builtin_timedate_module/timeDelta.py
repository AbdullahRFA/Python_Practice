from datetime import timedelta
from datetime import datetime

# Create a timedelta of 10 days
delta = timedelta(days=10)
print("Timedelta:", delta)

# Add or subtract timedelta to/from a date
today = date.today()
future_date = today + delta
print("Date 10 days from now:", future_date)

past_date = today - delta
print("Date 10 days ago:", past_date)