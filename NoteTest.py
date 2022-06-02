#1. Get real post
#2. background video
#3. Crop reddit post
#4. Text to speech
#5. Make a git repository
import praw

#creating reddit instance
reddit = praw.Reddit(client_id='9p-bz1BqUVokRNbAQPyxug', client_secret='x192jMMhDYGwnars-0v8AllQg3i7Sg', user_agent='WebScraping')

# get 10 hot posts from the MachineLearning subreddit
hot_posts = reddit.subreddit('TIFU').hot(limit=3)
for post in hot_posts:
    print(post.selftext.encode())
    print("\n\n")