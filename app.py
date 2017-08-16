#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from services import ParkingInfoListAPI, ParkingInfoListSearchAPI, ParkingInfoAPI
import database
from models import ParkingInfo

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
api = Api(app)

@app.route("/")
def hello():
    return "hello world!"

api.add_resource(ParkingInfoListAPI, '/api/v1.0/parking_infos')
api.add_resource(ParkingInfoListSearchAPI, '/api/v1.0/parking_infos/search/<string:param>')
api.add_resource(ParkingInfoAPI, '/api/v1.0/parking_infos/<int:parking_info_id>')

if __name__ == '__main__':
    database.init_db()
    app.run(debug=True)