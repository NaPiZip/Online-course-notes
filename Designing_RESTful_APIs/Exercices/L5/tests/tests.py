import os
import sys
import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append('../')

from app import app
from models import User, Base

class TestCase(unittest.TestCase):
    clean_up = True
    db_name = 'test.db'
    db_url = 'sqlite:///' + os.path.join(os.getcwd(), db_name)
    engine = create_engine(db_url)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    def setUp(self):
        app.config['TESTING'] = True
        app.config['QLALCHEMY_DATABASE_URI'] = self.db_url
        self.app = app.test_client()
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        if self.clean_up:
            Base.metadata.drop_all(self.engine)
            #os.remove(self.db_name)

    def test_get_login_route(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code,200)
        print(response.is_json)



if __name__ == '__main__':
    unittest.main()
    #SQLalchemy tutorial https://stackoverflow.com/questions/14719507/unit-tests-for-query-in-sqlalchemy
    #Flask tutorial https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-unit-testing-legacy
