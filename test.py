from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Chromeドライバーを取得
driver = webdriver.Chrome(executable_path="/Users/chocolate/Desktop/Python/chromedriver")

try:
    # youtubeを開く
    driver.get('https://www.youtube.com')

    # 要素が出現するまで待機
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='endpoint']")))

    # 要素を取得
    element = driver.find_element_by_xpath('//*[@id="endpoint"]')

    print("element{}".format(element))

    #入力待ち
    input()
except:
    print("えらーだよ！！たいへんだー！")
finally:
    # ブラウザを閉じる
    driver.quit()