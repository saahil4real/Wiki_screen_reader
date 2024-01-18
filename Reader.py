import pyttsx3
from bs4 import BeautifulSoup as bs
import requests
import time
from prototype_link_extracter import link_extractor

# import nltk
# nltk.download('punkt')

# print("done")

# import nltk
# import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

# nltk.download()

def_dict = link_extractor("https://en.wikipedia.org/wiki/Delhi")
# print(def_dict)
for i in def_dict.keys():
    print(i)

url = "https://en.wikipedia.org/wiki/Delhi"
html_content = requests.get(url).text
soup = bs(html_content, 'html.parser')

engine = pyttsx3.init()
rate = engine.getProperty('rate')
# print(rate)
engine.setProperty('rate', 150)

# s = "This is a string."
# result = s.split(" ")
# print(result)

paras = soup.find_all("p")
main_para = []
for para in paras:
    if len(para.get_text()) > 50:
        # engine.say(para.get_text())
        main_para.append(para)

# print(main_para[0])
para = main_para[0]
links = main_para[0].find_all("a", href=True)

list_of_links = []
for item in links:
    print(item)
    list_of_links.append(item.string)

for item in list_of_links:
    print(item)

replace_text = " this is the definition"
text = para.get_text()

# print(len(text))
# print(text)

for link in links:
    text = text.replace(link.string, link.string+replace_text, 1)
print(text)
# engine.say(text)
# engine.runAndWait()
