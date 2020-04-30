# https://www.practicepython.org/
# PRACTICE PYTHON
# Beginner Python exercises

# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

# https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/

import requests
from bs4 import BeautifulSoup
import datetime

def html_decode(url,tg,cl):
    page = requests.get(url)
    page_html = page.text
    
    soup = BeautifulSoup(page_html,'lxml')

    print(soup.title.string,"\n")
    print("Date:",datetime_object,"\n")
    print("The article titles:\n")
    
    num = 0
    for h1 in soup.find_all(tg, class_=cl):
        num = num + 1
        ntxt = str(num) + "."
        print(ntxt,h1.text)

# clear shell
def cls():
    print(50 * "\n")

# main program

datetime_object = datetime.date.today()

cls()

url = 'https://www.nytimes.com/'
#url = 'https://www.motostforky.pl/'
#url = 'http://www.griba.pl/_temp_/example.html'

page = requests.get(url)
page_html = page.text

#print(page.status_code) # 200 = ok, web loaded
#print(page.content) # text string
#print(page_html) # html with structure

# print some part of string
#for i in range(0,1000):
#    print(r_html[i],end='')

soup = BeautifulSoup(page_html,'lxml')

# printing only text from html file
#print(soup.get_text())

# title of the page
#print(soup.title)

# get attributes
#print(soup.title.name)

# get value of the title
print(soup.title.string,"\n")

# beginning navigation
#print(soup.title.parent.name)

# getting specific values
#print(soup.a.string)

# getting names and href of links
#for link in soup.find_all('a'):
    #print(link.string,end='')  # NavigableString object
    #print(link.text,end='')    # typical unicode text
    #print(link.get('href'))

print("Date:",datetime_object,"\n")
print("The article titles:\n")

num = 0
for h2 in soup.find_all('h2', class_='esl82me0'):
    num = num + 1
    ntxt = str(num)+"."
    print(ntxt,h2.text)

print()
print(50 * "*","\n")

html_decode("https://www.motostforky.pl/","h1","entry-title")
