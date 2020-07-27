'''Most if the code here are very specific to the website, and hence for scraping any
   website, we need to check it's terms and conditon(/robots.txt) and then the data from the
   website[Ctrl+Shift+I(inspect), Ctrl+U(source code)].'''

import requests
from bs4 import BeautifulSoup
import pprint  # used to make the output neater and visible

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')

 # here we are taking .subtext instead of .score because there is a chance of getting 0 points in some news, then we might get an error.
links = soup.select('.storylink')  
subtext = soup.select('.subtext') 

def sort_stories_by_votes(hacker_news):
    # created after create_custom_hnews function to sort the news.
    return sorted(hacker_news, key= lambda x: x['votes'], reverse=True)

def create_custom_hnews(link, subtext):
    # the actual code for the project
    hnews = []
    for idx, item in enumerate(link):
        title = item.getText()  # for all title, instead of link[idx] we can write item since both are same.
        href = item.get('href', None)  # for all link, None is default if link is broken
        vote = subtext[idx].select('.score')  # inside subtext we are selecting score
        if len(vote):  # this is because some link will have 0 points, vote is a string
            points = int(vote[0].getText().replace(' points', ''))  # chahing vote to a number(Ex: 22 points to 22)
            if points > 99: 
                hnews.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hnews)

pprint.pprint(create_custom_hnews(links, subtext))