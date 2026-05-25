# dictionaries (review)
# dictionaries store either heterogenious or homogenius data well! 

# create a dictionary 
person = {}

# assign key and value to a dictionary 
person['name'] = 'christian'
person['age'] = 27
person['employer'] = 'Utah State University'

# access information from the dictionary 
print(person['name'])

# we can easily iterate through the keys in a dictionary 
for key in person.keys():
    print(person[key])


# JSON 
# the syntax between a JSON and a python dictionary is identicle - because of this we can take any dictionary we want and turn it into a JSON. The opposite is also true, we can take any JSON we want and turn it into a dictionary.
# take a python dictionary and save it down to JSON format

# It's great to take a JSON, load it into a dictionary, then print it into the console to explore the data held within the JSON file.

import json
import requests

hobbies = {}
hobbies['sports'] = ['fly fishing', 'ultra running', 'climbing']
hobbies['casual'] = ['dog walks']

print(hobbies)

# save this to JSON format (it takes two arguments, the first is the dictionary and the second is the file we werite to)
json.dump(hobbies, open('hobbies.json', 'w'))

# loading a json into a dictionary is easy 
d1 = json.load(open('hobbies.json', 'r'))
print(d1)

# web JSON API's
# very powerful, easy way to get a massive amount of data from the web
# JSON is the standard 
# JSON - Javascript Object Notation

# 4 steps to getting JSON data 
# 1 - get the url and put it in the browser 
# 2 - stare at it and analyze the data we need 
# 3 - find the keys we need 
# 4 - request the json, convert to a dictionary, process the data 

# example url to query a web api 
example_url = 'https://api.datamuse.com/words?ml=fish'

# variables we'll use to query 
word = 'fish'
key_word = 'word'
score = 'score'
search_word = 'trout'

# generate url 
url = 'https://api.datamuse.com/words?ml=' + word
print(url)

# request data with request library
request = requests.get(url)

# json.loads loads the string version of a json, so we have to feed it a string to begin with
dct_full = json.loads(request.text)

print(dct_full)

# iterate through the dictionary's 
for dct_small in dct_full:
    print(dct_small)
    if dct_small[key_word] == search_word:
        print(search_word, 'score:', dct_small[score])


import requests

DATASET_ID = "pwn4-m3yp"
BASE_URL = f"https://data.cdc.gov/resource/{DATASET_ID}.json"

params = {
    "$where": "state='UT' AND end_date >= '2020-01-01' AND end_date <= '2023-12-31'",
    "$order": "end_date ASC"
}
req = requests.get(BASE_URL, params=params)
print(req.text)
