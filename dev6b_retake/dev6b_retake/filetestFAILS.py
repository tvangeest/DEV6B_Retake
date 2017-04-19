import unittest, json
from flask import *
from app import app
import mysql.connector

class Z_Test_filetestFAILS(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_statusA1fail(self):
        result = self.app.get('/a1')
        self.assertEqual(result.status_code,404)

    def test_statusA2fail(self):
        result = self.app.get('/a2')
        self.assertEqual(result.status_code,404)

    def test_statusindexfail(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code,404)

    def test_jsona1fail(self):
        result = self.app.get('/a1answers.json')
        self.assertEqual(result.status_code,404)
  
    def test_jsona2fail (self):
        result = self.app.get('/a2answers.json')
        self.assertEqual(result.status_code,404)


if __name__ == '__main__':
    unittest.main()

