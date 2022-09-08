# https://developers.facebook.com/docs/graph-api/reference/post
import requests
import json
import time

PAGE = 'KTXDHQGConfessions' # Page Id or Username
LIMIT = 100 # https://developers.facebook.com/docs/graph-api/overview/rate-limiting
FIELDS = 'message,comments' # https://developers.facebook.com/docs/graph-api/reference/post
SLEEP = 3 # Seconds

''' For Access Token
1. Go to https://business.facebook.com/content_management
2. Press Ctrl + U, then Ctrl + F to find the code that contains EAAG. 
3. Copy the highlighted text, that's the Token you need to get.
'''
ACCESS_TOKEN = ''

''' For Cookie
1. Reload https://graph.facebook.com/me?access_token={YOUR_ACCESS_TOKEN_HERE} with F12
2. Go to the Network Panel and copy value of the cookie param in Request Headers
'''
COOKIE = ''

url = f'https://graph.facebook.com/{PAGE}/posts?limit={LIMIT}&fields={FIELDS}&access_token={ACCESS_TOKEN}'
fields_set = set(FIELDS.replace(' ', '').split(','))
sess = requests.Session()

def get_data_and_next_url(url):
    response = sess.get(url, headers={'cookie': COOKIE})
    response = json.loads(response.text)

    try: data = response['data']
    except: 
        print(response['error']['message'])
        data = []

    try: 
        next_url = response['paging']['next']
        time.sleep(SLEEP)
    except: 
        print('Cannot find next URL')
        next_url = None
    return data, next_url

with open(f'{PAGE}.jsonl', 'w', encoding='utf-8') as file:
    while url is not None:
        print(f'\nGetting {LIMIT} posts from {url}')
        data, url = get_data_and_next_url(url)
        posts = [
            str(post) for post in data 
            if fields_set.issubset(post.keys())
        ]
        file.write('\n'.join(posts))
