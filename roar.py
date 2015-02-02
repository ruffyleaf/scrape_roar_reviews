#Author: Max
#Date: 28/jan/2015
#Scrape reviews about the ROAR and save it into mongodb
#########

import sys, pymongo
from scrape import scrapeURL

#hook up mongo
conn = pymongo.Connection("mongodb://localhost", safe=True)
db = conn.roar
reviews = db.reviews

def insertReviews(reviews):
    
    # from page 1 to 110
    for i in range(1,111):
        #setup the url
        url = 'http://www.amazon.com/Creative-Sound-Blaster-Roar-Built/product-reviews/B00N415E7Q/ref=cm_cr_pr_btm_link_next_'+str(i)+'?ie=UTF8&pageNumber='+str(i)+'&showViewpoints=0&sortBy=bySubmissionDateDescending'
       
        print "grabbing from " + url
        #grab the page
        page_reviews = scrapeURL(url, 'div', 'reviewText')
        
        print "inserting into mongo"

        #insert into mongo
        for review in page_reviews:
            r = {'url':url , 'review' : str(review) }
            
            try:
                reviews.insert(r)
            except:
                print "Unexpected error:", sys.exec_info()[0]

insertReviews(reviews)
