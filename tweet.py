import tweepy
import time
import os 

auth=tweepy.OAuthHandler(os.environ['apiKEY'],os.environ['keySECRET'])
auth.set_access_token(os.environ['acessToken'],os.environ['acessTokenSecret'])
api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
user=api.me()

def qouteHASH(hastag,items):
    likecount=0
    for tweet in tweepy.Cursor(api.search,hastag,tweetmode='extended').items(items):
        try:
            
            tweet.favorite()
            tweet.retweet()
            likecount+=1
            print(str(likecount)+"tweets tweeted")
            time.sleep(5)
            
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


      
qouteHASH('#TigrayGenocide',100)
