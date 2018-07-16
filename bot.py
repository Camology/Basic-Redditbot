import praw
import configparser
config = configparser.ConfigParser()
config._interpolation = configparser.ExtendedInterpolation()
config.read('config.ini')


keyword = '' #keyword you want to match on		 


bot = praw.Reddit(user_agent=config.get('abc', 'user_agent'),
	client_id=config.get('abc', 'client_id'),
	client_secret=config.get('abc', 'client_secret'),
	username=config.get('abc', 'username'),
	password=config.get('abc', 'password'))
subreddit= bot.subreddit('All') #decide which subs you want to scan for
comments = subreddit.stream.comments() 

for comment in comments:
	text = comment.body #text of the comment you matched on
	author = comment.author #comment author, good if you want to tag the other person
	

	if keyword in text.lower() and author != '': #put username here so you dont match on yourself
		message = ''.join(("hey sexy people i am a robot designed to seduce:",
				   "u/{0} ?".format(author)" ? #tags the author in the post for more fun
		))
		try:
			comment.reply(message) #sends the message
		except praw.exceptions.APIException as e:
			if e.error_type == 'RATELIMIT':
				time.sleep(60) #eventually handle the rate limit in a smarter way
		except Exception as e:
			print(e)
		print(message) #print the message to the console so you an see it too

