import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']

print('Dados do Ip Externo\n')
print('IP: {4}\n Região: {1}\nPais: {2}\nCidade: {3}\nOrg.{0}'.format(org,regiao,pais,cid,ip))