# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:10:32 2019

@author: Ahmed
"""

import requests
import json
from bs4 import BeautifulSoup
import time
import urllib.request
import os
def saveContent(contentUrl,category,extension,proxy):
    if not os.path.isdir(category):
        os.makedirs(category)
    urllib.request.urlretrieve(url=contentUrl, filename=category+"/"+category+extension+'.mp4') 


def scrape(URL,category,startingPage,proxies):
    pages=int(startingPage)
    if(proxies["http"]==""):
        proxies["http"]=None
    if(proxies["https"]==""):
        proxies["https"]=None
    
    while True:
        
        page = requests.get(URL+"?page="+str(pages),proxies=proxies)
        
        soup = BeautifulSoup(page.content, 'html.parser')
        
        products=soup.find_all(class_="item-main")
        if(len(products)==0 and pages>100):
            break
        failed=[]
        print(len(products))
        number=1
        for product in products:
            
            exists=str(product.find(class_="watermark has-video"))
            if(exists!="None"):
                
                link="https:"+product.find(class_="item-info").find(class_="title").find("a")['href']
                productPage=requests.get(link,proxies=proxies)
                soup = BeautifulSoup(productPage.content, 'html.parser')
                contentHolder=json.loads(soup.find('script', type='application/ld+json').text)
                for content in contentHolder:
                    if content["@type"]=="VideoObject":
                        tries=0
                        while True:
                            try:
                                saveContent("http:"+content["contentUrl"],category.replace("'","").replace(" ",""),"p"+str(pages)+"n"+str(number),proxies)
                                number+=1
                                break
                            except Exception as e:
                                if(tries==30):
                                    failed.append(content["contentUrl"])
                                    print("saving failed, moving on to the next video")
                                print("encountered problems while saving, retrying in 2 seconds"+str(e))
                                time.sleep(2)
                                tries+=1
        pages+=1                     
                                
                                
