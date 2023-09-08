dd = int(input("enter a date of the month "))
mm = input("enter a month of the year ")
year = int(input("enter the year "))
y = (year %100)
c = (y-year)/-100
c = int(c)
y = int(y)

if mm == "january":
    mm = 13
if mm == "february":
    mm = 14
if mm == "march":
    mm = 3
if mm == "april":
    mm = 4
if mm == "may":
    mm = 5
if mm == "june":
    mm = 6
if mm == "july":
    mm = 7
if mm == "august":
    mm = 8
if mm == "september":
    mm = 9
if mm == "october":
    mm = 10
if mm == "november":
    mm = 11
if mm == "december":
    mm = 12
mm = int(mm)
w = dd + 13 * (mm+1) //5 + y + (y/4)+(c/4)-2*c
w = int(w)
w = w%7

if w == 0:
    w = "Saturday"
if w == 1:
    w = "Sunday"
if w == 2:
    w = "Monday"
if w == 3:
    w = "Tuesday"
if w == 4:
    w = "Wednesday"
if w == 5:
    w = "Thursday"
if w == 6:
    w = "Friday"
print(w)