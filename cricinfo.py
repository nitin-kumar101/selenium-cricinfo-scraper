import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd

PATH = "/home/imnitin/code_snippets/tweets_scrapping/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://www.espncricinfo.com/team/india-6")

path = "" #Path of the directory where you want to store your cricinfo.csv file
Headings = []
Texts = []

articles = driver.find_elements(By.XPATH,"//*[contains(@class, 'ds-w-full ds-bg-fill-content-prime ds-overflow-hidden ds-rounded-xl ds-border ds-border-line ds-mb-4')]")

        
i=0
speed = 600
current_scroll_position, new_height= 0, 1
new_height = driver.execute_script("return document.body.scrollHeight")
while True:
    articles = driver.find_elements(By.XPATH,"//*[contains(@class, 'ds-w-full ds-bg-fill-content-prime ds-overflow-hidden ds-rounded-xl ds-border ds-border-line ds-mb-4')]")
    for article in articles:
        h2_element = article.find_element(By.TAG_NAME, "h2")
        h2_text = h2_element.text
        Headings.append(h2_text)
        paragraphs = article.find_elements(By.TAG_NAME, "p")
        for paragraph in paragraphs:
             h2_text = paragraph.text
             Texts.append(h2_text)
    
    current_scroll_position += speed
    driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
    new_height = driver.execute_script("return document.body.scrollHeight")
    sleep(3)
    if len(set(Texts))>2000:
            break  
    if len(set(Texts))%70 == 0:
      df = pd.DataFrame(zip(Headings,Texts),columns=['Headings','Texts'])
      df.drop_duplicates()
      df.to_csv(f"{path}/cricinfo.csv",index=False)


print(len(set(Texts)))
df = pd.DataFrame(zip(Headings,Texts),columns=['Headings','Texts'])
df.drop_duplicates()
df.to_csv(f"{path}/cricinfo.csv",index=False)
