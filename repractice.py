from pygooglenews import GoogleNews

topic = input("Enter a topic: ")
gn = GoogleNews()

news = gn.search(topic)

count = 0

for entry in news['entries']:
    if count < 5:
        print(f'\nArticle #{str(count+1)}: ')
        print(entry["title"])
        print(entry["published"])
        count +=1
    else:
        break