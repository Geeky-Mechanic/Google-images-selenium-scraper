import os

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from get_links import fetch_image_urls
from persist_images import persist_image


def search_and_download(search_term: str, driver_path: str, target_path='./images', number_images=5):
    # Create the webdriver service
    service = Service(driver_path)

    # add some options for the chrome browser
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    target_folder = os.path.join(target_path, '_'.join(search_term.lower().split(' ')))

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    with webdriver.Chrome(service=service, chrome_options=chrome_options) as wd:
        res = fetch_image_urls(search_term, number_images, wd=wd, sleep_between_interactions=0.5)

    for elem in res:
        persist_image(target_folder, elem)