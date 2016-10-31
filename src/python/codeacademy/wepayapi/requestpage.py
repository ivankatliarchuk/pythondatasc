import urllib3 as url
import requests

http = url.PoolManager()
r = http.request('GET', 'http://httpbin.org/robots.txt')


http = url.PoolManager()
request = http.request('GET', 'http://placekitten.com/')
html = request.read()

print(('Response body {}.').format(html))
print(('Response header {}.').format(request.headers))
print(html[559:1000])
from bs4 import BeautifulSoup
#soup = BeautifulSoup(html, 'text/html')

reg = requests.request('GET', 'http://placekitten.com/')
kittens = reg.content()
print(BeautifulSoup(reg.content, 'text/html'))


