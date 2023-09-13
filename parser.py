from bs4 import BeautifulSoup

# Specify the encoding when opening the file
with open('index.html', 'r', encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, 'lxml')
print(soup)