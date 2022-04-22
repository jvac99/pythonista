import tweepy as tw
#import time

with open ('access_token.txt', 'r') as tfile:
    BERER_TOKEN = tfile.readline().strip('\n')
    CONSUMER_KEY = tfile.readline().strip('\n')
    CONSUMER_KEY_SECRET = tfile.readline().strip('\n')
    ACCESS_TOKEN = tfile.readline().strip('\n')
    ACCESS_TOKEN_SECRET = tfile.readline().strip('\n')

# Autenticação
Client = tw.Client(bearer_token=BERER_TOKEN, consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_KEY_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET, wait_on_rate_limit=True)

# Objetivo da API

result = Client.search_recent_tweets(query = 'Cassie', max_results = 10)

data = result.data

for i in data:
    print (i.text)


# Prontinho para fazer o tweet
