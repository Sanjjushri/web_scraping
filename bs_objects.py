from bs4 import BeautifulSoup

html_doc = """

<!DOCTYPE html>
<html>

<head>
    <title>The Demo</title>
</head>

<body>

<p class="title"><b>The Demo</b></p>

<p class="story">Once upon a time there were three little sisters; their names:
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

<p class="story">...</p>
<b class="boldest">Extremely bold</b>
<blockquote class="boldest">Extremely bold</blockquote>
<b id="1">Test 1</b>
<b another-attribute="1" id="verybold">Test 2</b>

</body>
</html>

"""

with open('index.html', 'w') as f:
    f.write(html_doc)

soup = BeautifulSoup(html_doc, "lxml")

#prettify -- output is in formatted way
print(soup.prettify())

#bold tag
print(soup.b)

#para tag
print(soup.p)


# find -- finds the first occurence of the usage for a "b"
print(soup.find('b'))

#find all of the elements
print(soup.find_all('b'))

#gives the name of the tag
print(soup.b.name)

#alter the name and that reflected in the source
tag = soup.b
print(tag)

tag.name = "blockquote"
print(tag)

# find all the elements & return the element in the index provided
tag = soup.find_all('b')[2]
print(tag)

# id attribute 
print(tag['id'])

tag3 = soup.find_all('b')[2]
print(tag3)

# multiple attributes access
print(tag3['id'])
print(tag3['another-attribute'])

# all attributes as dictionary
tag = soup.find_all('b')[2]
print(tag)
print(tag.attrs)

#attributes are mutable and can alter them
tag['another-attribute'] = 2
print(tag)


