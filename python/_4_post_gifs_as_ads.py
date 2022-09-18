from english_words import english_words_set
import requests
import bs4
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

API_KEY = 'eHwxWlhTY3b0s0l0bcjGEOln4BXxBv41'
def get_patent_search_urls(index_url):
    response = driver.get(index_url)
    time.sleep(60)
    return [a.get_attribute('data-result') for a in driver.find_elements(By.CLASS_NAME, 'result-title.style-scope.search-result-item')]

def get_patent_abstract(index_url):
    response = driver.get(index_url)
    return driver.find_element(By.CLASS_NAME, 'abstract.patent-text').get_attribute('innerHTML')

def get_patent_text(index_url):
    response = driver.get(index_url)
    return driver.find_element(By.XPATH, '//div[@class="description style-scope patent-text"]').get_attribute('innerHTML')

def get_patent_title(index_url):
	response = driver.get(index_url)
	return driver.find_element(By.XPATH, '//h1[@id="title"]').get_attribute('innerHTML')

import json
from urllib import parse, request




for word in english_words_set:
	r = requests.post('https://www.babylonpolice.com/B/words/',data={'the_word_itself':word})
	print(r)
	url = "http://api.giphy.com/v1/gifs/search"
	params = parse.urlencode({
	  "q": word,
	  "api_key": API_KEY,
	  "limit": "5"
	})

	with request.urlopen("".join((url, "?", params))) as response:
		data = json.loads(response.read())
		print(json.dumps(data, sort_keys=True, indent=4))
	
	
	