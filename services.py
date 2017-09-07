#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import jsonify
from models import ParkingInfo
import database
from sqlalchemy.sql import text 
from flask import request

session = database.db_session

class ParkingInfoListAPI(Resource):
    def get(self):
        cur_latitude = request.args.get('cur_latitude')
        cur_longitude = request.args.get('cur_longitude')
        temp = []
        sql = text('select * from parking_info order by ACOS(SIN((:latitude * 3.1415) / 180 ) * SIN((:latitude * 3.1415) / 180 ) + COS((:latitude * 3.1415) / 180 ) * COS((latitude * 3.1415) / 180 ) * COS((:longitude * 3.1415) / 180 - (:longitude * 3.1415) / 180 ) ) * 6380  asc limit 500')
        result = database.engine.execute(sql, latitude = cur_latitude, longitude = cur_longitude)
        print(result)
        for item in result:
            pi = convert2parking_info(item)
            temp.append(pi.to_json())
        
        return jsonify(object = temp)

    def post(self):
        print(request.json)
        # parking_info = ParkingInfo(province=request.province, city=request.city, district=request.district, fee=request.fee)
        params = request.json
        parking_info = ParkingInfo(province=params.get('province'), city=params.get('city'), district=params.get('district'), 
        fee=params.get('fee'), address=params.get('address'))
        session.add(parking_info)
        session.commit()
        return "Posting" 


class ParkingInfoListSearchAPI(Resource):
    def get(self):
        return "Parking List Search API"


class ParkingInfoAPI(Resource):
    def get(self, parking_info_id):
        parking_info = ParkingInfo.query.get(parking_info_id)
        return jsonify(object = parking_info.to_json())


def convert2parking_info(item):
    pi = ParkingInfo()
    pi.id = item['id']
    pi.address = item['address']
    pi.city = item['city']
    pi.description = item['description']
    pi.district = item['district']
    pi.fee = item['fee']
    pi.latitude = str(item['latitude'])
    pi.longitude = str(item['longitude'])
    pi.name = item['name']
    pi.opening_time = item['opening_time']
    pi.province = item['province']
    pi.remark = item['remark']
    pi.telephone = item['telephone'] 
    return pi