# Objective:
The Application Scrapes current news and photos from five different Nasa and Mars related websites,
consolidates them in a database, then presents them on a single html page.

# Process:

## Step 1 Scraping Data:
My first step was testing my code in Jupyter Notebokk to successfully scrape the data that I eventually wanted to present. In my notebook I imported 
dependencies needed for the code. After connecting to a chromedriver that matches the version of chrome I use, I scraped the most recent nasa news article
title and a small article description from https://mars.nasa.gov/news/ with Beautiful Soup. <br>
I once again used the Nasa website to grab one of the newest photographs from mars, the url I used was here: https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
