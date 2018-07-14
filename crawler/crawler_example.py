# -*- coding: utf-8 -*-
"""
@author: Artur Franco
"""

# --------------------------------------------------

import requests
from bs4 import BeautifulSoup

# imprimir texto
pag = requests.get("http://dnd.wizards.com/").text
# transformar o texto em DOM (Document Object Model), sofre parser
soup = BeautifulSoup(pag, "lxml")

# buscando 6 links de matérias
links = soup.find_all('div', {'class', 'module_highlighted-products--product'})

# capturando 1 endereco
address = links[0].find('a').get('href')
print(address)

# --------------------------------------------------
i = 0;
for link in links:
    url = "http://dnd.wizards.com/"+link.find('a').get('href');
    pag = requests.get(url).text;
    
    # escrever resultado
    file = open('new '+str(i)+'.html', 'w');
    file.write(pag);
    file.close();
    i+=1;
