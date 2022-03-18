from 喵喵机UI自动化 import Driver封装

def yuansu():
    Driver封装.getdriver().back()
    print("输入元素定位方式："
          "1-find_element_by_android_uiautomator(name)\n"
          "2-driver.find_element_by_xpath\n"
          "3-driver.find_elements_by_class_name")
    name = input()
    name1 = int(name)
    if name1==1:
        print("输入元素")
        yuansu=input()
        Driver封装.getdriver().find_element_by_android_uiautomator(yuansu).click()   ####原生定位   new UiSelector().text("喵喵机")
    elif name1==2:
        print("输入元素")
        yuansu1 = input()
        Driver封装.getdriver().find_element_by_xpath(yuansu1).click()
yuansu()