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
            time.sleep(20)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
#use drafts instead ,log it 2
userid=[]
for users in tweepy.Cursor(api.friends).items():
        countretNlike=0
        #print(users.name)
        userid.append(users.id)
def likeNretweet(userid):
    for friends in userid:
        for tweet in tweepy.Cursor(api.user_timeline,user_id=friends ,count=10,include_rts=True,exclude_replies=True).items(10):
            try:
            
                #tweet.favorite()
                tweet.retweet()
                #print(tweet.text)
                countretNlike=+1
                print(str(countretNlike)+"done")
                time.sleep(60)
            except tweepy.TweepError as e:
                print(e)        
qouteHASH('#TigrayGenocide',150)
