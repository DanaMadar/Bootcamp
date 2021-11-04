# import json
# from faker import Faker

# fake = Faker()

# with open('file.json', 'r') as f:
#     family = json.load(f)

# print('janes children:')

# for child in family['children']:
#     child['favorite_color'] = fake.color()
#     for key, value in child.items():
#         print(f'my {key} is {value}')


# with open('file.json', 'w') as f:
#     json.dump(family, f, indent=2)


import json
# my_family = {
#     "parents":['Beth', 'Jerry',],
#     "children":['Summer', 'Morty',],
#     'are_awesome': True,
#     'have_dog': False,
#     'phone_number': None,
#     'friends': {'have_some':True, 'count':45}
# }
# my_str = json.dumps(my_family)
# print(my_str)
# with open('sanchez.json', 'w') as file:
#     json.dump(my_family, file, indent=2)

# with open('secrets', 'r') as f:
#     my_data = json.load(f)

# my_data['hobbies'] += ['surfing', 'skiing', 'gaming']
# # del my_data['age']
# with open('secrets', 'w') as f:
#     # json.dump(my_data, f, indent=1) # same as the two lines below
#     my_json_string = json.dumps(my_data, indent=1)
#     f.write(my_json_string)
#     # f.write()

import requests
import random
# response = requests.get('http://api.open-notify.org/iss-now.json')

# iss_data = response.json()
# print(response.text)
# print(response.status_code)
# print(iss_data['iss_position'])

# parameters = {"lat": 31.771959, "lon": 35.217018}
# response = requests.get(
#     "http://api.open-notify.org/iss-pass.json", params=parameters)
# response = requests.get(
#     "http://api.open-notify.org/iss-pass.json?lat=31.771959&lon=35.217018")
# print(response.json()['response'])

category_response = requests.get('https://api.chucknorris.io/jokes/categories')
if category_response.status_code == 200:
    categories = category_response.json()

category = categories[0]
params = {'category': category}
joke_response = requests.get(
    f'https://api.chucknorris.io/jokes/random', params=params)
if joke_response.status_code == 200:
    print(joke_response.json()['value'])
