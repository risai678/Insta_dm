from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome('./chromedriver')


def login(username, your_password):
    driver.get('https://www.instagram.com/')
    sleep(4)

    usern = driver.find_element_by_name("username")
    usern.send_keys(username)
    # finds the password box
    passw = driver.find_element_by_name("password")
    # sends the entered password
    passw.send_keys(your_password)
    passw.send_keys(Keys.RETURN)
    sleep(5.5)

    sleep(5)


def send_message():
    driver.get('https://www.instagram.com/amritpalsingh3178/')
    sleep(5)
    message = driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy    _8A5w5    ']")
    message.click()
    sleep(3)
    area = driver.find_element_by_xpath("//textarea[@placeholder='Message...']")
    area.send_keys('Hello how are you?  ')
    # area.send_keys(Keys.RETURN)
    area.send_keys(Keys.SHIFT, Keys.RETURN)
    area.send_keys('This is testing message ')
    area.send_keys(Keys.SHIFT, Keys.RETURN)
    area.send_keys('only for testing purpose')
    sleep(4)
    area.send_keys(Keys.RETURN)
    sleep(8)

def get_likes():
    driver.get('https://www.instagram.com/vikram7309/')
    listt=[]
    sleep(5)
    post_urls = driver.find_elements_by_xpath("//div[@class='Nnq7C weEfm']")

    for i in post_urls:
        bb=i.find_element_by_tag_name('a')
        listt.append(bb.get_attribute('href'))
    print(listt)
    for m in listt:
        driver.get(str(m))
        sleep(7)
        post_urls = driver.find_element_by_xpath(
            "//div[@class='_7UhW9   xLCgt      MMzan   KV-D4           uL8Hv        T0kll ']").text
        print(post_urls)
        driver.find_element_by_xpath(
            "//div[@class='_7UhW9   xLCgt      MMzan   KV-D4           uL8Hv        T0kll ']").click()
        sleep(3)




username=''
passs=''
login(username,passs)
# send_message()
get_likes()

