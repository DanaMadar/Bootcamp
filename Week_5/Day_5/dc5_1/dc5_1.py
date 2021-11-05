# Using the requests and time modules, create a function which returns the amount of time it takes a webpage to load (how long it takes for a complete response to a request).
# Test your code with multiple sites such as google, ynet, imdb, etc.

import requests
import time

response1 = requests.get('https://realpython.com/python-requests/')
response2 = requests.get(
    'http://learn.di-learning.com/courses/collection/18/course/13/section/62/chapter/312')
response3 = requests.get('https://www.youtube.com/')
print(response1.elapsed.total_seconds())
print(response2.elapsed.total_seconds())
print(response3.elapsed.total_seconds())
