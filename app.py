import requests
from bs4 import BeautifulSoup


url = 'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a'

resp = requests.get(url=url,verify=False)

soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)