from bs4 import BeautifulSoup
import requests
import sys
import re

url_input = sys.argv[1]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

content = requests.get(url_input, headers=headers)

soup = BeautifulSoup(content.text, 'html.parser')

if (soup.body):
    body_text = soup.body.get_text.lower()
else :
    print("Body text not found")

words = re.findall(r'[a-z0-9]+', body_text)

word_dict = {}
for word in words:
    if word in word_dict:
        word_dict[word] += 1
    else :
        word_dict[word] = 1

def hash_fun (word):
    p = 53
    m = 2**64
    i = 1
    hash_value = 0
    for char in word:
        hash_value = (hash_value + (ord(char)*i))%m
        i = (i * p)%m
    return hash_value

def cal_simhash(word_dict,b):
    V = [0]*b
    for word,count in word_dict.items():
        hash_val = hash_fun(word)
        for i in range(b):
            mask = 1 << i
            if (hash_val & mask):
                V[i] += count
            else:
                V[i] -= count
    fingerprint = 0
    for i in range(b):
        if V[i] > 0:
            fingerprint = fingerprint | (1<<i)
    return fingerprint









    




