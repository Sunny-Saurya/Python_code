def leap_year(year):
    if year % 2 == 0 or year % 100 == 0  and year != 400:
        print(year,"is leap year")
    else:
        print(year,"not a leap year")
year = int(input("Enter the year you want to check: "))
leap_year(year)