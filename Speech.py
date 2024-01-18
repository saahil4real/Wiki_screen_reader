import pyttsx3
from bs4 import BeautifulSoup as bs
import requests
import time

url = "https://en.wikipedia.org/wiki/Cricket"
html_content = requests.get(url).text
soup = bs(html_content, 'html.parser')

table = soup.find("table", attrs={"class": "wikitable"})

table_data = table.tbody.find_all("tr")
table_headings = table_data[0]
table_rows = table_data[1:]

headings = []
for th in table_headings.find_all("th"):
  headings.append(th.text.replace('\n', ' ').strip())

rows_data = []

for row in table_rows:
  new_row = []
  for th in row.find_all("th"):
    new_row.append(th.text.replace('\n', ' ').strip())
  for td in row.find_all("td"):
    new_row.append(td.text.replace('\n', ' ').strip())
  rows_data.append(new_row)


engine = pyttsx3.init()

for heading in headings:
    engine.say(heading)

for row in rows_data:
    for cell in row:
        engine.say(cell)

# engine.say("I will speak this text")
# engine.say("I will speak this text")
engine.runAndWait()
# engine.say("I will speak this text")