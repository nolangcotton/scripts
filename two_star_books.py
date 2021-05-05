#!/usr/local/bin/python3
#---------------------------------------
#   Sample Web Scrape using toscrape.com
#---------------------------------------
import requests
import bs4

#---------------------------------------
#   Generic URL
#---------------------------------------
URL    = 'https://books.toscrape.com/catalogue/page-{}.html'
titles = []

#---------------------------------------
#   Goal: to get the title of each book 
#         with a 2* rating
#---------------------------------------
for i in range(1,51):

    #---------------------------------------
    # Get Page 
    #---------------------------------------
    page = requests.get(URL.format(i))
    soup = bs4.BeautifulSoup(page.text, 'lxml')
    books = soup.select('.product_pod')

    #---------------------------------------
    # Loop through all books
    # if rating = 2 add to title list
    #---------------------------------------
    for book in books:
        if len(book.select('.star-rating.Two')) != 0 and books[0].select('a')[1]['title'] not in titles:
            titles.append(books[0].select('a')[1]['title'])

for k in titles:
    print(k)