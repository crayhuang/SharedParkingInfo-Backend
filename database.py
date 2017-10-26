from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('sqlite:////sqlite/test.db', convert_unicode=True)
# engine = create_engine('mysql://root:my-secret-pw@127.0.0.1:32768/SPI?charset=utf8mb4', convert_unicode=True, pool_recycle=3600)
engine = create_engine('mysql://SPIUser:q+ddHJ4kuCdk@tdsql-jvxc74c5.sql.tencentcdb.com:39/spi?charset=utf8mb4', convert_unicode=True, pool_recycle=3600)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)
