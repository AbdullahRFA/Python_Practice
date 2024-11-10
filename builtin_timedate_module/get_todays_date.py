# This Python code snippet demonstrates the use of the `date` class from the `datetime` module to work with dates. Here's a breakdown of what the code does:
from datetime import date

# Get today's date
today = date.today()
print("Today's date:", today)

# Create a specific date
specific_date = date(2023, 11, 8)
print("Specific date:", specific_date)

# Access year, month, and day
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)