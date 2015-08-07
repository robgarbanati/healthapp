from withings import WithingsAuth, WithingsApi

auth = WithingsAuth("53384734f261f01e1b5e728f36d77242bdf48eef43f76b19786b12eef5866", "b084dd376872378236d3d56191e5de52e3b054d01989551d1464e2d8e7b222")
#authorize_url = auth.get_authorize_url()
#print "Go to %s allow the app and copy your oauth_verifier" % authorize_url

#oauth_verifier = raw_input('Please enter your oauth_verifier: ')
creds = auth.get_credentials("IKfIyVSF1KU")

client = WithingsApi(creds)
measures = client.get_measures(limit=1)
print "Your last measured weight: %skg" % measures[0].weight

