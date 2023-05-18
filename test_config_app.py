import unittest
from flask import session
from app import app

SQLALCHEMY_DATABASE_URI = 'currency_test_db'


class ConverterRouteTestCase(unittest.TestCase):
    def setUp(self):
        """ Set Up Test Env """
        app.config.from_object('config.Config')
        self.client = app.test_client()

    def tearDown(self):
        """ Tear Down Test Env """
        pass

    def test_converter_route(self):
        """ Test /converter route """
        response = self.client.get('/converter', follow_redirects=True)

        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Converter', response.data)
        self.assertIn(b'From Currency', response.data)
        self.assertIn(b'To Currency', response.data)
        self.assertIn(b'Amount', response.data)

    def test_show_results_none(self):
        """ Test /results route with no conversion """
        with self.client:
            with self.client.session:
                response = self.client.get('/results')
                self.assertIn(response.status_code, [200, 302])

                self.assertIsNone(session['result'])

                self.assertIn(b'Converter', response.data)
                self.assertIn(b'From Currency', response.data)
                self.assertIn(b'To Currency', response.data)
                self.assertIn(b'Amount', response.data)
                self.assertIn(b'Result', response.data)


    def test_show_results_result(self):
        """ Test /results route with conversion """
        with self.client:
            session['from_currency'] = 'USD'
            session['to_currency'] = 'USD'
            session['result'] = 1.0

            response = self.client.get('/results')
            self.assertIn(response.status_code, [200, 302])

            with self.client.session_transaction() as session:
                self.assertEqual(session.get('result'), 1.0)

            self.assertIn(b'From Currency', response.data)
            self.assertIn(b'To Currency', response.data)
            self.assertIn(b'Amount', response.data)
            self.assertIn(b'Result', response.data)

if __name__ == '__main__':
    unittest.main()
