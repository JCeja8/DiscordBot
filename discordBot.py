import discord
import json
import requests

from discord.ext import commands

# Opening and loading JSON file
f = open('config.json')
data = json.load(f)

# Initializing discord bot
bot = commands.Bot(command_prefix = data['prefix'], help_command=None)

#Event to show that bot is ready to use.
@bot.event
async def on_ready():
	print('Bot is ready.')

#Simple command for testing.
@bot.command()
async def ping(ctx):
	await ctx.send(f'Pong! Latency: {round(bot.latency * 1000)}ms')

@bot.command()
async def help(ctx):
	await ctx.send(f'Usage: !standings [league] [season]')
	await ctx.send(f'Here are a list of supported leagues:')
	await ctx.send(showleagues)
	await ctx.send(f'Here are a list of supported seasons:')
	await ctx.send(seasons)

# Webscrape and output the stock information.
@bot.command()
async def stock(ctx, stock):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    URL = 'https://query1.finance.yahoo.com/v7/finance/quote?lang=en-US&region=US&corsDomain=finance.yahoo.com&symbols=' + stock
    stockInfo = requests.get(URL, headers = headers)
	
    # Change the output to be a dictionary value from the psudeo json that we get.
    stockData = json.loads(stockInfo.text)        # Load up the json
    stockData = stockData["quoteResponse"]      # Strip off the first two sections
    stockData = stockData["result"]
    stockData = str(stockData).lstrip("[").rstrip("]")  # Make valid dictionary format
    stockData = stockData.replace("'",'"').replace("True",'"True"').replace("False",'"False"')
    try:
        stockData = json.loads(stockData)
    except:
        await ctx.send("Error: Invalid ticker symbol")
        return
        
    if stockData.get('regularMarketChangePercent',0) < 0:
        upDown = 'down by'
    elif stockData.get('regularMarketChangePercent',0) > 0:
        upDown = 'up by'
    else:
        upDown = 'unchanged at'

    # marketState can be PRE, REGULAR, POST or POSTPOST or CLOSED
    if stockData.get('marketState','err') == 'PRE':
        txt = "{} closed yesterday at {:.2f} {} {:.2f}%. Yesterday's range was {}."
    elif stockData.get('marketState','err') == 'REGULAR':
        txt = "{} is currently at {:.2f} {} {:.2f}%. The day's range so far is {}."
    else:
        txt = "{} closed at {:.2f} {} {:.2f}%. The day's range is {}."
      
    await ctx.send(txt.format(stockData.get('symbol','err'),stockData.get('regularMarketPrice',0),upDown,stockData.get('regularMarketChangePercent',0),stockData.get('regularMarketDayRange','err')))

bot.run(data['token'])

# Closing file
f.close()