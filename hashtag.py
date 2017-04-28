################################################################################
################################################################################
####																		####
####		                 Hashtag RT Bot v1.0						
####		            Created by Mathew Hutchison						
####			 		 Retweets about x hashtags					
####							Python 3.5.2							
####																		####
################################################################################
################################################################################

import tweepy
from time import sleep
from config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print(':: Hashtag RT Script ::')
print('Input a hashtag and will retweet tweets relating to that tag every minute, or until script is stopped.\n\n')


hashtag = input('Enter a hashtag to RT: ')

# RTs about inputted tag

for tweet in tweepy.Cursor(api.search, q=hashtag).items() :
	try:
		# Confirms a tweet has been retweeted, also prints the user who made the tweet
		print('\nTweet by: @' + tweet.user.screen_name)
		print('Retweeted about: ' + hashtag)
			
		# Retweet random tweet
		tweet.retweet()

		# Works in seconds, can change for less frequents RTs
		sleep(60)

	except tweepy.TweepError as e:
		print(e.reason)

	except StopIteration:
		break
