import requests

url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
response = requests.get(url)

cotacoes = response.json()
#print(cotacoes)

dolar = round(float(cotacoes['USDBRL']['high']), 2)
euro = round(float(cotacoes['EURBRL']['high']), 2)
btc = cotacoes['BTCBRL']['high']

with open('cotacao.txt', 'w') as file:
  file.write('Tabela de cotação de moedas em tempo real - AwesomeAPI' + '\n\n')
  file.write(f"1 Dólar = {str(dolar)} R$\n")
  file.write(f"1 Euro = {str(euro)} R$\n")
  file.write(f"1 BTC = {str(btc)} R$\n")