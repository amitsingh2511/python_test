import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService

# importing webdriver from selenium
from selenium import webdriver

from PIL import Image

# Here Chrome will be used
driver = webdriver.Chrome()

# URL of website
url = "https://www.geeksforgeeks.org/"

# Opening the website
driver.get(url)

driver.save_screenshot("image.png")

# Loading the image
image = Image.open("image.png")

# Showing the image
image.show()


# def take_screenshot(url, output_filename):
#     # Initialize the web driver (replace 'chromedriver' with the path to your driver executable)
#     # driver = webdriver.Chrome(ChromeDriverManager(version="114").install())

#     # Open the web page
#     try:
#         chromedriver_path = r"C:/Users/Amit Singh/Downloads/chromedriver_win32/chromedriver.exe"
#         # Open the web page
#         # option = webdriver.ChromeOptions()
#         # option.add_argument("--headless")
#         # driver = webdriver.Chrome(ChromeDriverManager().install())

#         # driver = webdriver.Chrome(executable_path=chromedriver_path)

#         driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
#         # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
#         driver.get(url)

#         # Take a screenshot and save it
#         driver.get_screenshot_as_file(output_filename)
#         print(f"Screenshot saved as '{output_filename}'")
#     except Exception as e:
#         print(f"Error: {e}")
#     finally:
#         # Close the web driver
#         driver.quit()

# # Input URL
# url = "https://www.indiatoday.in/india/story/new-expressway-kashmir-kanyakumari-cag-report-nitin-gadkari-2423440-2023-08-19"

# # Output filename for the screenshot
# output_filename = "screenshot.png"

# # Call the function to capture a screenshot
# take_screenshot(url, output_filename)

# print(f"Screenshot saved as '{output_filename}'")