# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 01:56:15 2024

@author: yanna
"""

import requests

def get_random_chuck_norris_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['value']
    else:
        return 'Failed to fetch Chuck Norris joke'

if __name__ == "__main__":
    joke = get_random_chuck_norris_joke()
    print("Chuck Norris Joke:")
    print(joke)
