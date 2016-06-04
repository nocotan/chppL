# -*- coding: utf-8 -*-
"""chppL.
package management system for C/C++
"""
import os
from bottle import get
from bottle import request
from bottle import route
from bottle import run
from bottle import static_file
from bottle import template


@route('/css/<filename>')
def css_static(filename):
    return static_file(filename, root='./views/css')


@route('/fonts/<filename>')
def fonts_static(filename):
    return static_file(filename, root='./views/fonts')


@route('/js/<filename>')
def js_static(filename):
    return static_file(filename, root='./views/js')


@route('/')
def index():
    return template('index')


@get('/register')
def register():
    return template('register')


@route('/result')
def do_register():
    return (str(request.params.get("url")))


@route('/search')
def search():
    return template('search')


@route('/contact')
def contact():
    return template('contact')


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)),
    debug=True, reloader=True)
