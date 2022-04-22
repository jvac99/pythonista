from os import read, write
import tweepy
import time
import random

# https://docs.tweepy.org/en/stable/getting_started.html
API_KEY = ''
API_KEY_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# Autenticação
auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Objetivo da API
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Prontinho para fazer o tweet

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def random_phrase():
    p1 = ['Bom', 'Feliz', 'Alegre', 'Adorável', 'Agradável', 'Acessível', 'Cansativo', 'Bonito', 'Chato']
    p2 = [' dia', ' noite', ' ano', ' semana', ' tarde', ' feriado', ' aniversário', ' trabalho']

    genius_phrase = random.choice(p1) + random.choice(p2)
    return genius_phrase

def _main_():
    read_last_seen_str = str(read_last_seen(FILE_NAME))
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode = 'extended')
    print('Ultimo ID pesquisado:' + read_last_seen_str)
    for tweet in reversed(tweets):
        store_last_seen(FILE_NAME, tweet.id)
        genius_phrase = random_phrase()
        api.update_status('@'+ tweet.user.screen_name + ' ' + genius_phrase, in_reply_to_status_id=tweet.id)

while True:
    _main_()
    time.sleep(60)
