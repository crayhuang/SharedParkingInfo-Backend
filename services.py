#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import jsonify
from models import ParkingInfo, UserInfo, Feedback
import database
from sqlalchemy.sql import text 
from flask import request
import auth

session = database.db_session

class UserInfoAPI(Resource):
    def post(self):
        params = request.json
        print(params)
        # auth.check_sign_api(params)
        user_info = UserInfo(open_id=params.get('open_id'), nick_name=params.get('nick_name'), avatar_url=params.get('avatar_url'), gender=params.get('gender'), 
                            province=params.get('province'), city=params.get('city'), country=params.get('country'))

        session.add(user_info)
        session.commit()
        session.close()

        return "User Info"

class ParkingInfoListAPI(Resource):
    def get(self):
        # Signature Validation
        auth.check_sign_api(request.args)
        cur_latitude = request.args.get('latitude')
        cur_longitude = request.args.get('longitude')
        temp = []
        sql = text('select * from parking_info where status = %s order by ACOS(SIN((:latitude * 3.1415) / 180 ) * SIN((latitude * 3.1415) / 180 ) + COS((latitude * 3.1415) / 180 ) * COS((:latitude * 3.1415) / 180 ) * COS((longitude * 3.1415) / 180 - (:longitude * 3.1415) / 180 ) ) * 6380 asc limit 500' % "'APPROVED'")
        # sql = text('select * from parking_info order by (POWER(MOD(ABS(longitude-:longitude),360),2) + POWER(ABS(latitude-:latitude),2)) asc limit 500')
        print(sql)
        result = database.engine.execute(sql, latitude = cur_latitude, longitude = cur_longitude)
        
        for item in result:
            parking_info = convert2parking_info(item)
            temp.append(parking_info.to_json())
        
        return jsonify(object = temp)

    def post(self):
        print(request.json)

        # parking_info = ParkingInfo(province=request.province, city=request.city, district=request.district, fee=request.fee)
        params = request.json
        auth.check_sign_api(params)
        parking_info = ParkingInfo(name=params.get('name'), province=params.get('province'), city=params.get('city'), 
        district=params.get('district'), fee=params.get('fee'), address=params.get('address'), description=params.get('description'))
        session.add(parking_info)
        session.commit()
        session.close()
        return "Posted" 


class ParkingInfoListSearchAPI(Resource):
    def get(self):
        keyword = request.args.get('keyword')
        like_keyword = '%' + keyword + '%'
        temp = []
        result = ParkingInfo.query.filter(ParkingInfo.status == 'APPROVED').filter(ParkingInfo.name.like(like_keyword) | ParkingInfo.description.like(like_keyword)).all()
        for item in result:
            print(item.id)
            parking_info = convert2parking_info(item)
            temp.append(parking_info.to_json())

        return jsonify(object = temp)


class ParkingInfoAPI(Resource):
    def get(self, parking_info_id):
        auth.check_sign_api(request.args)
        
        parking_info = ParkingInfo.query.get(parking_info_id)

        return jsonify(object = parking_info.to_json())


class FeedbackAPI(Resource):
    def post(self):
        params = request.json
        print(params)
        auth.check_sign_api(params)
        feedback = Feedback(parking_info_id=params.get('parking_info_id'), feedback_content=params.get('feedback_content'))
        session.add(feedback)
        session.commit()
        session.close()
        return "Posted"

def convert2parking_info(item):
    pi = ParkingInfo()

    pi.id = item.id
    pi.address = item.address
    pi.city = item.city
    pi.description = item.description
    pi.district = item.district
    pi.fee = item.fee
    pi.latitude = str(item.latitude)
    pi.longitude = str(item.longitude)
    pi.name = item.name
    pi.opening_time = item.opening_time
    pi.province = item.province
    pi.remark = item.remark
    pi.telephone = item.telephone
    pi.status = item.status

    return pi