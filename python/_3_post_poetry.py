from english_words import english_words_set
import requests
import bs4
import cloudscraper
import re


ses = requests.Session()
ses.headers = { 'referer': 'https://magiceden.io/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'accept': 'application/json'}

scraper = cloudscraper.create_scraper(sess=ses)

def get_search_poem_urls(index_url):
    response = scraper.get(index_url, headers={
    'referer': 'https://magiceden.io/',
    'accept': 'application/json'
})
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    return [a.attrs.get('href') for a in soup.select('li a[href]')]

for word in english_words_set:
	base = "https://www.poetryfoundation.org/search?query="
	base += word
	print(word)
	r = requests.post('https://www.babylonpolice.com/B/words/',data={'the_word_itself':word})
	print(r.status_code)
	print(r.text)
	for a in set(get_search_poem_urls(base)):
		print(a)
		book_page = "https://www.poetryfoundation.org"
		if len(a)<40:
			if '/poems/' in a:
				print(book_page+a)
				url = book_page+a
				r = scraper.get(url)
				if bs4.BeautifulSoup(r.content, 'html.parser').find_all('h1'):
					title = bs4.BeautifulSoup(r.content, 'html.parser').find_all('h1')[0].text
					body = bs4.BeautifulSoup(r.content, 'html.parser').find_all('div', class_="o-poem")[0].text
					print(title)
					r = requests.post('https://www.babylonpolice.com/B/posts/',data={'title':title, "body":body})
					print(r.status_code)
					print(r.text)