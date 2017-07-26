#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
import database as db

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!"

if __name__ == '__main__':
    db.init_db()
    app.run()