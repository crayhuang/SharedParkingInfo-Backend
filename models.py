#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Float, Integer
from database import Base

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	name = Column(String(100), unique=True)
	def __init__(self, name=None):
		self.name = name



class ParkingInfo(Base):
	__tablename__ = 'parking_info'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(500))
	description = Column(String(2000))
	address = Column(String(2000))
	longitude = Column(Float)
	latitude = Column(Float)
	fee = Column(String(100))
	remark = Column(String(2000))
	opening_time = Column(String(200))

	def __init__(self, name=None, description=None, address=None, longitude=0.0, latitude=0.0, fee=None, remark=None, opening_time=None):
		self.name = name
		self.description = description
		self.address = address
		self.longitude = longitude
		self.latitude = latitude
		self.fee = fee
		self.remark = remark
		self.opening_time = opening_time
