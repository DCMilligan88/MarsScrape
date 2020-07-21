#dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import time
import pandas as pd


def scrape():
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    #Nasa news and teaser paragraph
    nasaUrl = 'https://mars.nasa.gov/news/'
    browser.visit(nasaUrl)
    html = browser.html
    soup = bs(html, 'html.parser')
    time.sleep(5)
    #variables for news title and paragraph
    articleTitle1 = articleTitle = soup.find('li',class_='slide')
    time.sleep(5)
    articleTitle = articleTitle1.find('div',class_='content_title').text
    articleTeaser = soup.find('div', class_='article_teaser_body').text

    #Image url connections

    imageUrl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(imageUrl)
    time.sleep(10)
    html = browser.html
    soup = bs(html, 'html.parser')

    #creating full url by scraping endpoint and concantinating with base
    newImageUrl = imageUrl.replace('/spaceimages/?search=&category=Mars', '')
    imageEndPoint= soup.article['style'][23:-3]
    fullImageUrl = newImageUrl + imageEndPoint

    #mars twitter: weather connections
    marsTwitter = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(marsTwitter)
    time.sleep(10)
    html = browser.html
    soup = bs(html, 'html.parser')

    #variable for marsWeather scrape
    marsWeather = soup.find_all('div', class_="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0")
    for weather in marsWeather:
        if 'sol' and 'pressure' in weather.text:
            marsInsight=weather.text
            break
    

    #connection for mars table
    marsTable= 'https://space-facts.com/mars/'
    browser.visit(marsTable)
    time.sleep(10)
    html = browser.html
    soup = bs(html, 'html.parser')

    #variable for mars table
    tableData = pd.read_html(marsTable)
    tableData = tableData[0]
    tableData.columns = ['Description', 'Value']
    tableData = tableData.set_index('Description')
    tableData = tableData.to_html()
  


    #Hemisphere url connections
    HemURL = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(HemURL)
    time.sleep(10)
    html = browser.html
    soup = bs(html, 'html.parser')

    # Create list empty for dictionaries of titles and links
    hemisphere_info = []
    hemispheres = soup.find("div", class_ = "result-list" ).find_all("div", class_="item")

    # Iterate through sections
    for hemisphere in hemispheres:
        title = hemisphere.h3.text
        endpoint = hemisphere.a["href"]
        image_link = "https://astrogeology.usgs.gov/" + endpoint   
        browser.visit(image_link)
        html = browser.html
        soup = bs(html, "html.parser")
        image_url = soup.find("div", class_="downloads").a["href"]
        hemisphere_info.append({"title": title, "img_url": image_url})

    #dictionary for mars info
    mars_info = {"articleTitle": articleTitle,
                "articleTeaser": articleTeaser,
                "fullImageUrl": fullImageUrl,
                "marsWeather": marsInsight,
                "marsTable": tableData,
                "hemisphere_info": hemisphere_info}

    browser.quit()

    return mars_info

if __name__ == '__main__':
    scrape()

