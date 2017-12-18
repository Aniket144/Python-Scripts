import sys 			# A basic interpreter that can handle low level functions of Computer OS
import operator		# For Arithmetic & Operations
import requests		# To make HTTP requests
import json			# For JSON
import twitter		# Twitter API	
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights
					# Package needed to interact with Personality Insights API
def analyze(handle):				
	twitter_consumer_key = ''
	twitter_consumer_secret = ''
	twitter_access_token = ''
	twitter_access_secret = ''
	twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)
	text = b''
	statuses = twitter_api.GetUserTimeline(screen_name=handle,count=200,include_rts=False)
	for status in statuses:
		if(status.lang == 'en'):
			print (status.text.encode('utf-8'))
    #The IBM Bluemix credentials for Personality Insights!
	pi_username = ''
	pi_password = ''
	personality_insights = PersonalityInsights(username=pi_username, password=pi_password)
	pi_result = personality_insights.profile(text)
	return pi_result

def flatten(orig):
    data = {}
    for c in orig['tree']['children']:
        if 'children' in c:
            for c2 in c['children']:
                if 'children' in c2:
                    for c3 in c2['children']:
                        if 'children' in c3:
                            for c4 in c3['children']:
                                if (c4['category'] == 'personality'):
                                    data[c4['id']] = c4['percentage']
                                    if 'children' not in c3:
                                        if (c3['category'] == 'personality'):
                                                data[c3['id']] = c3['percentage']
    return data

def compare(dict1, dict2):
    compared_data = {}
    for keys in dict1:
        if dict1[keys] != dict2[keys]:
            compared_data[keys]=abs(dict1[keys] - dict2[keys])
    return compared_data

print("Enter Your Twitter Handle")
user_handle = input()
print("Enter celebrity's Twitter Handle")
celebrity_handle = input()

#user_handle = "@Codecademy"
# celebrity_handle = "@IBM"

user_result = analyze(user_handle)
celebrity_result = analyze(celebrity_handle)

#First, flatten the results from the Watson PI API
user = flatten(user_result)
celebrity = flatten(celebrity_result)

#Then, compare the results of the Watson PI API by calculating the distance between traits
compared_results = compare(user,celebrity)

sorted_result = sorted(compared_results.items(), key=operator.itemgetter(1))

for keys, value in sorted_result[:5]:
	print (keys)
	print(user[keys]),
	print ('->'),
	print (celebrity[keys]),
	print ('->'),
	print (compared_results[keys])