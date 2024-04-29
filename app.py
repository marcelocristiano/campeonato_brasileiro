import requests
from bs4 import BeautifulSoup
import datetime
import time
import json

list_dados = []
ano_inicio = 2012
ano_atual = datetime.datetime.now().year

for ano in range(ano_inicio, ano_atual + 1):
    print(ano)
    url = 'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/{}'.format(ano)

    resp = requests.get(url=url,verify=False)

    soup = BeautifulSoup(resp.text, 'html.parser')

    if soup.find(class_="table m-b-20 tabela-expandir").find('tbody').find_all('tr', class_='expand-trigger'):
        tabela_expandida = soup.find(class_="table m-b-20 tabela-expandir").find('tbody').find_all('tr', class_='expand-trigger')
    else:
        tabela_expandida = soup.find(class_="table m-b-20 tabela-expandir").find('tbody').find_all('tr')
  
    for i in range(20):
        posicao = tabela_expandida[i].find('td').find('b').text
        clube = tabela_expandida[i].find(class_= 'hidden-xs').text
        pontos = tabela_expandida[i].find('th').text
        jogos = tabela_expandida[i].find_all('td')[1].text
        vitorias = tabela_expandida[i].find_all('td')[2].text
        empates = tabela_expandida[i].find_all('td')[3].text
        derrotas = tabela_expandida[i].find_all('td')[4].text
        gols_pro = tabela_expandida[i].find_all('td')[5].text
        gols_contra = tabela_expandida[i].find_all('td')[6].text
        saldo_gols = tabela_expandida[i].find_all('td')[7].text
        cartoes_amarelos = tabela_expandida[i].find_all('td')[8].text
        cartoes_vermelhos = tabela_expandida[i].find_all('td')[9].text
        aproveitamento = tabela_expandida[i].find_all('td')[10].text
        img = tabela_expandida[i].find('td').find('img')['src']

        tabela = {
            'ano': ano,
            'posicao' : posicao,
            'clube': clube,
            'pontos': pontos,
            'jogos': jogos,
            'vitorias': vitorias,
            'empates': empates,
            'derrotas': derrotas,
            'gols_pro': gols_pro,
            'gols_contra': gols_contra,
            'saldo_gols': saldo_gols,
            'cartoes_amarelos': cartoes_amarelos,
            'cartoes_vermelhos': cartoes_vermelhos,
            'aproveitamento': aproveitamento,
            'img': img
        }

        list_dados.append(tabela)

# Nome do arquivo onde o JSON será salvo
nome_arquivo = "campeonato_brasileiro.json"

# Convertendo a lista de dicionários para JSON
json_resultante = json.dumps(list_dados, ensure_ascii=False)

# Escrevendo o JSON resultante em um arquivo
with open(nome_arquivo, mode='w', encoding='utf-8') as arquivo_json:
    arquivo_json.write(json_resultante)

print("JSON salvo com sucesso no arquivo:", nome_arquivo)