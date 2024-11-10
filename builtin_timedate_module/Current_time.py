# This Python code snippet demonstrates the usage of the `datetime` module to work with dates and times. Here's a breakdown of what the code does:
from datetime import datetime

# Get the current date and time
now = datetime.now()
print("Current date and time:", now)

# Create a specific date and time
specific_datetime = datetime(2023, 11, 8, 14, 30, 15)
print("Specific date and time:", specific_datetime)

# Access date and time parts
print("Year:", now.year)
print("Hour:", now.hour)
