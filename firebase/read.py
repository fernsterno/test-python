import pyrebase
import time

config = {
    "apiKey": "*****************",
    "authDomain": "*****************",
    "databaseURL": "*****************",
    "storageBucket":"*****************"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

auth_user = auth.sign_in_with_email_and_password('*****************', '*****************')

db = firebase.database()

while True:
    users = db.child("users").get(auth_user['idToken'])
    print(users.val())
    time.sleep(2)