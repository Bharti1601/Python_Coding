# program to find leap year

year = int(input(" Enter the year :"))   # it takes year as an input  

# check the conditions of the leap year , if all match then print leap year else not a leap year.

if (x % 4) == 0 :
    if(year % 100) == 0 :
        if(year % 400) == 0 :
         
         print ("Year is Leap Year")

        else: 
            print("Year is not a leap year")
    else: 
        print("Year is a leap year")     
else:
    print("Year is not leap year")       

# output will be :

# Enter the year :2000
#Year is Leap Year         


    
