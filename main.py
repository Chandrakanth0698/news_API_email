import requests
# get api key and API url to get access to data
API_KEY = "b997584a6f7c46e7b049f0774987178a"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-10-03&" \
      "sortBy=publishedAt&apiKey=b997584a6f7c46e7b049f0774987178a"
# get the request object using get function
request = requests.get(url)
# get data in the dict using .json() function
content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])

