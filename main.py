# nested and ladder condtions of else if

temp = float(input('What is todays temperature ? '))
season = input('Which season is now ? Enter W for Winter and S for Summer: ')
# print(temp)
if season == 'W':
    if temp <= 5:
        print("Stay Inside the House.")
    elif 5 < temp < 25:
        print("Go for Tea.")
    else:
        print(f"Today Temperature is {temp}")
else:
    if temp < 10:
        print("Time for Tea.")
    elif temp > 20:
        print("Swimming Time")
    else:
        print(f"{temp}.C in {season}. Best Time for Bike Ride")

