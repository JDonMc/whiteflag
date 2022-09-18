from english_words import english_words_set
import requests
import bs4
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)


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


for word in english_words_set:
	base = "https://patents.google.com/?num=100&q="
	base += word + '&oq=' + word
	print(word)
	r = requests.post('https://www.babylonpolice.com/B/words/',data={'the_word_itself':word})
	print(r.status_code)
	print(r.text)
	for a in set(get_patent_search_urls(base)):
		print(a)
		book_page = "https://patents.google.com/"
		if len(a)<60:
			print(book_page+a)
			try:
				title = get_patent_title(book_page+a)

				body = "Abstract:" + get_patent_abstract(book_page+a) + " - Description: " + get_patent_text(book_page+a)
				#print(title)
				#print(body)
				if body:
					chapter_counter = 0
					body_len = len(body)
					for chapter in range(0, body_len, 144000):
						chapter_counter += 1
						r = requests.post('https://www.babylonpolice.com/B/posts/',data={'title':title[0:100] + ' Chapter '+ str(chapter_counter), "body":body[(chapter_counter-1)*144000:chapter_counter*144000]})
						print(r.status_code)
						print(r.text)
			except:
				print('empty')