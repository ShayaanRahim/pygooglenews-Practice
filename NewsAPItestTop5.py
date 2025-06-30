
from pygooglenews import GoogleNews

topic = input("Enter first topic: ")
language = input("Enter the language: ")
country1 = input("Enter the country(2-letter abbreviation:)")

gn = GoogleNews(lang=f'{language}', country=f'{country1}')
s = gn.search(f'{topic}')

count = 0

for entry in s["entries"]:
    if count < 5:
        print(f'\nArticle #{str(count+1)}: ')
        print(entry["title"])
        print(entry["published"])
        count+=1
    else:
        break
