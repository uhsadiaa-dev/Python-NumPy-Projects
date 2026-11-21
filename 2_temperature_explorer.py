import numpy as np
import calendar 
#1
days = np.arange(1, 366)
angles = 2*np.pi * (days-1) /365
sinwave = np.sin(angles)
noise = np.random.normal(0,2,365)
a = np.array([-1,0,1])
b = np.array([17, 25, 33])
seasonal_temp =np.interp(sinwave,a,b)
actual_temp = seasonal_temp + noise 
#2
organise = np.array(actual_temp[:360]).reshape(12,30)
monthlymean = np.mean(organise,axis=1)
maximumtemp = np.max(organise,axis =1)
minimumtemp = np.min(organise,axis=1)
#3
months= list(calendar.month_name)[1:]
hottestmonth = np.argmax(monthlymean)
coolestmonth = np.argmin(monthlymean)
#4
lowten = np.count_nonzero(organise<10)
highthirty = np.count_nonzero(organise>30)
#5
farenheit = (actual_temp* 9/5) + 32 
#6
windows = np.ones(7)/7
weeklyavg = np.convolve(actual_temp,windows,mode = 'valid')
#7
yearly = np.mean(actual_temp)
#8
def analysis():
    print(f"Hottest Month        : {months[hottestmonth]} ({np.max(monthlymean):.2f}°C)")
    print(f"Coldest Month        : {months[coolestmonth]} ({np.min(monthlymean):.2f}°C)")
    print(f"Days above 30°C      : {highthirty}")
    print(f"Days below 10°C      : {lowten}")
    print(f"Yearly Average Temp  : {yearly:.2f}°C ({(yearly* 9/5) + 32:.2f}°F)")

while True:
    print("---------------------------------------------------------")
    print("#Temperature Data Explorer#")
    print("1. Simulate yearly temperature data")
    print("2. View monthly temperature statistics")
    print("3. Find hottest and coldest months")
    print("4. Count days above 30°C and below 10°C")
    print("5. Convert Celsius to Fahrenheit")
    print("6. Calculate 7-day moving average")
    print("7. Find yearly average temperature")
    print("8. View complete analysis")
    print("9. Exit")
    print("----------------------------------------------------------")
    try:
        choose = int(input("choose the option from above:"))
        if choose ==1 :
            print("--- Daily Temperatures (°C) ---")
            print(actual_temp)
        elif choose ==2:
            print(f"{'Month':<10}{'Mean':<10}{'Maximum':<10}{'Minimum':<10}")
            for i in range(12):
                print(f"{months[i]:<10}{monthlymean[i]:<10.2f}{maximumtemp[i]:<10.2f}{minimumtemp[i]:<10.2f}")  
        elif choose ==3:
            print(f"Hottest month :{months[hottestmonth]}")
            print(f"Coolest month :{months[coolestmonth]}")
        elif choose ==4:
            print("Days below 10°C",lowten)
            print("Days above 30°C",highthirty)
        elif choose ==5:
            print(farenheit)
        elif choose ==6:
            print("=====weekly moving average=====")
            print(weeklyavg)
        elif choose ==7:
            print("The yearly average is",yearly)
        elif choose ==8:
            analysis()
        elif choose ==9:
            print("Have a good day!!")
            break
        else:
            print("Please enter a number from above.")
        
    except ValueError:
        print("Invalid choice!!")
