from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import logging
import asyncio
import re

from googletrans import Translator
from AnilistPython import Anilist

anilist = Anilist()

from main import db


def translate_text(text, target_language='en'):
    try:
        translator = Translator()
        translation = translator.translate(text, dest=target_language)
        return translation.text
    except:
        print(f"Eror ocured when we tarnslate:\n{text}")

#####  Jutsu parser  ##################


async def main(url='https://jut.su/anime/'):
    try:
        with Driver(uc=True) as driver:
            await get_main_page(driver, url)
            await get_anime(driver)
    except Exception as e:
        print(e)
        
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
            driver.get(link[0])
            try:
                name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'header_video'))).text.replace('Смотреть ', '').replace(' все серии', '').replace(' и сезоны', '')
                options = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'under_video_additional'))).text
                
                orig_name = re.search(f"Оригинальное название:(.+)", options, flags=re.IGNORECASE)

                if orig_name:
                    orig_name = orig_name.group(1).strip()
                    print(orig_name)
                
                year = re.search(f"Год выпуска:(.+)", options, flags=re.IGNORECASE)
                
                if year:
                    year = year.group(1).strip()
                    print(year)
                
                genre = re.search(f"Жанры:(.+)", options, flags=re.IGNORECASE)
                
                if genre:
                    genre = genre.group(1).strip()
                    print(genre)
                
                describtion = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'under_video'))).text
                img = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'all_anime_title')))
                img_style = img.get_attribute('style')
                img_link = re.search(r"url\(['\"]([^'\"]+)['\"]\)", img_style)
                image_url = 'https://static8.tgstat.ru/channels/_0/48/481b862ac84bfaeb7787c6c71010028f7a.jpg'
                if img_link:
                   image_url = img_link.group(1)
                print(name, options, describtion, image_url)
                db.update_anime(name, orig_name, year, genre, describtion, image_url)
        
            except Exception as e:
                print(e)
                
    except Exception as e:
        #print(e)
        pass

##### YammyAnimeTv parser ######

async def start_pars():
    try:
        with Driver(uc=True) as driver:
            driver.get('https://yummyanime.tv/series/page/1/')
            await pagination(driver)
    except Exception as e:
        print(f'Eror in start pars yammy anime tv \n {e}')
        
async def pagination(driver):
    try:
        pagination_main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'pagination__inner')))
        pag_page = WebDriverWait(pagination_main, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'span')))
        page = next((x.text for x in pag_page if x.text.isdigit()), None)
        print(f"PAGE: {page}")
        url = f'https://yummyanime.tv/series/page/{int(page) + 1}/'
        await process_link(driver, url)
    except Exception as e:
        print(f'error {e}')
        return 
        
async def process_link(driver, url):
    try:
        driver.get(url)
        await get_yammy_animes(driver)
        await get_yammy_anime(driver)
    except Exception as e:
        print(e)
        
async def get_yammy_anime(driver):
    names = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'movie-item__title')))
    
    await pagination(driver)
    
async def get_yammy_animes(driver):
    animes = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'movie-item')))
 
########## AnimeGO pars

async def anime_go():
    try:
        with Driver(uc=True) as driver:
            page_number = 1
            while True:
                try:
                    page_url = f'https://animego.org/anime/{page_number}'
                    driver.get(page_url)
                    animes = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'animes-list-item')))
                    await asyncio.sleep(2)
                    
                    for i in range(30):
                        driver.execute_script("window.scrollBy(0, 140)")

                    if not animes:
                        break
                    
                    print(len(animes))

                    for anime in animes:
                        body = WebDriverWait(anime, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'media-body')))
                        ratting = WebDriverWait(anime, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'animes-list-item-picture'))).text
                        anime_name = WebDriverWait(body, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'mb-1'))).text
                        orig_name = WebDriverWait(body, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'text-gray-dark-6'))).text
                        year = WebDriverWait(body, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'anime-year'))).text
                        anime_link = WebDriverWait(anime, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a'))).get_attribute('href')

                        img = WebDriverWait(anime, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'anime-list-lazy')))
                        img_style = img.get_attribute('style')
                        img_link = re.search(r"url\(['\"]([^'\"]+)['\"]\)", img_style)
                        
                        image_url = 'no img'
                        desc = 'trsfhhhf'
                        genre = 'fsghdfghdfgh'
                        
                        if img_link:
                           image_url = img_link.group(1)  
                        
                        try:
                            genre = WebDriverWait(body, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'anime-genre'))).text
                        except:
                            genre = "NO GENRE"
                            print('NO GENRE')
                            
                        db.add_animego(anime_name, desc, ratting, year, orig_name, genre, anime_link, image_url)

                        print(f"Name: {anime_name}\nOriginal: {orig_name}\nYear: {year}\nRatting: {ratting}\nIMG: {image_url}\nLink: {anime_link}\n\n")

                        #anime_series = WebDriverWait(anime, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'aailines'))).text
                        #anime_link = WebDriverWait(anime, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a'))).get_attribute('href')
                        #print(f'{anime_name} -- {anime_link}')
                        #db.add_anime(anime_name, anime_link, anime_series)

                    page_number += 1
                except Exception as e:
                    print(f'Error on page {page_number}: {e}')
                    break
    except Exception as e:
        print(f'Eror in start pars yammy anime tv \n {e}')
