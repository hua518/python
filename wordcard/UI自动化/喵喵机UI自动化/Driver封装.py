from appium import webdriver
desired_caps = {}
desired_caps['newCommandTimeout'] = '180000'  ######要是没增加，appium60s未接到下一个命令会退出
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'ZLINBUMF99999999'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = 'com.oppo.settings.SettingsActivity'
desired_caps['noReset'] = True
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
def getdriver():
    #driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)  若把这个放进去，每次调用都会执再次启动appium
    return driver
if __name__ == '__main__':
    getdriver()