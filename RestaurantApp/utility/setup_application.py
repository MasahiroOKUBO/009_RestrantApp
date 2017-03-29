import json

APPLICATION_NAME = "RestaurantApp"

GOOGLE_CLIENT_SECRET = json.loads(open('client_secret_google.json', 'r').read())
GOOGLE_CLIENT_ID = GOOGLE_CLIENT_SECRET['web']['client_id']

FACEBOOK_CLIENT_SECRET = json.loads(open('client_secret_facebook.json', 'r').read())
FACEBOOK_APP_ID = FACEBOOK_CLIENT_SECRET['web']['app_id']

