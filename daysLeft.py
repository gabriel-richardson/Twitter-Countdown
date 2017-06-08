import tweepy, time, sys

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

count = 15

for i in range(15, -1, -1):
	if count >= 2:
		api.update_status(status = "There are %i days left until LISD is back in school." % count)
	elif count <= 0:
		api.update_status(status = "LISD is back in school.")
		break
	else:
		api.update_status(status = "There is %i day left until LISD is back in school." % count)
	count -= 1
	time.sleep(86400)