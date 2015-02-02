import requests
from bs4 import BeautifulSoup

def scrapeURL(url, element, class_):
    """Takes in a URL, HTML element, and HTML class for scraping.
    Returns a beautiful soup element result set.
    """
    #get the page
    r = requests.get(url)
    
    #take out the meat
    doc = r.text

    #prepare the soup
    soup = BeautifulSoup(doc)

    #retrieve the essential
    try:
        reviews = soup.find_all(element, class_ = class_)
        return reviews
    except:
        print "Had problems retrieving reviews"
