# Importing the required modules
import os
import sys
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import pyttsx3


engine = pyttsx3.init()

# empty list
data = []

# for getting the header from
# the HTML file
list_header = []
# soup = BeautifulSoup(open(path),'html.parser')
# header = soup.find_all("table")[0].find("tr")

url = "https://en.wikipedia.org/wiki/Delhi"
# url = "https://en.wikipedia.org/wiki/Football"
html_content = requests.get(url).text
soup = bs(html_content, 'html.parser')
table = soup.find_all('table', {"class":"wikitable"})

# print(table)

l1 = soup.find_all('table', {"class":"wikitable"})[0].find("tr")

header = soup.find_all('table', {"class":"wikitable"})[0].find_all("tr")[1]



# print(header)

for items in header:
	try:
		if items.get_text() != "\n":
			list_header.append(items.get_text())
	except:
		continue


print(list_header)


# for getting the data
HTML_data = soup.find_all('table', {"class":"wikitable"})[0].find_all("tr")[2:]

print(HTML_data)




for element in HTML_data:
	sub_data = []
	for sub_element in element:
		try:
			if sub_element.get_text() != "\n":
				sub_data.append(sub_element.get_text())
		except:
			continue
	data.append(sub_data)

# Storing the data into Pandas
# DataFrame
print(data)


dataFrame = pd.DataFrame(data = data, columns = list_header)

print(dataFrame)

# Converting Pandas DataFrame
# into CSV file
dataFrame.to_csv('tableDE.csv')


row_data = []
row_data.append(list(dataFrame.columns.values))

for i in range(len(dataFrame)):
	row_data.append(dataFrame.loc[i, :].values.tolist())


# for row in row_data:
# 	print(row)

row_no = len(row_data) + 1
col_no = len(row_data[0])
ini_text = "Table with " + str(row_no) + "rows and " + str(col_no) + "columns"

engine.say(ini_text)
engine.say(l1.get_text())

for row in row_data:
	for cell in row:
		engine.say(cell)

engine.runAndWait()

