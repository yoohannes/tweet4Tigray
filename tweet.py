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
