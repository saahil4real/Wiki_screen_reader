
import requests
import networkx as nx
import wikipediaapi
from nltk.tokenize import sent_tokenize
from gensim.summarization import summarize
from bs4 import BeautifulSoup

def link_extractor(url):

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

    fix = "https://en.wikipedia.org" 
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    wiki = wikipediaapi.Wikipedia('en')

    a_tags = soup.find_all("a", href=True)
    links = []
    extra_links = []

    for link in a_tags:
        if link.text:
            if(link["href"][0]!='#'):{
                links.append(link["href"])
            }

    cleaned_links = list(set(links))

    for link in cleaned_links:
        if(link[0]=='h'):
            extra_links.append(link)
            cleaned_links.remove(link)

    def_urls = []
    summary_titles={}
    page_details = []

    for link in cleaned_links:
        if(link[0:6] == "/wiki/"):
            url_temp = fix + link
            def_urls.append(url_temp)
            summary_titles[url_temp] = link[6:]
        else:
            extra_links.append(link)
            cleaned_links.remove(link)

    # for url in def_urls:
    #     print(url)

    # print(len(def_urls))
    ################  For Extracting the text for the cleaned wikipedia links but the time complexity is way too much #################


    #   PAGERANK

    G = nx.barabasi_albert_graph(len(def_urls),76)
    pr = nx.pagerank(G,0.4)
    pr_values = list(pr.values())
    dic = {}
    for i in range(len(def_urls)):
        dic[def_urls[i]]=pr_values[i]

    dic = dict(sorted(dic.items(), key=lambda item: item[1]))
    # print(dic)

    sorted_scores = []

    for link,pr_score in dic.items():
        t = []
        t.append(pr_score)
        t.append(link)
        t.append(summary_titles[link])
        sorted_scores.append(t)

    sorted_scores.sort()
    sorted_scores.reverse()
    # for score in sorted_scores:
    #     print(score)

    count = len(sorted_scores)//20


    test_links=[]
    for i in range(count):
        test_links.append(sorted_scores[i])

    # print(test_links)

    # for u in test_links:
    #     print(u)

    test_def = {}

    # for i in range(count):
    #     req_test = requests.get(test_links[i][1], headers)
    #     soup_test = BeautifulSoup(req_test.content, 'html.parser')
    #     test_def[test_links[i][1]] = soup_test.find("div",{"id":"mw-content-text"})
        
    # for link,definition in test_def.items():
    #     print(link)
    #     temp = []
    #     temp.append(dic[link])
    #     test_def[link] = temp

    for i in range(count):
        page_wiki = wiki.page(test_links[i][2])
        #test_def[test_links[i][1]] = sent_tokenize(page_wiki.summary);
        test_def[test_links[i][1]] = summarize(page_wiki.summary);

    return test_def

