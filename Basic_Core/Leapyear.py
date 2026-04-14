year=input("Enter thr year in four digit :")
if (len(year)!=4):
    print("Invalid input year")
year=int(year)    
if (year %400 ==0 and year % 100 ==0) or (year %4 ==0):
         print(f"Leap year : {year}")
else:
        print(f"Not a Leap year {year}")
