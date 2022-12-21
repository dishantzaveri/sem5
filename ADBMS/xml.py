import xml.etree.ElementTree as et
import pandas as pd

author = []
title = []
genre = []
price = []
publish_date = []
description = []
b_id = []

tree = et.parse('data.xml')
root = tree.getroot()

for book in root.iter('book'):
    b_id.append(book.attrib['id'])
    title.append(book.find('title').text)
    genre.append(book.find('genre').text)
    price.append(book.find('price').text)
    publish_date.append(book.find('publish_date').text)
    description.append(book.find('description').text)

data = pd.DataFrame({'id':b_id, 'title': title, 'genre': genre, 'price': price, 'publish_date': publish_date, 'description': description})
print(data)