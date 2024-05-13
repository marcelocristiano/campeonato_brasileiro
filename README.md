# Web Scraping de Dados do Campeonato Brasileiro Série A

Este script em Python realiza o web scraping dos dados do Campeonato Brasileiro Série A a partir do site da Confederação Brasileira de Futebol (CBF). Ele extrai informações como posição na tabela, clube, pontos, jogos, vitórias, empates, derrotas, gols pró, gols contra, saldo de gols, cartões amarelos, cartões vermelhos e aproveitamento de cada equipe em cada ano desde 2012 até o ano atual.

## Bibliotecas Utilizadas

- **requests**: Para fazer requisições HTTP ao site da CBF.
- **BeautifulSoup**: Para fazer o parsing do HTML e extrair os dados desejados.
- **datetime**: Para obter o ano atual automaticamente.
- **time**: Para pausar a execução do script entre requisições, evitando sobrecarga no servidor.
- **json**: Para salvar os dados em formato JSON.

## Funcionamento

1. O script começa definindo uma lista vazia chamada `list_dados` para armazenar os dados extraídos.
2. Ele define o ano inicial como 2012 e o ano atual obtido automaticamente.
3. Em um loop que percorre os anos de 2012 até o ano atual, ele constrói a URL correspondente ao ano atual e faz uma requisição HTTP para obter o conteúdo da página.
4. Utilizando o BeautifulSoup, o script analisa o HTML da página em busca da tabela de classificação do campeonato.
5. Se a tabela estiver expandida (com detalhes de cada equipe visíveis), ele a captura. Caso contrário, ele captura a tabela normal.
6. Para cada equipe na tabela, ele extrai os dados relevantes (posição, clube, pontos, etc.) e os armazena em um dicionário.
7. Cada dicionário é adicionado à lista `list_dados`.
8. Ao final do loop, os dados são convertidos para o formato JSON e salvos em um arquivo com o nome "campeonato_brasileiro.json".

## Execução

Para executar o script, basta copiar e colar o código em um ambiente Python adequado e garantir que as bibliotecas necessárias estejam instaladas (`requests`, `BeautifulSoup`, etc.). Após a execução, um arquivo JSON contendo os dados será criado no mesmo diretório do script.

## Notas

- O script pausa por um curto período de tempo entre as requisições para evitar sobrecarregar o servidor da CBF.
- O código utiliza uma verificação simples para determinar se a tabela está expandida ou não. Dependendo das mudanças no site da CBF, pode ser necessário ajustar essa lógica para garantir que os dados sejam corretamente capturados.

**Observação:** Este script realiza scraping de dados de um site externo. Certifique-se de que você está autorizado a acessar e utilizar os dados de acordo com os termos de serviço do site em questão.
