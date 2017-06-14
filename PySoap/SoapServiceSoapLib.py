__author__ = 'arshad'
import soaplib
from soaplib.core.service import rpc, DefinitionBase, soap
from soaplib.core.model.primitive import String, Integer
from soaplib.core.server import wsgi
from soaplib.core.model.clazz import Array



class HelloWorldService(DefinitionBase):
    @soap(String,_returns=String)
    def say_hello(self,name):
        results = []
        return "Hello World JAX-WS "+name

if __name__=='__main__':
    try:
        from wsgiref.simple_server import make_server
        soap_application = soaplib.core.Application([HelloWorldService], 'tns')
        wsgi_application = wsgi.Application(soap_application)
        server = make_server('localhost', 9999, wsgi_application)
        server.serve_forever()
    except ImportError:
        print "Error: example server code requires Python >= 2.5"