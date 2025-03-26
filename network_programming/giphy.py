# Searching and Fetching Trending GIF

import requests

API_KEY = "cneTnz8c2HxQvV3NVaLjwfjBUCIsov2T"
endpoint = "https://api.giphy.com/v1/gifs/trending"

params = {
    "api_key":API_KEY,
    "limit":3,
    "rating":"g"
}

try:
    response = requests.get(endpoint,params=params)
    data = response.json()

    for gif in data["data"]:
        title = gif['title']
        trending_date = gif["trending_datetime"]
        url = gif['url']
        print(f"{title} | {trending_date}\n{url}\n")


except:
    print("Error occurred while fetching trending GIFs")