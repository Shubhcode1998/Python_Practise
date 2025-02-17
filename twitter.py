import tweepy

# Set up Twitter API credentials
consumer_key = '9LXNOOpSlgGWMPL64v1DaBLKw'
consumer_secret = 'UXDyPTgEXYupgy0evk96l1UAeVvv787sUMnbc9mURS9QYjfS00'
access_token = '4148247672-pfI4dtHupCR4u9p5jkoj0eGPOYNQ8oizGAcsnjH'
access_token_secret = 'lknWhrACQREWgU8oxDZ3elkNEuYnE1pMAH3XTm17X2JIM'

# Set up the API object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Use the Cursor object to search for tweets with the hashtag #weekendactivities
#tweets = tweepy.Cursor(api.search_tweets, q='#weekendactivities', lang='en', tweet_mode='extended').items(1000)

tweets = api.user_timeline(screen_name='@282f90e1afb0488', count=1000, tweet_mode='extended')

for tweet in tweets:
   print(tweet.full_text)

# # Analyze the data using Pandas and Matplotlib
# import pandas as pd
# import matplotlib.pyplot as plt

# # Create a Pandas DataFrame to store the tweet data
# df = pd.DataFrame(data=[tweet.full_text for tweet in tweets], columns=['Tweets'])

# # Analyze the volume of tweets over time
# df['Timestamp'] = df['Tweets'].apply(lambda tweet: tweet.created_at)
# df['Hour'] = df['Timestamp'].apply(lambda timestamp: timestamp.hour)
# df.groupby('Hour').size().plot(kind='bar')
# plt.title('Volume of Tweets by Hour')
# plt.xlabel('Hour')
# plt.ylabel('Number of Tweets')
# plt.show()

# # Analyze the sentiment of the tweets
# from textblob import TextBlob

# df['Sentiment'] = df['Tweets'].apply(lambda tweet: TextBlob(tweet).sentiment.polarity)
# df.groupby('Sentiment').size().plot(kind='bar')
# plt.title('Sentiment of Tweets')
# plt.xlabel('Sentiment Polarity')
# plt.ylabel('Number of Tweets')
# plt.show()