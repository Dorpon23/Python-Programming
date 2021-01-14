def weather_conditions(temp):
    if temp > 7:
        print("Warm")
    else:
         print("Cold")


x = int(input("Enter a temparature"))
weather_conditions(x)
