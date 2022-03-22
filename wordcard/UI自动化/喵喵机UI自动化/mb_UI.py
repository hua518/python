from UI自动化.喵喵机UI自动化 import Driver封装

Driver封装.getdriver().back()
# driver.swipe(start_x=538,start_y=1504,end_x=538,end_y=404)   ####页面拖拽
# driver.find_element_by_android_uiautomator('new UiSelector().text("喵喵机")').click()   ####原生定位
# driver.find_elements_by_class_name("android.widget.TextView")[2].click()                ####class_name中有多个，引入数组其中为index
# driver.find_element_by_xpath("//*[@text='喵喵机']").click()
# driver.find_elements_by_xpath("//*[@class='android.widget.TextView']")[2].click()