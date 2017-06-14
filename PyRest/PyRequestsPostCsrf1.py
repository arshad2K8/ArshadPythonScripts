__author__ = 'arshad'
import sys
import requests
from lxml import html

URL = 'https://portal.bitcasa.com/login'
login_url = 'http://arsh2k7.pythonanywhere.com/accounts/login/'


session_requests = requests.session()
result = session_requests.get(login_url)
tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]
print 'authenticity_token', authenticity_token
username = 'arshad'
password = 'Nishad@123'

payload =  {'username':username, 'password':password,
            'csrfmiddlewaretoken':authenticity_token
           }

login = session_requests.post(login_url, data=payload) #this should log in in, i don't have an account there to test.
payloadAddCat = {'id_name' : 'sampleCategory2', 'csrfmiddlewaretoken':authenticity_token}
urlAddCat = 'http://arsh2k7.pythonanywhere.com/rango/add_category/'
r = session_requests.post(urlAddCat, data=payloadAddCat) #unless you need to set a user agent or r

print 'response ', r.content