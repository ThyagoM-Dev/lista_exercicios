
# Python v2.7 (because of mechanize requirement)
# pip install re
# pip install bs4
# pip install mechanize
#######################

import re
import mechanize
from bs4 import BeautifulSoup

url = "http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/"

def open_url(browser, url):
    return browser.open(url).read()

def extract_contest_number(soup):
    r = soup.find("div", "title-bar").contents[3].span.string
    return re.search('[0-9]{4}', r).group(0)
    
def extract_tags(soup):
   return soup.find_all("ul", "numbers")

def extract_numbers(r):
    numbers = []
    for i in range(6):
        numbers.append(r[0].contents[i].string)
    return numbers

def write_result(numbers):
    results = ",".join(numbers)
    f = open("result_list.txt", "a")
    f.write(results+'\n')
    f.close()


browser = mechanize.Browser()
html = open_url(browser, url)
soup = BeautifulSoup(html, "html5lib")

resulted_number = int(extract_contest_number(soup))

# decrescent results
while resulted_number > 0:
    r = extract_tags(soup)
    numbers = extract_numbers(r)
    write_result(numbers)
    
    resulted_number -= 1
    
    browser.select_form(name="buscaForm")
    browser["concurso"] = str(resulted_number)
    next_html = browser.submit()
    
    soup = BeautifulSoup(next_html, "html5lib")