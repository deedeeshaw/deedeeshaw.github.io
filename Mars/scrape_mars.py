from bs4 import BeautifulSoup as bs
from splinter import Browser

import time

def init_browser():
    executable_path = {'executable_path':'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars = {}

# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. 
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    time.sleep(10)

    news_html = browser.html
    soup = bs(news_html, 'html.parser')

# Assign the text to variables that you can reference later.

    news_title = soup.find('div', class_='content_title').text.strip()
    

    news_p= soup.find('div', class_='article_teaser_body').text


# Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. 
# Save the tweet text for the weather report as a variable called mars_weather.

    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    weather_html = browser.html
    soup = bs(weather_html, 'html.parser')

    mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text.strip()

# Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet 
# including Diameter, Mass, etc.
# Use Pandas to convert the data to a HTML table string.

    import pandas as pd
    facts_url ='https://space-facts.com/mars/'
    facts = pd.read_html(facts_url)

    facts_df = facts[0]
    facts_df.columns = ['Description', 'Values']
    facts_df.set_index('Description', inplace=True)

    facts_html = facts_df.to_html()
    facts =facts_html.replace('\n', '')


    mars = {'headline': news_title,
     'article':news_p,
    'facts': facts,
    'weather':mars_weather
    }

    return mars




