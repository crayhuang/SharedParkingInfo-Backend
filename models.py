#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, BigInteger, String, Float
from database import Base

class User(Base):
	__tablename__ = 'users'
	id = Column(BigInteger, primary_key=True)
	name = Column(String(100), unique=True)

	def __init__(self, name=None):
		self.name = name
	

class ParkingInfo(Base):
	__tablename__ = 'parking_info'
	id = Column(BigInteger, primary_key=True)
	name = Column(String(500))
	description = Column(String(2000))
	longitude = Column(Float)
	latitude = Column(Float)
