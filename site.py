import os, os.path
import random
import string

import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        f = open('index.html')
        indx = f.read()
        f.close
        return indx

    @cherrypy.expose
    def science(self):
        f = open('science.html')
        indx = f.read()
        f.close
        return indx

    @cherrypy.expose
    def generate(self, length=8):
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        cherrypy.session['mystring'] = some_string
        return some_string

if __name__ == '__main__':
     conf = {
         '/': {
             'tools.sessions.on': True,
             'tools.staticdir.root': os.path.abspath(os.getcwd())
         },
         '/static': {
             'tools.staticdir.on': True,
             'tools.staticdir.dir': './public'
         }
     }
     cherrypy.quickstart(StringGenerator(), '/', conf)