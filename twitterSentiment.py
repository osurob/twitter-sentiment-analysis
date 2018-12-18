import tweepy
from textblob import TextBlob
from termcolor import colored
import csv
import matplotlib.pyplot as plt

consumer_key = 'HR4EshSlrtPkE8vwe4QiGFDdL'
consumer_secret = 'y4a1Vvag21CObVzMKxdkByXXfFDX0q06VocDaNanwGq6F8nU2B'

access_token = '767856757410365440-e0p9CtDau7i8KUQHaHqu2O1dUjVBZCL'
access_token_secret = 'rsQCh3nYPv5JuBJsZLti5xaeGjmjGrgi00nTP3UymMMa0'

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














