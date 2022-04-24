from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class Scraper:
    def scrape(zip: str):
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
        prefs = {
            'profile.default_content_setting_values':
            {
                'automatic_downloads': 0
            },
            'profile.content_settings.exceptions':
            {
                'automatic_downloads': 0
            },
            "download.default_directory" : "/home/appuser"
        }

        options.add_experimental_option('prefs', prefs)

        url = f"https://www.redfin.com/zipcode/{zip}/filter/include=sold-5yr"
        driver.get(url)
        time.sleep(5)
        driver.find_element_by_id("download-and-save").click()
        time.sleep(5)
