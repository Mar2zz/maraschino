import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

try:
    from settings import DATABASE

except ImportError:
    print "No settings.py found. Copy settings_example.py to settings.py, edit it and try again."
    quit()

engine = create_engine('sqlite:///%s' % (DATABASE), convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import maraschino.models
    Base.metadata.create_all(bind=engine)
