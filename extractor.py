import json 
import os
from pprint import pprint 

directory = '/Users/lijie/Desktop/spamDetection/TwitterDataCollector-master3/real_users/'

for root, dirs, files in os.walk(directory, topdown = False): 
	for name in files: 				
		if not name.startswith('.'): 
			with open(directory+name) as data_file: 
				data = json.load(data_file)
				followees_count = data["followees_count"]
				followers_count = data["followers_count"]
				if followers_count is not 0: 
					ratio = followees_count / followers_count
					# Tune the benchmark here for spammer definition
					if ratio > 10:  
						pprint(data["screen_name"])



