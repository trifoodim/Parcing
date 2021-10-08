from urllib.request import urlopen
html = urlopen('https://ru.wikipedia.org/wiki/Python').read().decode('utf-8')
# pos = html.find('<a href=')
# while pos != -1:
#     posquote = html.find('"', pos + 9) # срез ссылки
#     href = html[pos + 9:posquote]
#     print(href)
#     pos = html.find('<a href=', pos + 1)

# использование BeatifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
for a in soup.find_all('a', href=True):
    print(a['href'])