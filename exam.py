import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.select import Select
# 读取输入参数
date = sys.argv[1]
currency_code = sys.argv[2]

driver = webdriver.Chrome()
total={'GBP':'英镑',
'HKD':'港币',
'USD':'美元',
'CHF':'瑞士法郎',
'SGD':'新加坡元',
'SEK':'瑞典克朗',
'DKK':'丹麦克朗',
'NOK':'挪威克朗',
'JPY':'日元',
'CAD':'加拿大元',
'AUD':'澳大利亚元',
'EUR':'欧元',
'MOP':'澳门元',
'PHP':'菲律宾比索',
'THP':'泰国铢',
'NZD':'新西兰元',
'KRW':'韩元',
'RUB':'卢布',
'MYR':'林吉特',
'TWD':'新台币',
'ESP':'西班牙比塞塔',
'ITL':'意大利里拉',
'NLG':'荷兰盾',
'BEF':'比利时法郎',
'FIM':'芬兰马克',
'IDR':'印尼卢比',
'BRL':'巴西里亚尔',
'AED':'阿联酋迪拉姆',
'INR':'印度卢比',
'ZAR': '南非兰特',
'SAR': '沙特里亚尔',
'TRY': '土耳其里拉',
}

try:
    # 打开中国银行外汇牌价网站
    url = 'https://www.boc.cn/sourcedb/whpj/'
    driver.get(url)
    time.sleep(1)
    # 等待日期输入框加载完成
    date_input_locator = driver.find_element(By.CLASS_NAME, "title")
    print(date_input_locator)

    time.sleep(1)
    date_input = driver.find_elements(By.CLASS_NAME,"search_ipt")[2]
    date_input.clear()
    date_input.send_keys(date)
    print(date_input)
    time.sleep(1)

    currency_select = driver.find_element(By.CSS_SELECTOR, '#pjname')

    result=total[currency_code]
    print(result)

    Select(currency_select).select_by_value(result)  # 通过value值定位
    time.sleep(1)

    button = driver.find_elements(By.CSS_SELECTOR, '.search_btn')[1]
    button.click()
    time.sleep(1)

    save=driver.find_element(By.XPATH,'/html/body/div/div[4]/table/tbody/tr[2]/td[4]').text
    print(save)
    time.sleep(1)
    with open('result.txt', 'w') as f:
        f.write(save)
    time.sleep(1)
finally:
    # 关闭浏览器
    driver.quit()