from instagram.client import InstagramAPI
from random import randint
import sys
from collections import OrderedDict

client_id = '721cc35baafa4abf9c22a6cd58ac9253'
client_secret = 'bdac16788ab6432ca614a3d8164ff94f'
access_token = '1906277004.721cc35.83458773c49b4fedb4fa3df48a2de95b'
client_ip = '192.168.44.138'


api = InstagramAPI(client_id=client_id, client_secret=client_secret, client_ips= client_ip,access_token= access_token)

media_all_ids=[]

#get recent media ids with the tag "instadogs", only get the most recent 80
#tag_recent_media returns 2 variables, the media ID in an array and the next
#url for the next page
media_ids,next = api.tag_recent_media(tag_name='instadogs', count=80)

#obtain the max_tag_id to use to get the next page of results
temp,max_tag=next.split('max_tag_id=')
max_tag=str(max_tag)

for media_id in media_ids:
	media_all_ids.append(media_id.id)

counter = 1

#the while loop will go through the first 3 pages of resutls, you can increase this
# but you also need to increase the count above.
while next and counter < 3 :
	more_media, next = api.tag_recent_media(tag_name='instadogs', max_tag_id=max_tag)
	temp,max_tag=next.split('max_tag_id=')
	max_tag=str(max_tag)
	for media_id2 in more_media:
		media_all_ids.append(media_id2.id)
	print len(media_all_ids)
	counter+=1

#remove dublictes if any.
media_all_ids=list(OrderedDict.fromkeys(media_all_ids))

print len(media_all_ids)

