#!/usr/bin/env python3

import tweepy
import csv
import random
import os

# VARIABLES

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

csvFileName = "/global2000.csv"

company = ""
country = ""
companies = ""
randomnum = ""

path = os.getcwd()

# LOGIN TWITTER

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# FUNCIONS

def randomfuck():
	global company
	global country
	global companies
	global randomnum

	with open(path + csvFileName) as csv_file:
		csv_reader1 = csv.reader(csv_file, delimiter=',')
		companies = sum(1 for company in csv_reader1) - 1

	with open(path + csvFileName) as csv_file2:
		csv_reader2 = csv.reader(csv_file2, delimiter=',')
		randomnum = random.randint(1,companies)
		line_count = 0
		for row in csv_reader2:
			line_count = line_count + 1
			if line_count == randomnum:
				company = row[1]
				country = row[2]

	with open(path + csvFileName, 'r') as readfile:
		csvReader = csv.reader(readfile)
		clean_rows = []
		line_count = 0
		for row in csvReader:
			line_count = line_count + 1
			if line_count != randomnum:
				clean_rows.append(row)

	with open(path + csvFileName, 'w') as writefile:
		csv_writer = csv.writer(writefile)
		csv_writer.writerows(clean_rows)

def tweetit(company, country):
	tweet = "🖕 Fuck " + company + ", from " + country
	api.update_status(tweet)


randomfuck()
tweetit(company, country)