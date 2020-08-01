# Objective:
The Application Scrapes current news and photos from five different Nasa and Mars related websites,
consolidates them in a database, then presents them on a single html page.

# Process:

## Step 1 Scraping Data:
My first step was testing my code in Jupyter Notebokk to successfully scrape the data that I eventually wanted to present. In my notebook I imported 
dependencies needed for the code. After connecting to a chromedriver that matches the version of chrome I use, I scraped the most recent nasa news article
title and a small article description from <a href="https://mars.nasa.gov/news/">Nasa News</a> with Beautiful Soup.
I once again used the Nasa website to grab one of the newest photographs from mars, the url I used was here: <a href="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars">Mars Photo</a>
How is the weather on mars may be something you are interested in? Do I pack shorts or my lava resistant parka? Is there a light rain? or a cataclysmic death rain? To answer these questions and more I needed current data from the <a href="https://twitter.com/marswxreport?lang=en">Mars Twitter</a>. This provided an interesting challenge, whenever I tried to zero in on the section I needed I would always get some variable data returned. Noticing that all of the sections that I needed always contained the words "sol" and "pressure" I used a simple if statement to hone in on the most current section. Maybe you want some facts about mars to impress your friends at parties. Well I have scraped a simple facts table from this website <a href="https://space-facts.com/mars/" target="_top">Mars Facts</a> to provide you that oppurtunity.
