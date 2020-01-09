from selenium import webdriver

# Указываем полный путь к geckodriver.exe на вашем ПК.
driver = webdriver.Chrome('D:\chromedriver\chromedriver.exe')
driver.get("http://www.google.com")
element = driver.find_element_by_class_name('hpuQDe')
element.click()