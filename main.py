import requests
from send_email import send_email
# get api key and API url to get access to data
# you can change the category or country with f- strings
API_KEY = "b997584a6f7c46e7b049f0774987178a"
url = "https://newsapi.org/v2/top-headlines?" \
      "country=us" \
      "&category=business" \
      "&apiKey=b997584a6f7c46e7b049f0774987178a"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject: Today's Business News from Chandu's python API script " + "\n"
for article in content["articles"][:20]:
    if article["title"] and article["description"] :
        body = body + "Title:" + article["title"] + "\n" + "Description: " + article["description"] + "\n" \
               + article["url"] + "\n" + "Content:" + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)

