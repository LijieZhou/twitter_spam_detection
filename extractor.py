import json 
import os
import re
from pprint import pprint 

directory = '/Users/lijie/Desktop/spamDetection/test/real_users/'


for root, dirs, files in os.walk(directory, topdown = False): 
	for name in files: 				
		if not name.startswith('.'): 
			with open(directory+name) as data_file: 
				data = json.load(data_file)
				user_name = data['screen_name']
				# each user write into one output file 
				
				file = open(user_name,'w')


				# Extract URLs from tweets
				all_tweets = data["tweets"]

				for tweet in all_tweets: 
					if 'https://' in tweet:
						# You must encode in 'utf-8' otherwise certain ascii char will throw errors
						file.write(re.search("(?P<url>https?://[^\s]+)", tweet).group("url").encode('utf-8'))
						# Add the "/" so that we can build the URL as required by Google Safe Browsing
						file.write("/") 
						# Format the output line by line 
						file.write("\n")
						
				file.close()





