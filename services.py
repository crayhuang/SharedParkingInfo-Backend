#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import jsonify
from models import User, ParkingInfo
import database
from marshmallow import Schema

session = database.db_session

class ParkingInfoListAPI(Resource):
    def get(self):
        temp = []
        result = database.engine.execute('select * from parking_info order by ACOS(SIN((23.129163 * 3.1415) / 180 ) * SIN((latitude * 3.1415) / 180 ) +COS((23.129163 * 3.1415) / 180 ) * COS((latitude * 3.1415) / 180 ) *COS((113.264435 * 3.1415) / 180 - (longitude * 3.1415) / 180 ) ) * 6380  asc')
        print(result)
        for parking_info in result:
            temp.append(ParkingInfo(parking_info).to_json())
        # for parking_info in ParkingInfo.query.all():
        #     temp.append(parking_info.to_json())
        # for parking_info in result:
        
        return jsonify(object = temp)

class ParkingInfoListSearchAPI(Resource):
    def get(self, param):
        return "Parking List Search API"

class ParkingInfoAPI(Resource):
    def get(self, parking_info_id):
        parking_info = ParkingInfo.query.get(parking_info_id)
        return jsonify(object = parking_info.to_json())

    def put(self, parking_info_id):
        return None

class nearestParkingInfoListAPI(Resource):
    def get(self, param):
        temp = []
        result = database.engine.execute('''select
                                * from parking_info order by ACOS(SIN((23.129163
                                * 3.1415) / 180 ) * SIN((latitude * 3.1415) / 180 ) +COS((23.129163
                                * 3.1415) / 180 ) * COS((latitude * 3.1415) / 180 ) *COS((113.264435
                                * 3.1415) / 180 - (longitude * 3.1415) / 180 ) ) * 6380  asc''')
        return None