import json
import re_modified_data_mining
with open('parisAttacks.json','r') as f:
   	for count in range(0,10):
   		line=f.readline()
   		print "\n"
   		tweet=json.loads(line)
   		tweet=re_modified_data_mining.preprocess(tweet['text'])
   		for word in tweet:
   			print(word),