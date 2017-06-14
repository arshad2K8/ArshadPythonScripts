__author__ = 'arshad'
import requests
#http://docs.python-requests.org/en/master/user/quickstart/
r = requests.get('https://api.github.com/events')
respGoogle = requests.get('https://www.google.com/')
#print r.text
print respGoogle.text

#respPostReq = requests.post('http://httpbin.org/post', data = {'key':'value'})
respPut = requests.put('http://httpbin.org/put', data = {'key':'value'})
respDelete = requests.delete('http://httpbin.org/delete')
respHead = requests.head('http://httpbin.org/get')
respOptions = requests.options('http://httpbin.org/get')

# check the encodinq of reponse by r.encoding r.text converts repsonse text to a particular encoding automatically
# 1. use r.content to find out encoding , 2. then set r.encoding ---> call 3. r.text uses correct encoding for conversion
# 2. if used your own encoding , pass the codecs module tp r.encoding
# 3. if response  r.content is binary then use