from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import path

CUR_DIR = path.dirname(path.abspath(__file__))  # __file__ 代表現在這個檔案，也就是session_ios
APP = path.join(CUR_DIR, 'TheApp.apk')
# 因為我們將application和python檔案放在同一個目錄，所以可以用file的目錄帶出application的目錄
# 用APP這個常數表示application完整的路徑、名稱

APPIUM = 'http://localhost:4723'
# 全大寫的變數沒有一定要這樣做，只是凸顯他是個constant

CAPS = {
    'platformName': 'Android',
    # 'platformVersion': '13.6', 
    # 如果找不到，就會出現error，也可以直接整個省略
    'deviceName' : 'Android Emulator',
    'automationName': 'UiAutomator2', # 根據啟動appium後跑出的建議
    'app': APP,
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)
try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Login Screen')
    ))
    driver.find_element(MobileBy.CLASS_NAME, 'android.widget.TextView')
    driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Webview Demo"]')
finally:
    driver.quit()