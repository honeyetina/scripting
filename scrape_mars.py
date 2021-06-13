#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 18:57:54 2021

@author: charles
"""
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    items = soup.find_all('div', id='news')[0]
    item0 = items.find_all('div', class_='col-md-12')[0]
    news_title = item0.find_all('div', class_='content_title')[0].text
    
    news_p = item0.find_all('div', class_='article_teaser_body')[0].text
    
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image_url = url + \
        soup.find_all('img', class_='headerimage')[0].attrs['src']
    
    
    import pandas as pd
    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)
    tables
    df0 = tables[0]
    df0 = df0.set_index(0)
    df0.index.name = 'Description'
    df0.columns = ['Mars', 'Earth']
    mars_fact_table = df0.to_html()
    
    
    import time
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    items = soup.find_all('div', class_='item')
    
    hemisphere_image_urls = []
    for i in range(len(items)):
        # i = 0
        item = items[i]
        title = item.find_all('h3')[0].text
        browser.find_by_css('img.thumb')[i].click()
        html2 = browser.html
        soup2 = BeautifulSoup(html2, 'html.parser')
        img_url = url + soup2.find_all('div', class_='downloads')[0]\
            .find_all('li')[0]\
            .find_all('a')[0]\
            .attrs['href']
        hemisphere_image_urls.append({'title': title,
                                      'img_url': img_url})
        time.sleep(1)
        browser.visit(url)
        time.sleep(1)
        
    res = {'redplanetscience': {'news_title': news_title,
                                'news_p': news_p},
           'spaceimages-mars': featured_image_url,
           'galaxyfacts-mars': mars_fact_table,
           'marshemispheres': hemisphere_image_urls
        }
    browser.quit()
    return res
        














