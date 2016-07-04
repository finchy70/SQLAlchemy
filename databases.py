import sqlalchemy
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import datetime

engine = create_engine('sqlite:///database.db', echo=False)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)
    sign_up = Column(sqlalchemy.DATETIME)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)
"""
Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
session.add_all([User(name='wendy', fullname='Wendy Williams', password='foobar', sign_up=datetime.datetime.now()),
                 User(name='mary', fullname='Mary Contrary', password='xxg527', sign_up=datetime.datetime.now()),
                 User(name='fred', fullname='Fred Flinstone', password='blah', sign_up=datetime.datetime.now())])
session.commit()


#ed_user.password = 'f8s7ccs'

#session.dirty

#session.commit()

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname, instance.password)



updater = session.query(User).filter_by(name='wendy').first()
print('Updater= {}').format(updater)
updater.password='it_works123'
session.commit()

for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname, instance.password)


Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

updater = session.query(User).filter_by(name='ed').first()
updater.name='edward'
session.commit()
"""