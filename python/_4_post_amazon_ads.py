from english_words import english_words_set
import requests
import bs4
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)


def get_amazon_img(index_url):
    response = driver.get(index_url)
    print(driver.find_element(By.CLASS_NAME, 's-image').get_attribute('src'))
    return driver.find_element(By.CLASS_NAME, 's-image').get_attribute('src')

def get_amazon_url(index_url):
    response = driver.get(index_url)
    for each in driver.find_elements(By.CLASS_NAME, 'a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal'):
	    print(each.get_property('href'))
	    response = driver.get(each.get_property('href'))
	    driver.find_element(By.XPATH, '//a[@title="Text"]').click()
	    time.sleep(5)
	    for eaches in driver.find_elements(By.XPATH, "//textarea[@id='amzn-ss-text-shortlink-textarea']"):
		    print(eaches.get_attribute('innerHTML'))
		    return eaches.get_attribute('innerHTML')


login = "https://www.amazon.com.au/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com.au%2Fs%3Fk%3Dsell%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=auflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
response = driver.get(login)
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("kranked_354@hotmail.com")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("thatticklesQ-6313")
driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()



for word in english_words_set:
	base = "https://www.amazon.com.au/s?k="
	base += word
	print(word)
	r = requests.post('https://www.babylonpolice.com/B/words/',data={'the_word_itself':word})
	print(r.status_code)
	print(r.text)
	book_page = "https://www.amazon.com.au/"
	print(base)
	try:
		img = get_amazon_img(base)
		url = get_amazon_url(base)
		#print(title)
		#print(body)
		r = requests.post('https://www.babylonpolice.com/B/sponsor/',data={'the_sponsorship_phrase':word, "img":img, 'url':url, 'payperview':True, 'price_limit': 1, 'allowable_expenditure': 100000, 'author': '1'})
		print(r.status_code)
		print(r.text)
	except:
		print('empty')
