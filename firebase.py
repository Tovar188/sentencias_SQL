import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

firebase_sdk = credentials.Certificate('sentenciassql-firebase-adminsdk-enakm-0db5ce415d.json')

firebase_admin.initialize_app(firebase_sdk,{'databaseURL' : 'https://sentenciassql-default-rtdb.firebaseio.com'})

