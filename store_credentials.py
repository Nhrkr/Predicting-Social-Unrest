import json

# Enter your keys/secrets as strings in the following fields
credentials = {}
credentials['CONSUMER_KEY'] = 'Key'
credentials['CONSUMER_SECRET'] = 'Secret'
credentials['ACCESS_TOKEN'] = 'token'
credentials['ACCESS_SECRET'] = 'secret'
 
# Save the credentials object to file
with open("twitter_credentials.json", "w") as file:  
    json.dump(credentials, file)
