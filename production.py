#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from services import ParkingInfoListAPI, ParkingInfoListSearchAPI, ParkingInfoAPI, UserInfoAPI,FeedbackAPI
import database

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
api.add_resource(FeedbackAPI, '/api/v1.0/feedback')
# api.add_resource(ParkingInfoAPI, '/api/v1.0/parking_info')

if __name__ == '__main__':
    database.init_db()
    context = ('resources/gxtingche.com.crt', 'resources/gxtingche.com.key')
    app.run(host='0.0.0.0', port=443, debug=True, ssl_context=context, threaded=True)