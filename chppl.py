# -*- coding: utf-8 -*-
"""chppL.
package management system for C/C++
"""
import os
from bottle import route
from bottle import run


@route("/")
def chppl():
    return "Test"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
