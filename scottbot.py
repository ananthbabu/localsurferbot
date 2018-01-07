import requests, json
import datetime

#
# url = 'http://api.worldweatheronline.com/premium/v1/marine.ashx?key=e67e209a3eba498ca11125527180601&q=-30.278797,%2030.762171&format=json&tide=yes'
#
# r = requests.get(url)
#
# raw = r.json()
#
# data = json.dumps(raw['data']['weather'])

# loaded = json.loads(data)

# print(loaded)

get_time = datetime.datetime.today()
today_date = get_time.date()
print(today_date)

with open('data.json') as json_data:
    d = json.load(json_data)

    data = json.dumps(d['data']['weather'])

    loaded = json.loads(data)

for item in loaded:
    for a in item['date']:
        for b in item['astronomy']:
            print(b['sunrise'], item['date'])


