#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful import Resource

parking_info_list = ["test"]

class ParkingInfoListAPI(Resource):
    def get(self):
        return "Parking List API"

class ParkingInfoListSearchAPI(Resource):
    def get(self, param):
        return "Parking List Search API"

class ParkingInfoAPI(Resource):
    def get(self, parking_info_id):
        print(parking_info_id)
        return parking_info_list[parking_info_id]

    def put(self, parking_info_id):
        return parking_info_list[parking_info_id]