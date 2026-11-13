from datetime import date


title = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))
event_date = date(year, month, day)

print("\nFormatted Output: ")
print("Event:", title)
print("Date:", event_date)
print("Year:", event_date)
print("Month:", event_date)
print("Day:", event_date)
print("Weekday:", event_date)