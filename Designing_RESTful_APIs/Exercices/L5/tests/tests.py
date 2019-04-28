import os
import sys
import json
import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append('../')

from app import app, login_manager
from models import User, Base, MealRequest, Proposal
from dbSession import session as _session, engine



class TestCase(unittest.TestCase):
    dev_mode_enabled = False
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
            self.session.flush()
            self.session.query(User).delete()
            self.session.query(MealRequest).delete()
            self.session.query(Proposal).delete()
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

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Get_login_positive_checkIfLoginRouteIsCorrect(self):
        self.does_url_response_contain_substring( '/login', r'<title>Login</title>')

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Get_forwardslash_positive_checkIfLandingpageRouteIsCorrect(self):
        self.does_url_response_contain_substring( '/', r'<title>Meet\'N eat</title>')

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Get_apiKey_positive_checkIfApiKeyRouteRedirectsToLogin(self):
        self.does_url_response_contain_substring( '/apiKey', r'<title>Login</title>')

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Get_logout_positive_checkIfLogoutRouteRedirectsToLogin(self):
        self.does_url_response_contain_substring( '/logout', r'<title>Login</title>')

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Post_login_negative_checktIfLoginWithWrongCredentialFails(self):
        user_name = 'Nawin'
        pw = 'something'
        self.create_minimal_user(user_name,pw)
        response = self.app.post('/login', data=dict(username=user_name, password='qweq'), follow_redirects=True)
        self.assertEqual(response.status_code,200)
        self.assertTrue(self.does_data_contain_substring(response.data,r'<strong>Error!</strong> Invalid Credentials\n'))

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Post_login_positive_checktIfLoginWithCorrectCredentialPass(self):
        user_name = 'Nawin'
        pw = '1234'
        self.create_minimal_user(user_name, pw)
        response = self.app.post('/login', data=dict(username=user_name, password=pw), follow_redirects=True)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.is_json, True)
        self.assertNotEqual(response.get_json().get('token'),None)

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Get_v1_users_negative_checkIfUsersRouteFailsWithNoToken(self):
        result = self.app.get('/v1/users')
        self.assertEqual(result.status_code, 401)

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Get_v1_users_negative_checkIfUsersRouteFailsWithWrongToken(self):
        result = self.app.get('/v1/users',query_string=dict(token='asda'))
        self.assertEqual(result.status_code,401)

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Get_v1_users_positive_checkIfUsersRoutePassesWithCorrectToken(self):
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

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Get_v1_users_negative_checkIfUsersRouteFailsWhenNoUserExists(self):
        response = self.app.get('/v1/users', query_string =dict(token='asdasd'))
        self.assertTrue(self.does_data_contain_substring(response.data, 'Unauthorized address trying to use'))

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Put_v1_users_positive_checkIfChangingAnExsitstingTokenWorks(self):
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

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Put_v1_users_negativ_checkIfChangingAnExsitstingTokenWhitNoSpecifiedUserFails(self):
        new_token = '1234'
        self.create_minimal_user('Nawin','1234')
        self.login_user('Nawin','1234')
        response =  self.app.put('/v1/users', query_string=self.get_api_key_dict_of_current_user(),
                                               data=json.dumps({'token':new_token}) ,mimetype='application/json' )
        self.assertEqual(response.status_code, 404)
        self.logout_user()

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Delete_v1_users_positive_checkIfDeletingAUserWorks(self):
        user = 'Nawin'
        pw = '1234'
        self.create_minimal_user(user, pw)
        self.create_minimal_user('Second', 'abcd')
        self.login_user(user, pw)
        token = self.get_api_key_dict_of_current_user()

        #check number of users before deleting is two
        response = self.app.get('/v1/users', query_string=token)
        self.assertEqual(response.status_code,200)
        self.assertTrue(response.is_json)
        self.assertEqual(len(response.get_json()),2)

        #issue the delete request
        response = self.app.delete('/v1/users', query_string=token,
                                                data=json.dumps(dict(user_name='Second')),mimetype='application/json')
        self.assertEqual(response.status_code,200)
        self.assertTrue(self.does_data_contain_substring(response.data,'Success, deleted user:'))

        #check number of users before deleting is two
        response = self.app.get('/v1/users', query_string=token)
        self.assertEqual(response.status_code,200)
        self.assertTrue(response.is_json)
        self.assertEqual(len(response.get_json()),1)
        self.logout_user()

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Delete_v1_users_negative_checkIfDeletingANonExistingUserFails(self):
        user = 'Nawin'
        pw = '1234'
        self.create_minimal_user(user, pw)
        self.login_user(user, pw)
        token = self.get_api_key_dict_of_current_user()

        #check number of users before deleting is one
        response = self.app.get('/v1/users', query_string=token)
        self.assertEqual(response.status_code,200)
        self.assertTrue(response.is_json)
        self.assertEqual(len(response.get_json()),1)

        #issue the delete request
        response = self.app.delete('/v1/users', query_string=token,
                                                data=json.dumps(dict(user_name='Second')),mimetype='application/json')
        self.assertEqual(response.status_code,404)
        self.assertTrue(self.does_data_contain_substring(response.data,'ERROR, user not found'))

        #check number of users after deleting is still one
        response = self.app.get('/v1/users', query_string=token)
        self.assertEqual(response.status_code,200)
        self.assertTrue(response.is_json)
        self.assertEqual(len(response.get_json()),1)
        self.logout_user()

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Get_v1_users_id_negative_checkIfInitalGettingAUserFails(self):
        response = self.app.get('/v1/users/0')
        self.assertEqual(response.status_code, 401)

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Get_v1_users_id_negative_checkIfGettingANonexistenUserFails(self):
        user = 'Nawin'
        pw = 'Something'
        self.create_minimal_user(user, pw)
        self.login_user(user, pw)
        response = self.app.get('/v1/users/0', query_string=self.get_api_key_dict_of_current_user())
        self.assertEqual(response.status_code,404)
        self.assertTrue(self.does_data_contain_substring(response.data, "ERROR, user 0 not found!"))
        self.logout_user()

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Get_v1_users_id_positive_checkIfGettingAExistenUserPass(self):
        user = 'Nawin'
        pw = 'Something'
        self.create_minimal_user(user, pw)
        self.login_user(user, pw)
        response = self.app.get('/v1/users/1', query_string=self.get_api_key_dict_of_current_user())
        self.assertEqual(response.status_code,200)
        self.assertTrue(self.does_data_contain_substring(response.data, "\"id\":1"))
        self.logout_user()

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Post_v1_requests_positive_checkIfCreatingAValidMealRequestWorks(self):
        user = 'Nawin'
        pw = 'Something'

        payload = dict(meal_type="Tacos", location_area='Ann Arbor',
                       appointment_date='4/20/2019', meal_time='07:00PM')

        self.create_minimal_user(user, pw)
        self.login_user(user, pw)

        response = self.app.post('/v1/requests', query_string=self.get_api_key_dict_of_current_user(),
                                                 data=json.dumps(payload),mimetype='application/json')
        self.assertEqual(response.status_code,201)
        self.assertTrue(self.does_data_contain_substring(response.data, 'Success, created request:'))
        self.logout_user()

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Get_v1_requests_positive_checkIfGettingAValidMealRequestWorks(self):
        user = 'Nawin'
        pw = 'Something'

        payload = dict(meal_type="Tacos", location_area='Ann Arbor',
                       appointment_date='4/20/2019', meal_time='07:00PM')

        self.create_minimal_user(user, pw)
        self.login_user(user, pw)

        response = self.app.post('/v1/requests', query_string=self.get_api_key_dict_of_current_user(),
                                                 data=json.dumps(payload),mimetype='application/json')

        self.assertEqual(response.status_code,201)
        self.assertTrue(self.does_data_contain_substring(response.data, 'Success, created request:'))
        response = self.app.get('/v1/requests',query_string=self.get_api_key_dict_of_current_user())
        self.assertTrue(self.does_data_contain_substring(response.data,'\"appointment_date\":\"4/20/2019\"'))
        self.logout_user()

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Get_v1_requests_positive_createMultipleValidMealRequests(self):
        user = 'Nawin'
        pw = 'Something'

        payload = dict(meal_type='Tacos', location_area='Ann Arbor',
                       appointment_date='4/20/2019', meal_time='07:00PM')

        self.create_minimal_user(user, pw)
        self.login_user(user, pw)

        response = self.app.post('/v1/requests', query_string=self.get_api_key_dict_of_current_user(),
                                                 data=json.dumps(payload),mimetype='application/json')

        self.assertEqual(response.status_code,201)
        self.assertTrue(self.does_data_contain_substring(response.data, 'Success, created request:'))


        response = self.app.get('/v1/requests',query_string=self.get_api_key_dict_of_current_user())
        self.assertTrue(self.does_data_contain_substring(response.data,'\"meal_type\":\"{}\"'.format(payload['meal_type'])))

        payload['meal_type'] = 'Burgers'

        response = self.app.post('/v1/requests', query_string=self.get_api_key_dict_of_current_user(),
                                                 data=json.dumps(payload),mimetype='application/json')

        self.assertEqual(response.status_code,201)
        self.assertTrue(self.does_data_contain_substring(response.data, 'Success, created request:'))

        response = self.app.get('/v1/requests',query_string=self.get_api_key_dict_of_current_user())
        self.assertTrue(self.does_data_contain_substring(response.data,'\"meal_type\":\"{}\"'.format(payload['meal_type'])))
        self.logout_user()

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_post_v1_requests_negative_checkIfMultipleINcompletePosts(self):
        user = 'Nawin'
        pw = 'Something'
        self.create_minimal_user(user, pw)
        self.login_user(user, pw)

        response = self.app.post('/v1/requests', query_string=self.get_api_key_dict_of_current_user(),
                                                 data=json.dumps(dict(meal_type='Pizza')),mimetype='application/json')
        self.assertEqual(response.status_code,404)
        self.assertTrue(self.does_data_contain_substring(response.data, 'Error some input arguments are missing!'))

        response = self.app.post('/v1/requests', query_string=self.get_api_key_dict_of_current_user(),
                                                 data=json.dumps(dict(random='stuff')),mimetype='application/json')
        self.assertEqual(response.status_code,404)
        self.assertTrue(self.does_data_contain_substring(response.data, 'Error some input arguments are missing!'))
        self.logout_user()

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Get_v1_requests_id_positive_checkIfQueryingOfMealRequestsWorkBeforeAndAfterPostingOne(self):
        user = 'Nawin'
        pw = 'Somegt'

        payload = dict(meal_type="Tacos", location_area='Ann Arbor',
                       appointment_date='4/20/2019', meal_time='07:00PM')

        self.create_minimal_user(user, pw)
        self.login_user(user, pw)

        response = self.app.get('/v1/requests/1', query_string=self.get_api_key_dict_of_current_user())
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data,b'None')

        response = self.app.post('/v1/requests', query_string=self.get_api_key_dict_of_current_user(), data=json.dumps(payload),mimetype='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertTrue(self.does_data_contain_substring(response.data, 'Success, created request:'))

        response = self.app.get('/v1/requests/1', query_string=self.get_api_key_dict_of_current_user())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.does_data_contain_substring(response.data,'\"appointment_date\":\"4/20/2019\"'))
        self.assertTrue(response.is_json)
        self.assertTrue(response.get_json().get('location_name') != None)

        response = self.app.get('/v1/requests/0', query_string=self.get_api_key_dict_of_current_user())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'None')

        self.logout_user()

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Put_v1_requests_id_positive_updateAMealRequest(self):
        user = 'Nawin'
        pw = 'something'
        self.create_minimal_user(user,pw)
        self.login_user(user,pw)
        token = self.get_api_key_dict_of_current_user()
        payload = dict(meal_type="Tacos", location_area='Ann Arbor',
                       appointment_date='4/20/2019', meal_time='07:00PM')

        updated_payload = dict(meal_type="Burger", location_area='Detroit',
                       appointment_date='5/21/2020', meal_time='09:00AM')

        response = self.app.post('/v1/requests', query_string=token, data=json.dumps(payload), mimetype='application/json')
        self.assertEqual(response.status_code,201)

        response = self.app.get('/v1/requests/1', query_string=token)
        self.assertEqual(response.status_code,200)
        for key in payload:
            self.assertTrue(self.does_data_contain_substring(response.data, payload[key]))

        response = self.app.put('/v1/requests/1',query_string=token, data=json.dumps(updated_payload), mimetype='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.app.get('/v1/requests/1',query_string=token)
        self.assertEqual(response.status_code,200)

        for key in updated_payload:
            self.assertTrue(self.does_data_contain_substring(response.data, updated_payload[key]))
            self.assertFalse(self.does_data_contain_substring(response.data, payload[key]))

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Delete_route_v1_requests_id_positive_deleteMealRequestEntety(self):
        user = 'Nawin'
        pw = 'Something'
        self.create_minimal_user(user, pw)
        self.login_user(user,pw)

        token = self.get_api_key_dict_of_current_user()

        payload = dict(meal_type="Tacos", location_area='Ann Arbor',
                       appointment_date='4/20/2019', meal_time='07:00PM')

        response = self.app.post('/v1/requests', query_string=token, data=json.dumps(payload), mimetype='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.app.get('/v1/requests/1', query_string=token)
        self.assertEqual(response.status_code, 200)
        for key in payload:
            self.assertTrue(self.does_data_contain_substring(response.data, payload[key]))

        response = self.app.delete('/v1/requests/1', query_string=token)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.does_data_contain_substring(response.data, 'Success, deleted request: 1'))

        response  = self.app.get('/v1/requests', query_string=token)
        self.assertEqual(response.status_code,200)
        self.assertTrue(self.does_data_contain_substring(response.data, '[]'))

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Post_v1_proposals_complete_checkIfGeneratingAProposalOfADiffrentUserWorks(self):
        self.create_minimal_user('User1', 'Pw1')
        self.create_minimal_user('User2', 'Pw2')

        self.login_user('User1','Pw1')
        response = self.app.post('/v1/requests', query_string=self.get_api_key_dict_of_current_user(),
        data=json.dumps(dict(meal_type='Pizza', location_area='Detroit', appointment_date='4/22/2019')), mimetype='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertTrue(self.does_data_contain_substring(response.data, 'Success, created request'))

        response = self.app.get('/v1/requests', query_string= self.get_api_key_dict_of_current_user())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.does_data_contain_substring(response.data, 'Pizza'))
        meal_request_data = response.get_json()
        self.logout_user()

        self.login_user('User2', 'Pw2')

        response = self.app.post('/v1/proposals', query_string=self.get_api_key_dict_of_current_user(),
        data=json.dumps(dict(request_id=meal_request_data[0].get('id')+1)),
        mimetype='application/json')

        self.assertEqual(response.status_code,404)
        self.assertTrue(self.does_data_contain_substring(response.data,'ERROR, request id {} not found'.format(meal_request_data[0].get('id')+1)))

        response = self.app.post('/v1/proposals', query_string=self.get_api_key_dict_of_current_user(), data=json.dumps(dict(request_id=meal_request_data[0].get('id'))),
        mimetype='application/json')
        self.assertEqual(response.status_code,201)
        self.assertTrue(self.does_data_contain_substring(response.data, 'Success, created proposal: 1!'))

        response = self.app.post('/v1/proposals', query_string=self.get_api_key_dict_of_current_user(), data=json.dumps(dict(request_id=meal_request_data[0].get('id'))),
        mimetype='application/json')
        self.assertEqual(response.status_code,404)
        self.assertTrue(self.does_data_contain_substring(response.data,'ERROR, request id {} does already exist'.format(meal_request_data[0].get('id'))))
        self.logout_user()

    @unittest.skipIf(dev_mode_enabled, 'Do not run in developer mode!')
    def test_Get_v1_proposals_positive_checkIfGeneratingAProposalOfADiffrentUserWorksWhithQueryResponse(self):
        self.create_minimal_user('User1', 'Pw1')
        self.create_minimal_user('User2', 'Pw2')
        self.create_minimal_user('User3', 'Pw3')
        self.login_user('User1','Pw1')

        response = self.app.post('/v1/requests',  query_string=self.get_api_key_dict_of_current_user(),
        data=json.dumps(dict(meal_type='Pizza', location_area='Detroit', appointment_date='4/22/2019')), mimetype='application/json')
        self.assertEqual(response.status_code,201)

        response = self.app.get('/v1/requests', query_string=self.get_api_key_dict_of_current_user())
        self.assertEqual(response.status_code,200)
        self.assertTrue(self.does_data_contain_substring(response.data, 'Detroit'))
        meal_request_data = response.get_json()
        self.logout_user()

        self.login_user('User2','Pw2')
        response = self.app.post('/v1/proposals', query_string=self.get_api_key_dict_of_current_user(),
        data=json.dumps(dict(request_id=meal_request_data[0].get('id'))), mimetype='application/json')
        self.assertEqual(response.status_code,201)
        self.logout_user()

        self.login_user('User1', 'Pw1')
        response = self.app.get('/v1/proposals', query_string=self.get_api_key_dict_of_current_user())
        self.assertEqual(response.status_code,200)
        self.assertTrue(self.does_data_contain_substring(response.data,'\"user_porposed_to\":\"User1\"'))
        self.logout_user()

        self.login_user('User2','Pw2')
        response = self.app.get('/v1/proposals', query_string=self.get_api_key_dict_of_current_user())
        self.assertEqual(response.status_code,200)
        self.assertTrue(self.does_data_contain_substring(response.data,'\"user_porposed_from\":\"User2\"'))
        self.logout_user()

        self.login_user('User3','Pw3')

        response = self.app.get('/v1/proposals', query_string=self.get_api_key_dict_of_current_user())
        self.assertEqual(response.status_code,200)
        self.assertTrue(self.does_data_contain_substring(response.data,'[]'))
        self.logout_user()

    def testDev(self):
        print("asd")

if __name__ == '__main__':
    #@Hint:
    # Refactor test cases such that the naming scheme is consistent and easy to follow.
    # The scheme should contain the Http request method e.g.
    # test_<request_type>_<url_scheme>_<positive_negative_complete_test>
    # test_Get_v2_requests_id_positive_getAllPostedRequests

    unittest.main()
