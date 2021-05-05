#!/usr/local/bin/python3
#---------------------------------------
#   Sample Web Scrape using toscrape.com
#---------------------------------------
import requests
import bs4

author_list = []
i = 1

while True:

    URL  = 'http://quotes.toscrape.com/page/' + str(i) + '/'
    page = requests.get(URL)
    soup = bs4.BeautifulSoup(page.text, 'lxml')

    authors = soup.select('.author')
    if len(authors) == 0:
        break

    for author in authors:
        if author.text not in author_list:
            author_list.append(author.text)
    i += 1

print(author_list)