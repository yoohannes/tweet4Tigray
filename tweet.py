import tweepy
import time

api_key="Z8F2Jo1lcjqNlAw2Lpj9NXRFo"
api_secret_key="cSnXgx9S9y5NJiIDV4pia9Wm0XRg4HT7E2WUlabzJShys3AizR"
acess_token="1251029127366430722-lIeDaB08z2BGlFsTjWXQzf7Wa0nX1C"
acess_token_secret="4TVykbPDVBT2rzg77vjn81V1vyaT8mAjRqaQi9SuRThYA"


auth=tweepy.OAuthHandler(api_key,api_secret_key)
auth.set_access_token(acess_token,acess_token_secret)
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
#
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
qouteHASH('#TigrayGenocide',100)