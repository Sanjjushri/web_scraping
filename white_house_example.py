import requests 
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefing-room/")
src = result.content

soup = BeautifulSoup(src, 'lxml')

#after inspecting that page -- links are stored in h2 tag

urls = []
for h2_tag in soup.find_all("h2"):
	a_tag = h2_tag.find("a")
	if a_tag == None:
		urls.append("Empty")
		continue
	urls.append(a_tag.attrs['href'])


print(urls)


# METHOD -- 2 
# urls =[ ]
# for x in soup.findAll('h2',{'class':'news-item__title-container'}):
#     links = x.find_all('a')
#     urls.append(links)   
# print(urls)


# METHOD -- 3
# if a_tag is not None:
#         urls.append(a_tag.attrs['href'])