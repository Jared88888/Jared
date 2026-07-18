#original buggy code
# while True:
# date = input("Enter the date (DD-MM-YYYY): ")
#     test = date
#     if len(test)= 10 and test[2]=="-" and test[5]=="-":
#         day = int(test[0:2])
#         month = int(test[3:])
#         year = int(test[6:])
#         check_year = year>1900 and year<=2000
#         check_month = month>=1 or month<=12
#         check_day_31 = day<=31 and (month in [1,3,5,7,8,10,12])
#         check_day_30 = day<=31 and (month in [4,6,9,11])
#         check_day_Feb = month == 0 and ((day<=29 and year%4==0) or day<=28)
#         if check year:
#             if check_month:
#                 if check_day_31 or check_day_30 or check_day_Feb
#                     break
#                 else:
#                     print("Error in day")
#             else:
#                 print("Error in year")
#         else:
#             print("Error in month")
#     else:
#         print(Error in format")
# print("Date accepted")


while True: #1, indent
    date = input("Enter the date (DD-MM-YYYY): ")
    test = date #2, indent
    if len(test) == 10 and test[2]=="-" and test[5]=="-": #3, change to ==
        day = int(test[0:2])
        month = int(test[3:5]) #4, end at 5
        year = int(test[6:])
        check_year = year>=1900 and year<=2026 #8 change to 2026 #10 change to >=
        check_month = month>=1 and month<=12 #9 change or to and
        check_day_31 = day<=31 and (month in [1,3,5,7,8,10,12])
        check_day_30 = day<=30 and (month in [4,6,9,11]) #11, change to 30
        check_day_Feb = month == 2 and ((day<=29 and year%4==0) or month == 2 and day<=28) #12, month change to 2, #13 add or month ==2
        if check_year: #5, add underscore to make it correct variable name
            if check_month:
                if check_day_31 or check_day_30 or check_day_Feb: #6, add :
                    break
                else:
                    print("Error in day")
            else:
                print("Error in month. ") #15, change to month
        else:
            print("Error in year. ") #14, change to year
    else:
        print("Error in format") #7 add "
print("Date accepted")