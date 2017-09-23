#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Numeric, Integer, Text
from database import Base

class UserInfo(Base):
	__tablename__ = 'user_info'
	id = Column(Integer, primary_key=True)
	nick_name = Column(String(100))
	open_id = Column(Text)
	avatar_url = Column(Text)
	gender = Column(Integer)
	province = Column(String(100))
	city = Column(String(100))
	country = Column(String(100))
	def __init__(self, nick_name=None, open_id=None, avatar_url=None, gender=0, 
				province=None, city=None, country=None):
		self.nick_name = nick_name
		self.open_id = open_id
		self.avatar_url = avatar_url
		self.gender = gender
		self.province = province
		self.city = city
		self.country = country

	def to_json(self):
		return {
			'id': self.id,
			'nick_name': self.nick_name,
			'open_id': self.open_id,
			'avatar_url': self.avatar_url,
			'gender': self.gender,
			'province': self.province,
			'city': self.city,
			'country': self.country
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