from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Driver(uc=True)

aname = 'англельские ритмы кадры'
aname = aname.replace(' ', '+')
url = f'https://www.google.com/search?q={aname}&sca_esv=593440848&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiiy-PbtqiDAxUUQlUIHb-SD2UQ_AUoAXoECAQQAw&biw=1264&bih=694'

driver.get(url)