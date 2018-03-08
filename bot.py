import praw

keyword = '' #keyword you want to match on		 

bot = praw.Reddit(user_agent='', #same as username
	              client_id='', #comes from registration
	              client_secret='', #comes from registration
	              username='', #username
	              password='') #password
subreddit= bot.subreddit('All') #decide which subs you want to scan for
comments = subreddit.stream.comments() 

for comment in comments:
	text = comment.body #text of the comment you matched on
	author = comment.author #comment author, good if you want to tag the other person
	

	if keyword in text.lower() and author != '': #put username here so you dont match on yourself
		message = ''.join(("hey sexy people i am a robot designed to seduce:",
				   "u/{0} ?".format(author)" ? #tags the author in the post for more fun
		))
		comment.reply(message) #sends the message
		print(message) #prints to console for fun

