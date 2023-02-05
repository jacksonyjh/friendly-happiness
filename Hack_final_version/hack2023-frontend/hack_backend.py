import requests
import json


def get_sports(keyword):
    url = "https://sports.api.decathlon.com/sports"

    querystring = {"tag": keyword}

    payload = ""
    response = requests.request("GET", url, data=payload)

    print(json.dumps(response.json(), indent=4))
    # response.headers.add('Access-Control-Allow-Origin', '*')

    return response.json()

# print(get_sports(keyword="basketball"))