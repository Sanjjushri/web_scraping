import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.google.com/")


#the code that we get back from the google. com home page is 200

print(result.status_code) 

print(result.headers)


#the web source of the google.com home page

src = result.content
print(src)


#beautiful soup module to parse and process the source
# lxml -- if we dont hav it it will give us warning 

soup = BeautifulSoup(src, 'lxml')


#links -- find a tags

links = soup.find_all("a")
print(links)
print("\n")


#extract the links that contains the text

for link in links:
    if "About" in link.text:
        print(link)
        print(link.attrs['href'])


