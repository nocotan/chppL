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
from bottle import TEMPLATE_PATH
from bottle import url


VIEWS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'views'))

TEMPLATE_PATH.insert(0, VIEWS_PATH)


@route('/css/:path#.+#', name='static/css')
def css_static(path):
    return static_file(path, root='static/css')


@route('/fonts/<filename>')
def fonts_static(filename):
    return static_file(filename, root='static/fonts')


@route('/js/<filename>')
def js_static(filename):
    return static_file(filename, root='static/js')


@route('/')
def index():
    return template('index', get_url=url)


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


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
