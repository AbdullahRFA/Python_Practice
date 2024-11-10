# Format datetime as a string
from datetime import datetime
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_date)

# Parse a string into a datetime object
parsed_date = datetime.strptime("2023-11-08 14:30:15", "%Y-%m-%d %H:%M:%S")
print("Parsed date and time:", parsed_date)
