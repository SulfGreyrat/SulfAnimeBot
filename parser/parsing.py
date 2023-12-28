from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import logging
import asyncio
import re

from main import db


async def main(url='https://jut.su/anime/'):
    try:
        with Driver(uc=True) as driver:
            await get_main_page(driver, url)
            await asyncio.sleep(5)
            await get_anime(driver)
    except Exception as e:
        print(e)
    finally:
        driver.quit()
        
async def get_main_page(driver, url):
    page_number = 1
    while True:
        try:
            page_url = f'https://jut.su/anime/page-{page_number}'
            driver.get(page_url)
            animes = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'all_anime_global')))
            if not animes:
                break

            for anime in animes:
                anime_name = WebDriverWait(anime, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'aaname'))).text
                anime_series = WebDriverWait(anime, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'aailines'))).text
                anime_link = WebDriverWait(anime, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a'))).get_attribute('href')
                print(f'{anime_name} -- {anime_link}')
                db.add_anime(anime_name, anime_link, anime_series)
            
            page_number += 1
        except Exception as e:
            print(f'Error on page {page_number}: {e}')
            break
        
        
    
async def get_anime(driver):
    try:
        links = db.get_links()
        for link in links:
            print(link[2])
            driver.get(link[2])
            try:
                name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'header_video'))).text.replace('Смотреть ', '').replace(' все серии', '').replace(' и сезоны', '')
                options = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'under_video_additional'))).text
                describtion = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'under_video'))).text
                img = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'all_anime_title')))
                img_style = img.get_attribute('style')
                img_link = re.search(r"url\(['\"]([^'\"]+)['\"]\)", img_style)
                image_url = 'https://static8.tgstat.ru/channels/_0/48/481b862ac84bfaeb7787c6c71010028f7a.jpg'
                if img_link:
                   image_url = img_link.group(1)
                print(name, options, describtion, image_url)
                db.update_anime(name, options, describtion, image_url)
        
            except Exception as e:
                print(e)
    except Exception as e:
        #print(e)
        pass
