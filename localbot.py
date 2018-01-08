import telegram
import telegram.ext
from telegram.ext import Updater, CommandHandler
import requests
from telegram.ext.dispatcher import run_async
import datetime
import json

teltoken = "536741613:AAEWapwGJEM3zmqBW6qS05RgOnCtnkee1Bw"

bot = telegram.Bot(token=teltoken)
updater = Updater(token=teltoken)


def start(bot, update):

    send = lambda x: bot.sendMessage(chat_id=update.message.chat_id, text=x)

    send("Howzit bru 😎 ")
    send("Tomorrow's forecast will be sent every night at 8pm")
    send("For an on demand report, send me /update and I will be right back at you")
    send("cheers!")


def check(bot, update):

    send = lambda x: bot.sendMessage(chat_id=update.message.chat_id, text=x)

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
    # send("if you go surf tomorrow morning", dateeightamtmrw)
    # print("expect:")
    if winddirect == "SSW" or winddirect == "SW" or winddirect == "WSW" or winddirect == "W" or winddirect == "WNW" or winddirect == "NW" or winddirect == "NNW":
        offshore = ("An Offshore Wind  - " + winddirect)
    else:
        offshore = ("A Kak Onshore - " + winddirect)
    #
    if temp < 23:
        wetsuit = ("Wear your wetsuit, it will be chilly")

    else:
        wetsuit = ("Nice and warm. ")
        wetsuit = ("Wear Boardies")

    if avgwavesize < 3.5:
        waves = ("There's a little bit of swell.")

    elif avgwavesize < 2:
        waves = ("Not much swell around.")

    elif avgwavesize < 6:
        waves = ("There's some swell. Go surf.")

    elif avgwavesize > 6.1:
        waves = ("Gonna be pretty big")

    elif avgwavesize > 10:
        waves = ("Gonna be HUGE!!")

    send("Forecast for tomorrow at 8AM")
    send(dateeightamtmrw)
    send("Expect the following: ")
    send(offshore)
    send(wetsuit)
    send(waves)



def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("check", check))


    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
