#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from services import ParkingInfoListAPI, ParkingInfoListSearchAPI, ParkingInfoAPI
import database
from models import ParkingInfo

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello():
    return "hello world!"

api.add_resource(ParkingInfoListAPI, '/api/v1.0/parking_infos')
api.add_resource(ParkingInfoListSearchAPI, '/api/v1.0/parking_infos/search/<string:param>')
api.add_resource(ParkingInfoAPI, '/api/v1.0/parking_infos/<int:parking_info_id>')

# def init_data():
#     for x in range(4):
#         parking_info = ParkingInfo("Name: " + str(x), "Description: " + str(x),
#         "Province: " + str(x), "City: " + str(x), "Disctrict: " + str(x),
#          "Address: " + str(x), 0.0, 0.0, "fee: " + str(x), "remark: " + str(x), 
#          "opening_time: " + str(x))
#         database.db_session.add(parking_info)    

#     database.db_session.commit()

if __name__ == '__main__':
    database.init_db()
    app.run(debug=True)

