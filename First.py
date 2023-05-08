from bs4 import BeautifulSoup
# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup
# Importing the HTTP library
import requests as req
from tqdm import tqdm
#from extract import filename 
import os 
import sys

path = "/Users/zourubin/Desktop/kani/arXiv-MDTE-key-word-extraction/parser example/dataset/0001/astro-ph0001032.html"
html = open(path)
soup = BeautifulSoup(html, features="html.parser")
text = soup.get_text()
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = '\n'.join(chunk for chunk in chunks if chunk)
# for word in text:
#     print('yes')
text

def find_sentences_with_word(string, word):
    sentences = string.split(".")  # Split the string into individual sentences

    # Iterate over the sentences and print those containing the target word
    for sentence in sentences:
        if word in sentence:
            print(sentence)
            return
    print('target word not found in this file')

# Example usage
input_string = text
target_word ="cameras"

find_sentences_with_word(input_string, target_word)