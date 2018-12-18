# Twitter sentiment and subjectivity analysis 
Sentiment/subjectivity analysis on twitter posts using Tweepy, TextBlob, matplotlib

## Dataset information
In order to gather information from twitter I used the tweepy API to collectively create a representative dataset. The
dataset is gathered through searching for posts that contain a relevant keyword. 

This keyword is indicated here as Love.
public_tweets = api.search(q='Love',count = 100)

### Requirements/Dependencies
There are some general library requirements for the project and some which are specific to individual methods.
The general requirements are as follows.


-> <code>Tweepy</code>

-> <code>Textblob</code>

-> <code>Termcolor</code>

-> <code>csv</code>

-> <code>matplotlib.pyplot</code>

-> <code>Twitter account</code>



#### Usage

1. In order to use the code you must have the listed dependencies installed. 
2. Clone the github repo
3. Go to https://developer.twitter.com/en/apps and create new app, fill out information and get Consumer key/secret and access token/secret.
4. Open the twitterSentiment.py file and change the consumer_key, consumer_secret, access_token, and access_key to the twitter app api information you got from the previous step.
5. Open terminal, and run python twitterSentiment.py OR python3 twitterSentimen.py if you have python3 installed.
6. A CSV file will be saved to the local directory including 100 posts, their username, subjectivity level, and sentiment level.
7. A plot will be displayed using the CSV file to visually present sentiment and subjectivity level for the keyword.
