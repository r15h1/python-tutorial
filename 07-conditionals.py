def figure_out_season(month):
    if month in (12,1,2):
        print("winter")
    elif month == 3 or month == 4 or month == 5:
        print("spring")
    elif month <= 8:
        print("summer")
    else:
        print("fall")

month = input("Enter month: ")
figure_out_season(int(month))

#other logical operators:
#not, or, and, >, <, ==, !=, >=, <=, in