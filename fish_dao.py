# pip install numpy
# pip install pandas
# python -m pip install

# mariadb 연결하는법 - sqlalchemy
# https://mariadb.com/ko/resources/blog/using-sqlalchemy-with-mariadb-connector-python-part-1/

# pandas 라이브러리로 insert, select 하는법(sqlalchemy의 engine(connection) 필요)
# https://ayoteralab.tistory.com/entry/AT-09-mariadbmysql-connection-with-python-2

# session 객체 만들어서 orm 사용하는법(파이썬 클래스로 질의)
# https://docs.sqlalchemy.org/en/14/orm/tutorial.html#creating-a-session

# 이스케이프 특수문자
# https://freedeveloper.tistory.com/191
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import sqlalchemy as db
from data.fish_api import gettestData, gettrainData
from sqlalchemy.orm import sessionmaker

# dict 타입으로 insert하고 dict 타입으로 select하는게 가장 편하다. - pymysql 라이브러리(mysql, mariadb)

# DataFrame도 DB에 insert하고 select가능하다 - SQLAlchemy(ORM)
# class 타입으로도 insert하고 select하는게 가능하다

# mariadb://127.0.0.1:3306/pythondb?usernme=python&password=python1234
engine = db.create_engine(
    "mariadb+mariadbconnector://python:python1234@127.0.0.1:3306/pythondb")


def traininsert():
    trains = gettrainData()
    trains.to_sql("train", engine, index=False, if_exists="replace")


def testinsert():
    tests = gettestData()
    tests.to_sql("test", engine, index=False, if_exists="replace")


def trainselect():
    traindf = pd.read_sql("select * from train", con=engine)
    print(traindf)


def testselect():
    testdf = pd.read_sql("select * from test", con=engine)
    print(testdf)

# traininsert()
# testinsert()


trainselect()
testselect()
