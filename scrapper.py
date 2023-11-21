from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv 

start_url="https://exoplanets.nasa.gov/exoplanet-catalog/"
browser=webdriver.Chrome()
browser.get(start_url)
time.sleep(10)
planets_data=[]
def scrape():
    headers=["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date"]
    planet_data=[]
    for i in range(0,490):
        soup=BeautifulSoup(browser.page_source,"html.parser")