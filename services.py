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
        for parking_info in ParkingInfo.query.all():
            temp.append(parking_info.to_json())
        
        return jsonify(object = temp)

class ParkingInfoListSearchAPI(Resource):
    def get(self, param):
        return "Parking List Search API"

class ParkingInfoAPI(Resource):
    def get(self, parking_info_id):
        # return session.query(ParkingInfo).filter(User.id = parking_info_id)
        return None

    def put(self, parking_info_id):
        return parking_info_list[parking_info_id]