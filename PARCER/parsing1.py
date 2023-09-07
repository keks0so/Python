from bs4 import BeautifulSoup as bsoup
import requests

headers = {
    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

req = requests.get('https://www.103.by/spec/1123-ahnovec/?placeId=10156292')
src = req.text

#with open("indexxx.html", "w") as file:
#    file.write(src)

soup = bsoup(src, "lxml")

user_name = soup.find_all('div', class_="Review__AuthorName")
print(user_name)