from datetime import date
from datetime import datetime
today = date.today()
print("Today's date is: ", today)

my_date = date(1996, 12, 11)

print("Date passed as argument is", my_date)
print(today.day)
print(today.month, today.year)


date_time = datetime.fromtimestamp(4366323245)
print("date time from time stamp: ", date_time)

today1 = date.today()
Str = date.isoformat(today1)
print("string representation: ", Str)

current = datetime.now()
print(current)

Set = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(Set)
print("\nElements of set: ")
for i in Set:
    print(i, end =" ")
print()
