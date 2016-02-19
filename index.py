#!/usr/bin/python
# -*- coding: utf-8 -*-

import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

testik = cherrypy.sessio

test = HelloWorld()

if __name__ == '__main__':
   cherrypy.quickstart(HelloWorld())
