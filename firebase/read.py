from firebase import firebase
import time
firebase = firebase.FirebaseApplication('https://test-f97f0.firebaseio.com', None)
result = firebase.get('/users',None)
while True:
    result = firebase.get('/users',None)
    print(result)
    time.sleep(2)