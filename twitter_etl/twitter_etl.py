import tweepy
import pandas as pd
from datetime import datetime
import s3fs


consumer_key = "IZPBTz1Hz5Xf4gdEt7eMPA415"
consumer_secret  = "LoUodIiHkHrZrpORMOubBGFpOJPITYzd9K5I0fHhb4dRqSotDu"
access_token  = "327683901-ZJLlVt9FeEEtnYlAQrajQtPyKaZtGHHTGuYXz9TS"
access_token_secret  = "2Xk7RCkIdZlDG2ieP4UadK2jRN9aYQj8Ivdl4pXqTH0KZ"


auth = tweepy.OAuth1UserHandler(
  consumer_key, 
  consumer_secret, 
  access_token, 
  access_token_secret
)

api = tweepy.API(auth)
#print(api.get_user(screen_name='elonmusk'))
print(api)
#user2 = api.get_user(screen_name='shambhav02')
#print(user2)
#me = api.home_timeline()
#print(me)
tweets = api.user_timeline(

    screen_name = '@elonmusk',
   count=200,
    include_rts = False,
    tweet_mode = 'extended'
)
#print(tweets)

tweet_list =[]

for tweet in tweets:
    text = tweet._json["full_text"]

    refined_tweet = {
                 "user": tweet.user.screen_name,
                 "text": text,
                 "followers_count": tweet.user.followers_count,
                 "retweet_count" : tweet.retweet_count,
                 "created_at": tweet.user.created_at


    }
    tweet_list.append(refined_tweet)
#print(tweet_list)
df = pd.DataFrame(tweet_list)
df.to_csv("elonmusk.csv")