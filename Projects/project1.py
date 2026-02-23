from bs4 import BeautifulSoup
import requests
import sys

url_input = sys.argv[1]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

content = requests.get(url_input, headers=headers)

soup = BeautifulSoup(content.text, 'html.parser')

if soup.title:
    print("Web Page Title : ", soup.title.text)
else :
    print ("Page title not found")

print("Web Page Body Text : ")
if soup.body:
    body_text = soup.body.get_text().strip()
    print(body_text)
else :
    print("This web page does not contain any text in it's body.")

print("Links attached to web page : ")
links = soup.find_all('a')
for link in links:
    print(link.get('href'))


