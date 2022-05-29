from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from os import listdir, remove
from os.path import isfile, join, splitext
import csv

class Scraper:
    def get_selenium():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        options.add_argument("--start-maximized") #open Browser in maximized mode
        options.add_argument("--no-sandbox") #bypass OS security model
        options.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        options.binary_location = '/usr/bin/google-chrome-stable'
        driver = webdriver.Chrome(options=options, executable_path="/usr/local/bin/chromedriver")
        
        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        return driver

    def scrape(zip: str):
        driver = Scraper.get_selenium()
        url = f"https://www.redfin.com/zipcode/{zip}/filter/include=sold-5yr"
        driver.get(url)
        time.sleep(5)
        driver.find_element_by_id("download-and-save").click()
        time.sleep(5)

    def process_address_csv(address=".", remove_file=True):
        files = [file for file in listdir(address) if isfile(join(address, file))]
        csv_dicts = []
        for file in files:
            if splitext(file)[1] == ".csv":
                with open(join(address, file), "r") as infile:
                    reader = csv.DictReader(infile)
                    for row in reader:
                        csv_dicts.append(
                            {
                                "address": row["ADDRESS"],
                                "city": row["CITY"],
                                "state": row['STATE OR PROVINCE'],
                                "zip": row['ZIP OR POSTAL CODE'],
                                "latitude": row['LATITUDE'],
                                "longitude": row['LONGITUDE']
                            }
                        )
                if remove_file == True:
                    remove(file)
        return csv_dicts
