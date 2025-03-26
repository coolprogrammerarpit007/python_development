import requests
# URL = "https://randomuser.me/api/"

# response = requests.get(URL)
# data = response.json()
# print(data)

# consuming the CAT API

# URL = "https://api.thecatapi.com/v1/breeds"
# response = requests.get(URL)

# # sending the custom headers to the request

# headers = {"X-Request-Id": "<my-request-id>"}
# response = requests.get("https://example.org", headers=headers)
# response.request.headers
# {'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate',
# 'Accept': '*/*', 'Connection': 'keep-alive',
# 'X-Request-Id': '<my-request-id>'}


# Calling the charts-api and saving image in the file

# url = "https://image-charts.com/chart?chs=700x125&cht=ls&chd=t:23,15,28"
# response = requests.get(url)

# # print(response.request.headers)  
# # print(response.headers)

# # print(response.headers.get('Content-Type'))

# fhand = open("chart.png","wb")
# fhand.write(response.content)


# response = requests.get("https://randomuser.me/api/?gender=female").json()
# print(response)


# sending query params to the api recall.

# query_params = {"gender":"female","nat":"de"}
# response = requests.get("https://randomuser.me/api/",params=query_params).json()
# print(response)



# Advanced API Concepts
# API Authentication Using Keys

# endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
# api_key = "DEMO_KEY"
# query_params = {"api_key":api_key,"earth_date":"2020-07-01"}

# response = requests.get(endpoint,params=query_params).json()['img_src']
# print(response.headers.get("Content-Type"))
# print(response)



# OAuth Api Authentication

