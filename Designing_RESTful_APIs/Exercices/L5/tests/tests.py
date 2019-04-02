import os
import sys
import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append('../')

from app import app, login_manager
from models import User, Base

class TestCase(unittest.TestCase):
    clean_up = True
    db_name = 'test.db'
    db_url = 'sqlite:///' + os.path.join(os.getcwd(), db_name)
    engine = create_engine(db_url)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    app = []
    def setUp(self):
        app.config['TESTING'] = True
        app.secret_key="Something"
        app.config['QLALCHEMY_DATABASE_URI'] = self.db_url
        self.app = app.test_client()
        login_manager.init_app(app)
        login_manager.login_view = 'login_api.login'
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        if self.clean_up:
            Base.metadata.drop_all(self.engine)
            os.remove(self.db_name)

    def does_url_response_contain_substring(self ,url, sub_string):
        response = self.app.get(url, follow_redirects=True)
        self.assertEqual(response.status_code,200)

        data = str(response.data)
        if sub_string is not str:
            sub_string = str(sub_string)
        if sub_string in data:
            return
        else:
            self.assertTrue(False)

    def test_get_login_route(self):
        self.does_url_response_contain_substring( '/login', r'<title>Login</title>')

    def test_get_index_page(self):
        self.does_url_response_contain_substring( '/', r'<title>Meet\'N eat</title>')

    def test_get_apiKey_page_whitout_logged_in_user(self):
        self.does_url_response_contain_substring( '/apiKey', r'<title>Login</title>')

    def test_get_logout_page_whitout_logged_in_user(self):
        self.does_url_response_contain_substring( '/logout', r'<title>Login</title>')


if __name__ == '__main__':
    unittest.main()
    #SQLalchemy tutorial https://stackoverflow.com/questions/14719507/unit-tests-for-query-in-sqlalchemy
    #Flask tutorial https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-unit-testing-legacy
