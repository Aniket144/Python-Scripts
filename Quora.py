import requests
from bs4 import BeautifulSoup
import webbrowser
import time

Q_url = 'https://www.facebook.com/pg/quoraIN/posts/?ref=page_internal'
hrefs = BeautifulSoup(requests.get(Q_url).text, "html.parser").find_all("a")
links = set([])

def Href2Url(href_link):
    href_link = href_link.replace('%2F','/')
    href_link = href_link.replace('%25E2%2580%2599','\'')
    return href_link

for link in hrefs:
    hrefs = link.get('href')
    if 'www.quora.com' in hrefs:
        quora_link = hrefs[45:hrefs.index('&h')]
        #quora_link = quora_link.replace('%2F','/')
        quora_link = Href2Url(quora_link)
        links.add(quora_link)
for url in links:
    print(url)
    webbrowser.open_new(url)
    time.sleep(1)

