from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import time

def init_browser():
    executable_path = {'executable_path':'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars = {}
# MARS NEWS
# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. 
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    # time.sleep(5)

    news_html = browser.html
    soup = bs(news_html, 'html.parser')

# Assign the text to variables that you can reference later.

    news_title = soup.find('div', class_='content_title').text.strip()
    

    news_p= soup.find('div', class_='article_teaser_body').text


# MARS WEATHER
# Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. 
# Save the tweet text for the weather report as a variable called mars_weather.

    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    weather_html = browser.html
    soup = bs(weather_html, 'html.parser')

    mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text.strip()

# MARS FACTS
# Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet 
# including Diameter, Mass, etc.
# Use Pandas to convert the data to a HTML table string.

    
    facts_url ='https://space-facts.com/mars/'
    facts = pd.read_html(facts_url)

    facts_df = facts[0]
    facts_df.columns = ['Description', 'Values']
    facts_df.set_index('Description', inplace=True)

    facts_html = facts_df.to_html()
    facts =facts_html.replace('\n', '')

# MARS FEATURED IMAGE
# Visit the url for JPL Featured Space Image here.
# Use splinter to navigate the site and find the image url for the current Featured Mars Image 
# and assign the url string to a variable called featured_image_url.
# Make sure to find the image url to the full size .jpg image.
# Make sure to save a complete url string for this image.

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(10)

    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(10)
    browser.click_link_by_partial_text('more info')

    html = browser.html
    soup = bs(html, 'html.parser')

    first_url = 'https://www.jpl.nasa.gov/'
    img_link = soup.find('img', class_='main_image')['src']

    featured_image_url = first_url + img_link
    
# MARS HEMISHPERE IMAGES
# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
# You will need to click each of the links to the hemispheres in order to find the image url 
# to the full resolution image.
# Save both the image url string for the full resolution hemisphere image, 
# and the Hemisphere title containing the hemisphere name. 
# Use a Python dictionary to store the data using the keys img_url and title.
# Append the dictionary with the image url string and the hemisphere title to a list. 
# This list will contain one dictionary for each hemisphere.


    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    time.sleep(5)

    html = browser.html
    soup = bs(html, 'html.parser')
    hemis_html ='https://astrogeology.usgs.gov'

    c_h = soup.find('img', class_='wide-image')['src']
    cerb_h =hemis_html + c_h

    browser.click_link_by_partial_text('Back')
    time.sleep(5)

    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    time.sleep(5)

    html = browser.html
    soup = bs(html, 'html.parser')

    sc_h = soup.find('img', class_='wide-image')['src']
    schi_h =hemis_html + sc_h

    browser.click_link_by_partial_text('Back')

    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    time.sleep(5)

    html = browser.html
    soup = bs(html, 'html.parser')

    sy_h = soup.find('img', class_='wide-image')['src']
    sym_h =hemis_html + sy_h

    browser.click_link_by_partial_text('Back')

    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    time.sleep(5)

    html = browser.html
    soup = bs(html, 'html.parser')

    vm_h = soup.find('img', class_='wide-image')['src']
    vam_h =hemis_html + vm_h

    browser.click_link_by_partial_text('Back')

    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": vam_h},
    {"title": "Cerberus Hemisphere", "img_url": cerb_h},
    {"title": "Schiaparelli Hemisphere", "img_url": schi_h},
    {"title": "Syrtis Major Hemisphere", "img_url": sym_h},
    ]

    mars = {'headline': news_title,
    'article':news_p,
    'facts': facts,
    'weather':mars_weather,
    'featured_img': featured_image_url,
    'hemisphere_img': hemisphere_image_urls
    }
    return mars




