from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
access_token="Insert Acces Token"
access_token_secret="Insert access Token Secret"
consumer_key ="Insert Consumer Key"
consumer_secret="Insert Consumer Secrey code"

class StdOutListener(StreamListener):
	def on_data(self,data):
		print data
		return True

	def on_error(self,data):
		print status

if __name__ == '__main__':
	l=StdOutListener()
	auth=OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_token_secret)
	stream=Stream(auth,l)

	stream.filter(track=['#enter the tweet you want to Mine'])
