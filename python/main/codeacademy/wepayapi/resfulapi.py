import urllib3 as urllib

url = 'http://placekitten.com/200/300'
http = urllib.PoolManager()
response = http.request('GET', url, preload_content = False) # stream the response.
# print(('Response header {}.').format(response.headers))
# kittens = response.data
#
# with open('kitten.jpg') as fp:
#     file_data = fp.read()

file = open('file.jpg', 'w')
for chunk in response.stream(32):
    file.write(bytearray(chunk))
file.close()
response.release_conn()


