# The MIT License (MIT)

# Copyright (c) 2015 Mustafa EL-Hilo

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from instagram.client import InstagramAPI
from random import randint
import sys
import time
from collections import OrderedDict

client_id = '721cc35baafa4abf9c22a6cd58ac9253'
client_secret = 'bdac16788ab6432ca614a3d8164ff94f'
access_token = '1906277004.721cc35.83458773c49b4fedb4fa3df48a2de95b'
client_ip = '192.168.44.138'

#client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri

api = InstagramAPI(client_id=client_id, client_secret=client_secret, client_ips= client_ip,access_token= access_token)
#from instagram.client import InstagramAPI

#api = InstagramAPI(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET')
#popular_media = api.media_popular(count=3)
#for media in popular_media:
    #print media.images['standard_resolution'].url

#stringmaybe = api.user('goalsstretch')
mymedia = api.user_media_feed()
print mymedia, len(mymedia[0])

f1=open('robswebsite.html', 'w')
print >>f1, '<html>\n<head>\n\n<title>Rob\'s Website!!</title>\n</head>\n\n'
print >>f1, '<body>\n<h1>This is my website!!!!</h1>\n'

for media_obj in mymedia[0]:
    myurl = media_obj.get_standard_resolution_url()
    print myurl, type(myurl)
    print >>f1, '<div><img src="%s" alt="Me stretching"></div>\n' % myurl

print >>f1, '</body>'

