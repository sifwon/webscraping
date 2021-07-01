from selenium import webdriver
import time
import pandas as pd
import os
import datetime
keyword="python"
keyword
url="http://re-zero-anime.jp/tv/"
r=requests.get(url)
time.sleep(3)
soup=BeautifulSoup(r.text,)