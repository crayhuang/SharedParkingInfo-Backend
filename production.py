#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from services import ParkingInfoListAPI, ParkingInfoListSearchAPI, ParkingInfoAPI, UserInfoAPI
import database
from models import ParkingInfo
from OpenSSL import SSL

import os

# context = SSL.Context(SSL.TLSv1_2_METHOD)
# cer = os.path.join(os.path.dirname(__file__), 'resources/gxtingche.com.crt')
# key = os.path.join(os.path.dirname(__file__), 'resources/gxtingche.com.key')

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
api = Api(app)

@app.route("/")
def hello():
    return "hello world!"

api.add_resource(UserInfoAPI, '/api/v1.0/user_info')
api.add_resource(ParkingInfoListAPI, '/api/v1.0/parking_infos')
api.add_resource(ParkingInfoListSearchAPI, '/api/v1.0/parking_infos/search')
api.add_resource(ParkingInfoAPI, '/api/v1.0/parking_infos/<int:parking_info_id>')
# api.add_resource(ParkingInfoAPI, '/api/v1.0/parking_info')

if __name__ == '__main__':
    database.init_db()
    context = ('resources/gxtingche.crt', 'resources/gxtingche.key')
    app.run(host='0.0.0.0', port=443, debug=True, ssl_context=context)