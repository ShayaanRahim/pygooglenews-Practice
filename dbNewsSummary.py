from pygooglenews import GoogleNews

topic = input('Enter a topic: ')
gn = GoogleNews()

date = gn.search(query= topic, helper=True, when = "2d", from_ = None, to_ = None, proxies=None, scraping_bee = None)

for entry in date["entries"]:
    print(entry["title"])
    print(entry["published"])