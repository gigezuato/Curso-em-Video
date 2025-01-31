import urllib.request
import urllib.error

'''
 método.read()
 biblioteca requests
 '''

site = 'https://www.instagram.com/#'
try:
    resposta = urllib.request.urlopen(site)
except urllib.error.URLError as e:
    print(f'Essa url não está acessível. Erro: {e}')
else:
    print('A url está acessível!')