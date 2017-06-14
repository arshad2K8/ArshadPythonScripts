__author__ = 'arshad'
import urllib2, urllib, requests
from lxml import html

#issuing GET requests

url = 'http://arsh2k7.pythonanywhere.com/rango/'
response = urllib2.urlopen(url).read()
#Errors are reported as exceptions (urllib2.HTTPError or urllib2.URLError).
#print response

# isuing a post request

urlPost = 'http://arsh2k7.pythonanywhere.com/rango/add_category/'
username = 'arshad'
password = 'Nishad@123'
csrfToken = 'ogAXuOVdSQkpPGHzoF7lmVKQ1Cvi05tV'
params = urllib.urlencode(
    {'username':username,
     'password':password,
     'csrfmiddlewaretoken':csrfToken
    })
#responsePost = urllib2.urlopen(urlPost, params).read()


#create a sessions objects
session_requests = requests.session()
login_url = 'http://arsh2k7.pythonanywhere.com/accounts/login/'
result = session_requests.get(login_url)
tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]
print authenticity_token
payload =  {'username':username, 'password':password,
            'csrfmiddlewaretoken':authenticity_token
           }
postLoginresult = session_requests.post(login_url, data = payload, headers = dict(referer=login_url))
print 'postLoginresult ',postLoginresult

# after login
urlAddCat = 'http://arsh2k7.pythonanywhere.com/rango/add_category/'
payloadAddCat = {'id_name' : 'sampleCategory2', 'csrfmiddlewaretoken':authenticity_token}
resultAddCat = session_requests.post(urlAddCat, data = payloadAddCat, headers = dict(referer=urlAddCat))

print 'resultAddCat', resultAddCat.history