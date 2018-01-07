import requests, json
import datetime

#
# url = ''
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
# print(today_date)

with open('data.json') as json_data:
    d = json.load(json_data)

    data = json.dumps(d['data']['weather'])

    loaded = json.loads(data)

for item in loaded:
    for a in item['date']:
        for b in item['tides']:
            for c in b['tide_data']:
                tide_date = item['date']
                tide_type = c['tide_type']
                tide_time = c['tideTime']
