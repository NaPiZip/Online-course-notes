import os
import sys
import json
import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append('../')

from app import app, login_manager
from models import User, Base
from dbSession import session as _session, engine

class TestCase(unittest.TestCase):
    clean_up    = True
    session     = _session
    app = []
    def setUp(self):
        app.config['TESTING'] = True
        app.secret_key="Something"
        self.app = app.test_client()
        login_manager.init_app(app)
        login_manager.login_view = 'login_api.login'

    def tearDown(self):
        if self.clean_up:
            self.session.query(User).delete()
            self.session.commit()
            self.session.close()

    def tearDownClass():
        os.remove('finalProject.db')

    def does_url_response_contain_substring(self ,url, sub_string):
        response = self.app.get(url, follow_redirects=True)
        self.assertEqual(response.status_code,200)
        self.assertTrue(self.does_data_contain_substring(response.data, sub_string))

    def does_data_contain_substring(self, in_data, sub_string):
        data = str(in_data)
        if sub_string is not str:
            sub_string = str(sub_string)
        if sub_string in data:
            return True
        else:
            return False

    def create_minimal_user(self, user_name, password):
        new_user = User(user_name=user_name, email='something@google.com')
        new_user.generate_api_key()
        new_user.hash_password(password)
        self.session.add(new_user)
        self.session.commit()

    def login_user(self, user, pw):
        response = self.app.post('/login', data=dict(username=user, password=pw), follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def logout_user(self):
        response = self.app.get('logout')
        self.assertEqual(response.status_code,200)

    def get_api_key_dict_of_current_user(self):
        response  = self.app.get('/apiKey')
        if response.status_code == 200 and response.is_json:
            return response.get_json()
        else:
            return None

    def test_get_login_route(self):
        self.does_url_response_contain_substring( '/login', r'<title>Login</title>')

    def test_get_index_page(self):
        self.does_url_response_contain_substring( '/', r'<title>Meet\'N eat</title>')

    def test_get_apiKey_page_whitout_logged_in_user(self):
        self.does_url_response_contain_substring( '/apiKey', r'<title>Login</title>')

    def test_get_logout_page_whitout_logged_in_user(self):
        self.does_url_response_contain_substring( '/logout', r'<title>Login</title>')

    def test_post_request_with_wrong_password(self):
        user_name = 'Nawin'
        pw = 'something'
        self.create_minimal_user(user_name,pw)
        response = self.app.post('/login', data=dict(username=user_name, password='qweq'), follow_redirects=True)
        self.assertEqual(response.status_code,200)
        self.assertTrue(self.does_data_contain_substring(response.data,r'<strong>Error!</strong> Invalid Credentials\n'))

    def test_post_request_with_correct_password(self):
        user_name = 'Nawin'
        pw = '1234'
        self.create_minimal_user(user_name, pw)
        response = self.app.post('/login', data=dict(username=user_name, password=pw), follow_redirects=True)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.is_json, True)
        self.assertNotEqual(response.get_json().get('token'),None)

    def test_token_route_v1_users_no_key(self):
        result = self.app.get('/v1/users')
        self.assertEqual(result.status_code, 401)

    def test_token_route_v1_users_false_key(self):
        result = self.app.get('/v1/users',query_string=dict(token='asda'))
        self.assertEqual(result.status_code,401)

    def test_token_route_v1_users_valid_token(self):
        self.create_minimal_user('Nawin','1234')
        self.create_minimal_user('a','abcd')
        self.create_minimal_user('b','abcd')
        self.create_minimal_user('c','abcd')
        self.login_user('Nawin','1234')

        response = self.app.get('/v1/users', query_string =self.get_api_key_dict_of_current_user())
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.is_json, True)
        self.assertEqual(len(response.get_json()),4)
        self.logout_user()

    def test_token_route_v1_users_invalid_token(self):
        response = self.app.get('/v1/users', query_string =dict(token='asdasd'))
        self.assertTrue(self.does_data_contain_substring(response.data, 'Unauthorized address trying to use'))

    def test_token_route_v1_users_valid_token_post(self):
        new_token = '1234'
        self.create_minimal_user('Nawin','1234')
        self.login_user('Nawin','1234')
        response =  self.app.put('/v1/users', query_string=self.get_api_key_dict_of_current_user(),
                                               data=json.dumps({'user_name':'Nawin','token':new_token}) ,mimetype='application/json' )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(self.does_data_contain_substring(response.data, 'Success, updated user'))
        response = self.app.get('/v1/users', query_string =self.get_api_key_dict_of_current_user())
        self.assertTrue(self.does_data_contain_substring(response.data, '\"token\":\"{}\"'.format(new_token)))
        response = self.app.get('/v1/users', query_string =dict(token=new_token))
        self.assertEqual(response.status_code,200)
        self.logout_user()

    def test_token_route_v1_users_valid_token_post_missing_user(self):
        new_token = '1234'
        self.create_minimal_user('Nawin','1234')
        self.login_user('Nawin','1234')
        response =  self.app.put('/v1/users', query_string=self.get_api_key_dict_of_current_user(),
                                               data=json.dumps({'token':new_token}) ,mimetype='application/json' )
        self.assertEqual(response.status_code, 404)
        self.logout_user()

    def test_token_route_v1_users_with_id_invalid_token(self):
        response = self.app.get('/v1/users/0')
        self.assertEqual(response.status_code, 401)

    def test_token_route_v1_users_with_id_invalid_id(self):
        user = 'Nawin'
        pw = 'Something'
        self.create_minimal_user(user, pw)
        self.login_user(user, pw)
        response = self.app.get('/v1/users/0', query_string=self.get_api_key_dict_of_current_user())
        self.assertEqual(response.status_code,404)
        self.assertTrue(self.does_data_contain_substring(response.data, "ERROR, user 0 not found!"))
        self.logout_user()

    def test_token_route_v1_users_with_id_valid_everything(self):
        user = 'Nawin'
        pw = 'Something'
        self.create_minimal_user(user, pw)
        self.login_user(user, pw)
        response = self.app.get('/v1/users/1', query_string=self.get_api_key_dict_of_current_user())
        self.assertEqual(response.status_code,200)
        self.assertTrue(self.does_data_contain_substring(response.data, "\"id\":1"))
        self.logout_user()


if __name__ == '__main__':
    unittest.main()
    #SQLalchemy tutorial https://stackoverflow.com/questions/14719507/unit-tests-for-query-in-sqlalchemy
    #Flask tutorial https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-unit-testing-legacy
