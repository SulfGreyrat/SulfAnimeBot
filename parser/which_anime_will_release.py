from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sqlite3

import time
import logging
import asyncio


def which_anime_will_enter(url='https://animego.org/'):
    try:
        with Driver(uc=True) as driver:
            driver.get(url)
            main_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'mb-md-0')))

            main__page = WebDriverWait(main_page, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-expanded='true']")))
            print(main__page.text)

            db = sqlite3.connect("BotDB.db")
            cursor = db.cursor()
            
            cursor.execute("DELETE FROM todays_anime")
            db.commit()
            
            animes = WebDriverWait(main__page, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'list-group-item')))
            for anime in animes:
                print(anime.text)
                cursor.execute("INSERT INTO todays_anime (text) VALUES (?)", (anime.text,))
                db.commit()
            
    except Exception as e:
        print(f"error {e}")
        
#async def pars_main(driver):
#    main_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'mb-md-0 ')))
#    on_clicks = WebDriverWait(main_page, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'bb-dashed-1')))
#    
#    for on_click in on_clicks:
#        on_click.click()
#    
#    main__page = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'mb-md-0 '))).text
#    print(main__page)
#
#    return main__page
