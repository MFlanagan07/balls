dd = int(input("enter a date of the month "))
mm = int(input("enter a month as a number "))
y = int(input("enter a year "))
y = y%100
c = y - (y%100)/100
a = dd
b = 13*(mm+1)//5
a1 = y
a2 = y/4
a3 = c/4
a4 = 2*c
w = (a+b+a1+a2+a3-a4)%7
w = int(w)
print(type(w))
if w == 0:
    w ="Saturday"
if w == 1:
    w ="Sunday"
if w == 2:
    w ="Monday"
if w == 3:
    w ="Tuesday"
if w == 4:
    w ="Wednesday"
if w == 5:
    w ="Thursday"
if w == 6:
    w ="Friday"
print(w)
