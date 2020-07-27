import requests
from bs4 import BeautifulSoup

'''Beautiful Soup is a Python library for pulling
   data out of HTML and XML file and convert into an object(called as soup)
   that we can manipulate and use.(web scraping)'''

res = requests.get('https://news.ycombinator.com/')
# print(res.text)  # complete html text of the website

'''parsing: analyse a string into logical syntactic components
            in the language it is written.'''

soup = BeautifulSoup(res.text, 'html.parser')

'''Most of the code here like 'div', 'a'  are related to
   HTML so do not think about it too much.'''

# print(soup)
# print(soup.body)  # only body 
print(soup.find_all('div'))  # div in HTML is division
# print(soup.find_all('a')) # a in HTML is hyperlink
print(soup.title)  # give title of website
print(soup.a)  # first link
print(soup.find('a'))  # first link same as above line
print(soup.find( id="score_22854120"))  
