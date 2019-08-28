# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 01:12:55 2019

@author: Ahmed
"""

import scraper
import tkinter as tk
from tkinter import ttk
import pandas as pd
df = pd.read_excel("AllCategories.xlsx")
Category= list(df.iloc[:,1])
References= df.iloc[:,2]
reference=References[1]
category = Category[1]

def callScraper(url,catig,pag,prox):
    
    
    pag = scraper.scrape(url,catig,pag,prox )
    
def updateRef(value,cat):
    
    global reference
    global category
    reference = value
    category  = cat
top = tk.Tk()
top.geometry('320x150')

startScrappingButton = tk.Button(top, text = 'Start Scraping',command= lambda:  callScraper(References[comboExample.current()],Category[comboExample.current()],page.get(),{"http":entryHTTP.get(),
                                                                                                          "https":entryHTTPS.get()}))
startScrappingButton.grid(column=0,row=0)

labelTop = tk.Label(top,text = "Choose your Category to scrape")
labelTop.grid(column=0, row=1)
labelStartpage=tk.Label(top,text="Specify Starting Page")
labelStartpage.grid(column=1, row=1)

labelHTTP=tk.Label(top,text="HTTP Proxy")
labelHTTPS=tk.Label(top,text="HTTPS Proxy")
entryHTTP = tk.Entry(top)
entryHTTPS = tk.Entry(top)

labelHTTP.grid(column=0,row=3)
labelHTTPS.grid(column=0,row=4)
entryHTTP.grid(column=1,row=3)
entryHTTPS.grid(column=1,row=4)

page = tk.Entry(top)
page.insert(0,"1")
page.grid(column=1,row=2)

comboExample = ttk.Combobox(top, values=Category,state="readonly")
comboExample.current(1)
comboExample.grid(column=0, row=2)
comboExample.bind("<<ComboboxSelected>>", lambda _ : updateRef(References[comboExample.current()]),Category[comboExample.current()])

top.mainloop()