__author__ = 'arshad'
from suds.client import Client
url_service = 'http://localhost:9999/ws/hello?wsdl'
client = Client(url_service)
list_of_methods = [method for method in client.wsdl.services[0].ports[0].methods]

response = client.service.getHelloWorldAsString("France")
print response