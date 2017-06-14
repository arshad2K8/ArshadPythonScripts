__author__ = 'arshad'
import urllib2, urllib, requests
from lxml import html
import re
#issuing GET requests

# isuing a post request
username = 'arshad'
password = 'Nishad@123'

#create a sessions objects
session_requests = requests.session()
login_url = 'http://arsh2k7.pythonanywhere.com/accounts/login/'
result = session_requests.get(login_url)

#print 'First Response is ', result.content

tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]
print 'authenticity_token',authenticity_token
payload =  {'username':username, 'password':password,
            'csrfmiddlewaretoken':authenticity_token
           }
postLoginresult = session_requests.post(login_url, data = payload, headers = dict(referer=login_url))
#print 'postLoginresult cokies',postLoginresult.content

afterLoginCookies = postLoginresult.cookies
# after login
urlAddCat = 'http://arsh2k7.pythonanywhere.com/rango/add_category/'
result = session_requests.get(urlAddCat)
#print 'First Response is ', result.content
tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]
print 'authenticity_token',authenticity_token


payloadAddCat = {'name' : 'Shadalooooooo4553', 'csrfmiddlewaretoken':authenticity_token,
                 'views':'0','likes':'0' , 'slug':'Shadalooooooo4552'
                }
resultAddCat = session_requests.post(urlAddCat, data = payloadAddCat, headers = dict(referer=urlAddCat))

#print 'resultAddCat', resultAddCat.content