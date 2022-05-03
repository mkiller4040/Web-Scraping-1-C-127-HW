from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
 
start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
 
browser = webdriver.Chrome("/Monit/Learn and Study/Monit/Projects/C-127/chromedriver.exe")
 
browser.get(start_url)
 
time.sleep(10)
 
def scrape() :
 
    header = ["name",
    "distance",
    "mass", "radius"]
 
    planetData = []
 
    for i in range(0,428) :
        soup = BeautifulSoup(browser.page_source, "html.parser")
 
        for ultag in soup.find_all("ul", attrs = {"class", "exoplanet"}) :
            li_tags = ultag.find_all("li")
            templist = []
            for index, litag in enumerate(li_tags) :
                if index == 0 :
                    templist.append(litag.find_all("a")[0].contents[0])
                else :
                    try :
                        templist.append(litag.contents[0])
                    except :
                        templist.append("")
            planetData.append(templist)
        browser.find_element_by_xpath("")
    with open("data.csv", "w") as f :
        csvWriter = csv.writer(f)
        csvWriter.writerow(header)
        csvWriter.writerows(planetData)
 
scrape()