# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

#sample json
userJSON = '{"first_name": "Ronny", "last_name": "Nijimbere", "age": 33}'

#parse to dict
user = json.loads(userJSON)


#print(user)
#print(user['first_name'])

car = {'make': 'bmw', 'model': 'piece of shit', 'year': 1912}

carJSON = json.dumps(car)
print(carJSON)