from english_words import english_words_set
import requests
import bs4
import time

import json
from urllib import parse, request


import space
import wikiquote

import torch

from torchtext.datasets import AG_NEWS
train_iter = iter(AG_NEWS(split='train'))

artists = ["Beyonce", "Plato"]
for artist in artists:
	articles = wikiquote.search(artist)
	for article in articles:
		quotes = wikiquote.quotes(article)
		for quote in quotes:
			

			
	