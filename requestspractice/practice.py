import requests
import hmac
import hashlib
import base64

base_string = 'GET&http%3A%2F%2Fphotos.example.net%2Fphotos&file%3Dvacation.jpg%26oauth_consumer_key%3Ddpf43f3p2l4k3l03%26oauth_nonce%3Dkllo9940pd9333jh%26oauth_signature_method%3DHMAC-SHA1%26oauth_timestamp%3D1191242096%26oauth_token%3Dnnch734d00sl2jdk%26oauth_version%3D1.0%26size%3Doriginal'
test_key = 'kd94hf93k423kf44&pfkkdhi9sl3r4s00'
digest_maker = hmac.new(test_key, base_string, hashlib.sha1)
digest = digest_maker.digest()
signature = base64.b64encode(digest)

print signature
test_output = 'tR3+Ty81lMeYAr/Fid0kMTYa/WM='
print test_output
print signature == test_output



API_Key = '53384734f261f01e1b5e728f36d77242bdf48eef43f76b19786b12eef5866'
API_Secret = 'b084dd376872378236d3d56191e5de52e3b054d01989551d1464e2d8e7b222'

# TODO: generate key
payload = {'oauth_callback': '127.0.0.1', 'oauth_consumer_key': API_Key,
           'oauth_nonce': My_Nonce, 'oauth_signature': My_Sig, 'oauth_signature_method': 'HMAC-SHA1',
           'oauth_timestamp': My_Timestamp, 'oauth_version': '1.0'}





#r = requests.get('https://api.github.com/events')
r = requests.get('https://example.com')
print r.text
#print r

#>>> payload = {'key1': 'value1', 'key2': 'value2'}
#>>> r = requests.get("http://httpbin.org/get", params=payload)

payload = {'oauth_callback': '127.0.0.1', 'oauth_consumer_key': API_Key,
           'oauth_nonce': My_Nonce, 'oauth_signature': My_Sig, 'oauth_signature_method': 'HMAC-SHA1',
           'oauth_timestamp': My_Timestamp, 'oauth_version': '1.0'}

#r = requests.get("http://httpbin.org/get", params=payload)
r = requests.get("https://oauth.withings.com/account/request_token", params=payload)
"""

