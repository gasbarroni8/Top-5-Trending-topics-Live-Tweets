import tweepy
import time
# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=""
consumer_secret=""

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=""
access_token_secret=""


#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
	tweet_counter = 0
	def on_status(self, status):
		MyStreamListener.tweet_counter+=1
		text = str(status.text)
		name = str(status.user.screen_name)
		created = str(status.created_at)
		followers = str(status.user.followers_count)
		if hasattr(status,'retweeted_status'):
				return
		if (MyStreamListener.tweet_counter>=11):
				return False
		if (MyStreamListener.tweet_counter==0):
				return False
		#print(the name)
		print('-'*100)
		print (text,created)
		print("Username: "+ name +", " +followers+" followers")
		print('-'*100)
	def on_error(self, status_code):
	    if status_code == 420:
	        #returning False in on_error disconnects the stream
	        return False

myStreamListener = MyStreamListener()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,timeout=10)
#api.update_status('update status') 
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

print ("We can see live tweets on trending keywords based on location. ")
options = ['Worldwide','New York','Los Angeles','Toronto','New Delhi','Sydney','London','Berlin','Madrid','Rome','Paris']
woeid = [1,2459115,2442047,4118,2295019,1105779,44418,638243,766273,721943,615702]
for i in range(11):
	print(str(i) + ". {}\n".format(options[i]))
num= int(input("Enter number for option:"))
if (num >= 0 and num < 11):
	location = api.trends_place(woeid[num])
else:
	print("Error. Try again later.")

data=(location[0])
wtrends= data['trends']
names = [trend['name'] for trend in wtrends]
print("Here are the top 5 trending keywords worldwide: \n")
for x in range(5):
	print (names[x]+'\n')
print("Here are some live tweets streaming for the 5 trending keywords now: \n")
time.sleep(5)
for x in range(5):
	print ('#'*30+' '+names[x]+' '+'#'*30)
	myStream.filter(track=[names[x]])
	MyStreamListener.tweet_counter = 0
	time.sleep(5)
	
	
	
	
