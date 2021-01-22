import tweepy
import time

auth = tweepy.OAuthHandler('UsQkrWHGmLNUu9PHEttrt6OGV','MLkHGxZVNmdmmS1lXPgNgWJYPbdDbv2t9rZ0jKBdbFYaQeittttYt')
auth.set_access_token('1352429613167730692-ZgplBGCoEUgF7fzhrtrqHxfISlz2BR','8LNVT3fBDHSrtrtrtsJ9WzHbCB9Iy5oVtJEpCFn2Ft')

api = tweepy.API(auth)
file_name = "last_seen_id.txt" //File to store tweet IDs so we do not repeat through a tweet.

def retrieve_last_seen_id(file_name): 
    f_read = open(file_name, 'r')
    last_seen_id = str(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply_to_them():    
    last_seen_id = retrieve_last_seen_id(file_name)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    
    for mention in reversed(mentions):
        
        if "#tweetbaba" in mention.full_text.lower():
            last_seen_id = mention.id
            store_last_seen_id(last_seen_id, file_name)
            api.update_status('@' + mention.user.screen_name + 'Hey, I can see you :)', mention.id)

while True:
    reply_to_them()
    time.sleep(20)
