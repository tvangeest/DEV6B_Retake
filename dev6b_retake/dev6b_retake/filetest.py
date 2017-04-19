import unittest, json
from flask import *
from app import app
import mysql.connector

class Test_unittests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_statusA1(self):
        result = self.app.get('/a1')
        self.assertEqual(result.status_code,200)

    def test_statusA2(self):
        result = self.app.get('/a2')
        self.assertEqual(result.status_code,200)

    def test_statusindex(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code,200)

    def test_jsona1(self):
        result = self.app.get('/a1answers.json')
        self.assertEqual(result.status_code,200)
  
    def test_jsona2(self):
        result = self.app.get('/a2answers.json')
        self.assertEqual(result.status_code,200)


if __name__ == '__main__':
    unittest.main()
