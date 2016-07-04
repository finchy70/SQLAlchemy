from databases import User
import sqlalchemy
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import datetime
from gui import Time
import wx


def _pydate2wxdate(date):
    import datetime
    assert isinstance(date, (datetime.datetime, datetime.date))
    tt = date.timetuple()
    dmy = (tt[2], tt[1]-1, tt[0])
    return wx.DateTimeFromDMY(*dmy)

def _wxdate2pydate(date):
    import datetime
    assert isinstance(date, wx.DateTime)
    if date.IsValid():
        ymd = map(int, date.FormatISODate().split('-'))
        return datetime.date(*ymd)
    else:
        return None


engine= create_engine('sqlite:///database.db', echo=True)
Session = sessionmaker()
Session.configure(bind = engine)
session = Session()
"""
date_change = session.query(User).filter_by(name = 'wendy').first()
print "before %s" % date_change.sign_up
date_change.sign_up = datetime.datetime.strptime('2030-04-04', '%Y-%m-%d')
session.commit()
"""
engine= create_engine('sqlite:///database.db', echo=True)
Session = sessionmaker()
Session.configure(bind = engine)
session = Session()
date_change1 = session.query(User).filter_by(name = 'wendy').first()
print "after %s" % date_change1.sign_up


class TimeTest(Time):
    def __init__(self, parent):
        Time.__init__(self, parent)
        engine = create_engine('sqlite:///database.db', echo=True)
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        date_change = session.query(User).filter_by(name='wendy').first()
        self.m_datePicker1.SetValue(_pydate2wxdate(date_change.sign_up))

    """
        new_time = _wxdate2pydate(self.m_datePicker1.GetValue())
        print "New Time =%s." % new_time
        print type(new_time)
        engine = create_engine('sqlite:///database.db', echo=True)
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        date_change = session.query(User).filter_by(name='wendy').first()
        date_change.sign_up = new_time
        session.commit()
"""





if __name__ == '__main__':
    app = wx.App(0)
    frame = TimeTest(None)
    frame.Centre()
    frame.Show()
    app.MainLoop()