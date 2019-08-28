import requests
from bs4 import BeautifulSoup
import pandas as pd
def updateCategoryList():
    df = pd.DataFrame(columns=['Category','Reference'])
    
    page = requests.get("https://www.alibaba.com/sitemap/product_categories.html")

    soup = BeautifulSoup(page.content, 'html.parser')

    categories=list(soup.find_all(class_="narrow"))
    #print(list(categories))
    for category in categories:
        listItem=(list(category.find_all("li")))
        for item in listItem:
            ref="https://www.alibaba.com/catalog"+item.find("a")['href']
            ref=ref.replace("pid","cid")
            title=item.find("a").text
            print(str(ref)+": "+title)
            df=df.append({"Category":title,"Reference":ref}, ignore_index=True)
        #print(str(listItem))
    df.to_excel("AllCategories.xlsx")
    return df
updateCategoryList()