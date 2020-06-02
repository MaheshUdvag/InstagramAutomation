from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\Mahesh\Desktop\chromedriver.exe')
driver.get("https://www.instagram.com/?hl=en")

time.sleep(3)
email = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
email.send_keys('your username')

time.sleep(4)
password = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
password.send_keys('your password')

time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()

time.sleep(4)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()

time.sleep(5)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()