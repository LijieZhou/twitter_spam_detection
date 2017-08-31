# TwitterDataCollector
This project collects data from Twitter.

# Requirements
'auth.k' file containing:
1. Consumer key
2. Consumer secret
3. Access token
4. Acces token scret

Watch this video to know how to get these keys: https://www.coursera.org/learn/social-media-data-analytics/lecture/rs7Oh/video-3-using-python-to-extract-data-from-twitter

# Features
Collects tweets from Twitter based on specified keywords, collects information about author of the tweet, gets all followers and followees of the author.

# Exceptions

Twitter api provides 15 minutes windows to collect data. RateLimitError is raised when an API method fails due to hitting Twitter’s rate limit. Program sleeps for 15 minutes if RateLimitError is raised.