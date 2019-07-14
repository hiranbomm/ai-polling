import tweepy
import re



class TwitterData(object):


    def __init__(self, candidates):
        self.all_tweets = []
        self.API = None
        self.polarity = None
        self.positive = None
        self.negative = None

        # self.candidates = candidates


    def authorize(self):
        try:
            # keys deleted for privacy


            authorized = tweepy.OAuthHandler(consumerKey, consumerSecret)
            authorized.set_access_token(accessKey, accessSecret)

            self.API = tweepy.API(authorized) # , wait_on_rate_limit=True)

        except:
            print("ERROR: AUTHENTICATION FOR API FAILED")


    def getData(self, candidate, NUM_TWEETS):
        print("getting tweets")
        self.all_tweets.clear()

        # for each tweet returned, get rid of unwanted symbols and add it to all_tweets
        for tweet in tweepy.Cursor(self.API.search, q=candidate, lang='en').items(NUM_TWEETS):
            text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(RT)", " ", tweet.text).split())
            self.all_tweets.append(text) # .encode('utf-8'))

        print("done getting data")
