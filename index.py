#!/usr/bin/python
# -*- coding: utf-8 -*-

import cherrypy
from tinydb import TinyDB, where

db = TinyDB('/home/klerik/Downloads/muj_blog/db.json')

kategorie = db.table('kategorie')
zapisky=db.table('zapisky')

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return str(zapisky.all())

if __name__ == '__main__':
   cherrypy.quickstart(HelloWorld())