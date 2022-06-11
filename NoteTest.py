# Need a Catefories command
# 

# This program prints Hello, world!
import discord
# import datetime
# import re
# import numpy as np
# import pandas as pd
import requests 
# import json
# import sys

from urllib.request import urlopen
from bs4 import BeautifulSoup
# from dateutil import parser
# from dateutil import tz
from discord.ext import commands
# from tabulate import tabulate

import json
  
# Opening JSON file
f = open('config.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

bot = commands.Bot(command_prefix = data['prefix'], help_command=None)

#Event to show that bot is ready to use.
@bot.event
async def on_ready():
	print('Bot is ready.')

#Simple command for testing.
@bot.command()
async def ping(ctx):
	await ctx.send(f'Pong! Latency: {round(bot.latency * 1000)}ms')

#Command for printing the standings of a league and season.
@bot.command()
async def category(ctx, category):

    URL = "https://www.randomtriviagenerator.com/#/category/"
    page = requests.get(URL)

    print(page.text)
    
    categories = ["SCIENCE", "GENERAL", "ARTS", "ENTERTAINMENT", "GEOGRAPHY"]
    
    if category.upper() not in categories :
        await ctx.send("Invalid input, please pick from the list of categories.")
        await ctx.send(categories)
        return
	# else:
		#build the url
		# base_url = 'https://www.espn.com/soccer/standings/_/league/' + league
		
	# if season not in seasons :
	    # await ctx.send("Invalid input, please pick from the list of seasons.")
	    # await ctx.send(seasons)
	    # return
	# else:
		# if season != seasons[7] :
			# base_url = base_url + "/season/" + season

	#Open the url
	# page = urlopen(base_url)
	# soup = BeautifulSoup(page.read(), 'html.parser')

	#Go to the section in html that stores the standings
	# table = soup.find_all("tr", {"class": ["Table__TR Table__TR--sm Table__even", "filled Table__TR Table__TR--sm Table__even"]})
	# total = len(table)/2

	#Create an array for the teams in the order they are placed in the standings
	# data = []
	# teams = {} 
	# for x in range(0, int(total)):
		# teams[x] = table[x].abbr["title"]

	#Create arrays for the rest of the stats being scraped
	# matches = {}
	# wins = {}
	# draws = {}
	# loses = {}
	# goalsfor = {}
	# goalsagainst = {}
	# goaldiff = {}
	# points = {}

	#Scrape all the stats by looping through every team
	# for x in range(int(total), int(len(table))):
		# matchstat = table[x].find('span',{'class':'stat-cell'})
		# matches[x-int(total)] = matchstat.text
		# winstat = matchstat.find_next('span',{'class':'stat-cell'})
		# wins[x-int(total)] = winstat.text
		# drawstat = winstat.find_next('span',{'class':'stat-cell'})
		# draws[x-int(total)] = drawstat.text
		# losestat = drawstat.find_next('span',{'class':'stat-cell'})
		# loses[x-int(total)] = losestat.text
		# gfstat = losestat.find_next('span',{'class':'stat-cell'})
		# goalsfor[x-int(total)] = gfstat.text
		# gastat = gfstat.find_next('span',{'class':'stat-cell'})
		# goalsagainst[x-int(total)] = gastat.text
		# gdstat = gastat.find_next('span',{'class':'stat-cell'})
		# goaldiff[x-int(total)] = gdstat.text
		# pointstat = gdstat.find_next('span',{'class':'stat-cell'})
		# points[x-int(total)] = pointstat.text
		
	# for x in range(0, int(total)):
		# data.append([teams[x], matches[x], wins[x], draws[x], loses[x], goalsfor[x], goalsagainst[x], goaldiff[x], points[x]])	
	#print(data)
	#create empty data frame in pandas
	# full_stat = pd.DataFrame(data, columns = ['Team', 'GP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'PTS'])

	#print the results
	# codeblock = "```"
	# await ctx.send(codeblock + tabulate(full_stat, showindex=False, headers=full_stat.columns) + codeblock)
	# print(codeblock + tabulate(full_stat, showindex=False, headers=full_stat.columns) + codeblock)
	# page.close()

@bot.command()
async def help(ctx):
	await ctx.send(f'Usage: !standings [league] [season]')
	await ctx.send(f'Here are a list of supported leagues:')
	await ctx.send(showleagues)
	await ctx.send(f'Here are a list of supported seasons:')
	await ctx.send(seasons)

bot.run(data['token'])

# Closing file
f.close()

# Useful git commands
# 1. git status --This is used to view if you need to add/commit/push files to the repository.
# 2. git add --This is needed to add modified files and have them ready to be committed.
# 3. git commit -m "INSERT YOUR MESSAGE HERE" --This is used to staged your changes and the message needs to be useful.
# 4. git push --set-upstream origin INSERT-BRANCH-NAME <--IF FIRST TIME EVER ON BRANCH otherwrise --> git push
# 5. git log --See previous commits
# 6. git checkout INSERT-BRANCH-NAME --USED TO GO TO A DIFFERENT BRANCH
# 7. git branch --See your current branch/other branches that exist