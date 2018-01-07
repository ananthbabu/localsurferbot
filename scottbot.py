import requests, json
import datetime

date = datetime.datetime.today()
the_date = date.date()
# print(today_date)

with open("data.json", 'r') as weather_data:
    my_data = json.load(weather_data)

    tmrw_data = my_data['data']['weather'][2]
    tmrwdate = tmrw_data['date']

    nineamdata = tmrw_data['hourly'][5]
    timespot = nineamdata['time']
    swellsize = nineamdata['swellHeight_ft']
    swellperiod = nineamdata['swellPeriod_secs']
    winddirect = nineamdata['winddir16Point']
    windspeed = nineamdata['windspeedKmph']
    tempnine = nineamdata['tempC']
    watertemp = "waterTemp_C"

    # print(winddirect)

    print("if you go surf at: " + timespot + " on " + tmrwdate)
    print("expect:")

    if winddirect == "SSW" or winddirect == "SW" or winddirect == "WSW" or winddirect == "W" or winddirect == "WNW" or winddirect == "NW" or winddirect == "NNW":
        print("good wind - " + winddirect)
    else:
        print("shit wind - " + winddirect)

    if tempnine < "20" or watertemp < "23":
        print("wear wetsuit")

    else:
        print("wear boardies")

    # print(nineamdata)
