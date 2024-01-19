import pyttsx3
from bs4 import BeautifulSoup as bs
import requests
import time
import networkx as nx
import wikipediaapi
import wikipedia
from nltk.tokenize import sent_tokenize
import re
import nltk
# import spacy 
# from spacy import displacy 

# from prototype_link_extracter import link_extractor

wiki = wikipediaapi.Wikipedia('en')
# page_wiki = wiki.page("Udaipur")
# res = sent_tokenize(page_wiki.summary);
# print(res)

base_url = "https://en.wikipedia.org/wiki/"
search_term = input("Enter Search term: ")

final_url = base_url + search_term

print(final_url)


# url = "https://en.wikipedia.org/wiki/Cricket"
html_content = requests.get(final_url).text
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
# print(main_para[1])
# print(main_para[0])



para = main_para[0]
links = para.find_all("a", href=True)
print(links)


list_dict = {}
list_of_links = []
for i in range(0,len(links),5):
    print(links[i]['href'])
    if links[i]['href'].startswith("#"):
        continue
    else:
        if(links[i].string != None):
            list_of_links.append(links[i].string)

print(list_of_links)



if 'batting side' in list_of_links:
    list_of_links.remove('batting side')
if 'catching' in list_of_links:
    list_of_links.remove('catching')

for item in list_of_links:
    print(item)
    list_dict[item] = wikipedia.summary(item, sentences = 2);



print(len(list_of_links))

print(list_dict)


text = para.get_text()
text = sent_tokenize(text);

print(text)

final_string = ""

# sentence = text
# tokens = nltk.word_tokenize(sentence)
# print("tokens = ", tokens) 

# tagged = nltk.pos_tag(tokens)

# entities = nltk.chunk.ne_chunk(tagged)
# #print("entities = ", entities) 

# nlp = spacy.load("en_core_web_sm")
# sentence = text
# doc = nlp(sentence)
# print(f"{'Node (from)-->':<15} {'Relation':^10} {'-->Node (to)':>15}\n")
# #for token in doc:
#     #print("{:<15} {:^10} {:>15}".format(str(token.head.text), str(token.dep_), str(token.text)))
# displacy.render(doc, style='dep')

for line in text:
    final_string += line + " "
    for i in range(len(list_of_links)):
        if list_of_links[i] in line:
            final_string += list_dict[list_of_links[i]] + " "


final_string = re.sub(r'\[[^0-9]*\]', ' ', final_string)
final_string = re.sub('[^a-zA-Z]', ' ', final_string)
final_string = re.sub(r'\s+', ' ', final_string)

print(final_string)

engine.say(final_string)
engine.runAndWait()


#######################################################################################
#######################################################################################


"""
# replace_text = " this is the definition"
text = para.get_text()
text = sent_tokenize(text);

print(text)

final_string = ""

for line in text:
    final_string += line + " "
    for i in range(len(list_of_links)):
        if list_of_links[i] in line:
            final_string += list_dict[list_of_links[i]] + " "

print(final_string)


engine.say(final_string)
engine.runAndWait()
"""
