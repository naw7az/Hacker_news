import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')

'''the select function is a CSS selector, In CSS, selectors are used
   to target the HTML elements on our web pages that we want to style.'''

# print(soup.select('a'))  # all links like before
links = soup.select('.storylink')  # return all links, . stands for class(storylink here)
votes = soup.select('.score')  # return all votes in a link 
print(votes[0])  # the first vote
print(votes[0].get('id'))

          