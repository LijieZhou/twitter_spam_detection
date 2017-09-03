import subprocess
import os

directory = '/Users/lijie/go/bin/results/'

for root, dirs, files in os.walk(directory, topdown=False): 
	for name in files: 
		if not name.startswith('.'):
			with open(directory+name) as data_file: 
				content = data_file.readlines()
				

queries = [x.strip() for x in content]


for i in queries: 
	url = i+"apiv4/ANY_PLATFORM/MALWARE/URL/"
	print url
	# social_engineering_url = i+"apiv4/ANY_PLATFORM/SOCIAL_ENGINEERING/URL/"
	# unwanted_software_url = i+"apiv4/ANY_PLATFORM/apiv4/ANY_PLATFORM/SOCIAL_ENGINEERING/URL/"
	# e = 'echo ' + str(url) + '| /Users/lijie/go/bin/sblookup -apikey=AIzaSyD34YoaefwTRTu_Tk4lO_9HUb0Eql5ha_k >> output1.txt'
	e = 'echo ' + str(url) + '| /Users/lijie/go/bin/sblookup -apikey=AIzaSyD34YoaefwTRTu_Tk4lO_9HUb0Eql5ha_k >> output2.txt' 
	subprocess.call(e,shell=True)
