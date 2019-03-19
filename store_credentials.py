import json

# Enter your keys/secrets as strings in the following fields
credentials = {}
credentials['CONSUMER_KEY'] = 'iJBfq6XchKhZhDg0o18skYNyp'
credentials['CONSUMER_SECRET'] = '7TEHyXMU6XDgHUaR2XT29VowsrIyBpB5rOtFx2Gi18FYJjBtJh'
credentials['ACCESS_TOKEN'] = '2725236026-an7z9tJ9HhJwIRljfETkRNup7LJG3d2iULt9Ija'
credentials['ACCESS_SECRET'] = '3o4tELrjgwiM7jyx2QzP8PRxoYnIz6O3BRusDG5Qq2CW4'
 
# Save the credentials object to file
with open("twitter_credentials.json", "w") as file:  
    json.dump(credentials, file)