import praw

keyword = ''		 

bot = praw.Reddit(user_agent='',
	              client_id='',
	              client_secret='',
	              username='',
	              password='')
subreddit= bot.subreddit('All')
comments = subreddit.stream.comments()

for comment in comments:
	text = comment.body
	author = comment.author
	

	if keyword in text.lower() and author != '':
		message = ''.join(("hey sexy people i am a robot designed to seduce"

		))
		comment.reply(message)
		print(message)

