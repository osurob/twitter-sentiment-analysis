import tweepy
from textblob import TextBlob
from termcolor import colored
import csv
import matplotlib.pyplot as plt

consumer_key = 'INSERT_KEY_HERE'
consumer_secret = 'INSERT_SECRET_HERE'

access_token = 'INSERT_KEY_HERE'
access_token_secret = 'INSERT_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search(q='Love',count = 100)

with open('tweets_data.csv', mode='w') as tweets_file:
	tweets_writer = csv.writer(tweets_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for tweet in public_tweets:
		print(tweet.text)
		analysis = TextBlob(tweet.text)
		print colored(analysis.sentiment, 'red')
		tweets_writer.writerow([tweet.author.screen_name,tweet.text.encode('utf-8'),analysis.sentiment.polarity,analysis.sentiment.subjectivity])

with open('tweets_data.csv', mode='r') as tweets_file:
	x = []
	y = []
	csv_reader = csv.reader(tweets_file, delimiter=',')
	for row in csv_reader:
		x.append(float(row[2]))
		y.append(float(row[3]))

	plt.scatter(x,y)
	plt.xlabel('Sentiment polarity')
	plt.ylabel('Subjectivity (opinion)')
	plt.show()














