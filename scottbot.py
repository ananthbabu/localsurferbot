import requests, json
import datetime

# date = datetime.datetime.today()
# the_date = date.date()
# print(today_date)

# with open("data.json", 'r') as weather_data:
#     my_data = json.load(weather_data)

url = 'https://magicseaweed.com/api/aa1171867a9a7698c04e99235767afb8/forecast/?spot_id=87'
r = requests.get(url)
my_data = r.json()

convertdate = my_data[10]["localTimestamp"]
dateeightamtmrw = (datetime.datetime.fromtimestamp(
    int(convertdate)
).strftime('%Y-%m-%d %H:%M'))
# print(dateeightamtmrw)

swelldata = my_data[10]["swell"]
# print(thedata)

maxwavesize = swelldata["maxBreakingHeight"]
minwavesize = swelldata["minBreakingHeight"]
avgwavesize = (maxwavesize + minwavesize) / 2
# print("average wave size is", avgwavesize)ls
swellperiod = swelldata["components"]["combined"]["period"]
# print(swellperiod)
swelldir = swelldata["components"]["combined"]["compassDirection"]
# print(swelldir)
winddata = my_data[10]["wind"]
# print(winddata)
windspeed = winddata["speed"]
# print(windspeed)
kmhwind = windspeed * 1.609344
# print(kmhwind, "kmh")
winddirect = winddata["compassDirection"]
# winddirect = "SW"
# print(winddir)
temp = my_data[10]["condition"]["temperature"]
# print(temp)
print("if you go surf tomorrow morning", dateeightamtmrw )
print("expect:")
if winddirect == "SSW" or winddirect == "SW" or winddirect == "WSW" or winddirect == "W" or winddirect == "WNW" or winddirect == "NW" or winddirect == "NNW":
    print("An Offshore Wind  - " + winddirect)
else:
    print("A Kak Onshore - " + winddirect)
#
if temp < 23:
    print("Wear Wetsuit")

else:
    print("Weather is quite warm ", temp,"c")
    print("Wear Boardies")

if avgwavesize < 3.5:
    print("waves should be fun at around ", avgwavesize,"ft")

elif avgwavesize < 2:
    print("Not much swell around")

elif avgwavesize < 6:
    print("Some swell around at ",avgwavesize,"ft")

elif avgwavesize > 6.1:
    print("Gonna be pretty big")

elif avgwavesize > 10:
    print("Gonna be HUGE!!")

