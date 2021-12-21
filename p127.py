from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL='https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome("C:/Users/rishi/Python/Classes/c127/chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers=['Name','Distance','Mass','Radius']
    brighteststar_data=[]
    for i in range(0,428):
        soup=BeautifulSoup(browser.page_source,'html.passer')
        for ul_tag in soup.find_all('ul',attrs={'class', 'brighteststar'}):
            li_tags=ul_tag.find_all('li')
            temp_list=[]
            for index, li_tag in enumerate(li_tags):
                if index==0:
                    temp_list.append(li_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append('')
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open('scapper_2.csv','w')as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerow(brighteststar_data)
scrape()