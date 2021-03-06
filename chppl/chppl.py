# -*- coding: utf-8 -*-
"""chppL.
package management system for C/C++
created by @nocotan
"""
import os
from bottle import get
from bottle import jinja2_template as template
from bottle import request
from bottle import route
from bottle import run
from bottle import static_file
from bottle import TEMPLATE_PATH

from chppl_data import ChpplData
from chppl_result import ChpplResult
from chppl_search import ChpplSearch


VIEWS = os.path.abspath(os.path.join(os.path.dirname(__file__), 'views'))
STATIC = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static'))


TEMPLATE_PATH.insert(0, VIEWS)
TEMPLATE_PATH.insert(0, STATIC)


@route('/static/<filename:path>')
def static(filename):
    """static file path"""
    return static_file(filename, root=STATIC)


@route('/')
def index():
    """index page"""
    return template('index')


@get('/register')
def register():
    """register page"""
    return template('register')


@route('/result')
def do_register():
    """do register
    @param: url
    @param: name
    @param: description
    @param: creator
    """

    data = ChpplData()
    data.set_url(str(request.params.get("url")))
    data.set_name(str(request.params.get("name")))
    data.set_description(str(request.params.get("description")))
    data.set_creator(str(request.params.get("creator")))

    result = ChpplResult()
    result.set_data(data)

    if result.check_data() is "Success":
        result.execute_query("insert")

    msg_list = result.get_msg_list()

    return template('result', result=result.check_data(), msg_list=msg_list)


@route('/search')
def search():
    """search page
    @return: search_list
    """
    search = ChpplSearch()
    search.search_all()
    search_list = search.get_search_list()
    return template('search', search_list=search_list)


@route('/manage')
def manage():
    """manage page"""
    return template('manage')


@route('/manage_result')
def to_delete():
    """do delete
    @param: package
    @param: confilm
    """

    data = ChpplData()
    data.set_package(str(request.params.get('package')))
    data.set_confilm(str(request.params.get('confilm')))

    result = ChpplResult()
    result.set_data(data)

    if result.confilm_data() is "Success":
        result.execute_query("delete")

    msg_list = result.get_msg_list()

    return template('result', result=result.confilm_data(), msg_list=msg_list)


@route('/contact')
def contact():
    """contact page"""
    return template('contact')


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
