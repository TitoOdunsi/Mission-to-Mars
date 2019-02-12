#!/usr/bin/env python
# coding: utf-8
#Mission to Mars

#dependencies
from bs4 import BeautifulSoup 
from splinter import browser
import requests

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return browser = Browser('chrome', **executable_path, headless=False)

mars_data = {}

def scrape_mars_news():
    try:
        browser = init_browser()
   

        #NASA Mars News
        url = "https://mars.nasa.gov/news/"
        browser.visit(url)
        #Scraping page into Soup
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        #Collect latest news title and paragraph
        news_title = soup.find("div", class_="content_title").text
        news_paragraph = soup.find("div", class_="article_teaser_body").text
        #Display the scraped data
        print(news_title)
        print(news_paragraph)

        return mars_data

    finally:

        browser.quit()

def scrape_mars_image()

    try:
        browser = init_browser()
        #Visiting JPL Mars URL
        featured_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(featured_image_url)
        #Scraping browser with Beautiful Soup to find image
        html_image = browser.html
        soup = BeautifulSoup(html_image, 'html.parser')
        #Saving image to variable
        featured_image_url = soup.find("img", class_="thumb")["src"]
        image_url = "https://www.jpl.nasa.gov"+ image
        featured_image_url = image_url
        # Display featured image
        featured_image_url

        return mars_data
    finally:

        browser.quit()

def scrape_mars_weather():

    try:
        browser = init_browser():
        #Visiting Mars weather twitter account
        weather_url = "https://twitter.com/marswxreport?lang=en"
        browser.visit(weather_url)
        #Scraping latest mars weather from tweet
        html_weather = browser.html
        soup = BeautifulSoup(html_weather, 'html.parser')
        recent_tweets = soup.find_all('div', class_='js-tweet-text-container')
        for tweet in recent_tweets:
        weather_tweet = tweet.find('p').text
        if 'Sol' and 'pressure' in weather_tweet"
        print(weather_tweet)
        break
    else:
        pass

    return mars_data
finally:

    browser.quit()



def scrape_mars_facts():
#Visting Mars Facts
mars_facts_url = "http://space-facts.com/mars/"
#Scraping table using pandas
import pandas as pd
facts = pd.read_html(mars_facts_url)
mars_df = mars_facts[0]
#Assigning columns and setting index
mars_df.columns = ['Description', 'Value']
mars_df.set_index('Description', inplace=True)
mars_df.to_html()
mars_df

return mars_data


def scrape_mars_hemispheres():
    try:
        browser = init_browser()
#Visiting Mars Hemispheres
hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemispheres_url)
#Scraping html with soup
html_hemispheres = browser.html
soup = BeautifulSoup(html_hemispheres, 'html.parser')
# Retreiving items that contain mars hemispheres information
items = soup.find_all('div', class_='item')
hemisphere_image_urls = [] 
hemispheres_main_url = 'https://astrogeology.usgs.gov'
#looping through items
for i in items: 
    title = i.find('h3').text
    partial_img_url = i.find('a', class_='itemLink product-item')['href']
    browser.visit(hemispheres_main_url + partial_img_url)
    partial_img_html = browser.html
    soup = BeautifulSoup( partial_img_html, 'html.parser')
    img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
    hemisphere_image_urls.append({"title" : title, "img_url" : img_url})    
# Display hemisphere_image_urls
hemisphere_image_urls

    return mars_data
finally:

    browser.quit()






# In[ ]:




