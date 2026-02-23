from bs4 import BeautifulSoup
import requests
import sys
import re


def url_processing(url_input):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    content = requests.get(url_input, headers=headers)

    soup = BeautifulSoup(content.text, 'html.parser')

    if (soup.body):
        body_text = soup.body.get_text().lower()
    else :
        print("Body text not found")

    words = re.findall(r'[a-z0-9]+', body_text)

    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else :
            word_dict[word] = 1

    return word_dict

def hash_fun (word):
    p = 53    #given in qs
    m = 2**64  #given in qs
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

def common_bits(hash1,hash2,b):
    count = 0
    for i in range(b):
        bit1 = (hash1 >> i) & 1
        bit2 = (hash2 >> i) & 1
        if (bit1 == bit2):
            count+=1
    return count

if __name__ == "__main__":
    url1 = sys.argv[1]
    url2 = sys.argv[2]
    word_dict1 = url_processing(url1)
    word_dict2 = url_processing(url2)
    b = 64 #Or We can take value of b from user.
    simhash1 = cal_simhash(word_dict1,b)
    simhash2 = cal_simhash(word_dict2,b)
    count_common_bits = common_bits(simhash1,simhash2,b)
    print("Common Bits :", count_common_bits)






    









    




