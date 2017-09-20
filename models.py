#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Numeric, Integer, Text
from database import Base

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	nickname = Column(String(100))
	open_id = Column(Text)
	def __init__(self, nickename=None, open_id=None):
		self.nickname = nickename
		self.open_id = open_id

	def to_json(self):
		return {
			'id': self.id,
			'nickname': self.nickname,
			'open_id': self.open_id
		}


class ParkingInfo(Base):
	__tablename__ = 'parking_info'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(Text)
	description = Column(Text)
	province = Column(String(20))
	city = Column(String(20))
	district = Column(String(20))
	address = Column(Text)
	longitude = Column(Numeric(16, 10))
	latitude = Column(Numeric(16, 10))
	fee = Column(Text)
	remark = Column(Text)
	opening_time = Column(Text)
	telephone = Column(String(100))
	status = Column(String(50))

	def __init__(self, name=None, description=None, province=None, city=None, district=None, address=None, longitude=0.0, latitude=0.0, 
				fee=None, remark=None, opening_time=None, telephone=None, status='PENDING'):
		self.name = name
		self.description = description
		self.province = province
		self.city = city
		self.district = district
		self.address = address
		self.longitude = longitude
		self.latitude = latitude
		self.fee = fee
		self.remark = remark
		self.opening_time = opening_time
		self.telephone = telephone
		self.status = status
		
	
	def to_json(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'provice': self.province,
			'city': self.city,
			'district': self.district,
			'address': self.address,
			'longitude': str(self.longitude),
			'latitude': str(self.latitude),
			'fee': self.fee,
			'remark': self.remark,
			'opening_time': self.opening_time,
			'telephone': self.telephone,
			'status': self.status
		}