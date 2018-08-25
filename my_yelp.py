# Maintainer: Kumail Razvi
# Create Date: 25-Aug-2018

import requests


def search_business():
    api_key = "e6mtc6SVQPPS68uiYK6KNaYm4Mit_SChSxouObNX7QHmh-eZi3Y2NGE_1D3kPOC7PZwKslLfTeMpQpsF0dNftkSxDJLiaZOToOlMheJS7p5ljt161KBEdO0tC2t_W3Yx"
    url = "https://api.yelp.com/v3/businesses/search"
    my_headers = {
        "Authorization": "Bearer %s" % api_key
    }

    my_params = {
        "term": "restaurants",
        "location": "chicago",
        "limit": 3,
    }

    businesses_object = requests.get(url, headers=my_headers, params=my_params)
    businesses_dict = businesses_object.text
    print(businesses_dict)

# Calling search_business function
search_business()
