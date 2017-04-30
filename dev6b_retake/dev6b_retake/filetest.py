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

    def test_statusC1(self):
        result = self.app.get('/c1')
        self.assertEqual(result.status_code,200)

    def test_statusC2(self):
        result = self.app.get('/c2')
        self.assertEqual(result.status_code,200)

    def test_statusW1(self):
        result = self.app.get('/w1')
        self.assertEqual(result.status_code,200)

    def test_statusW2(self):
        result = self.app.get('/w2')
        self.assertEqual(result.status_code,200)

    def test_statusindex(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code,200)

    def test_statusjsona1(self):
        result = self.app.get('/a1answers.json')
        self.assertEqual(result.status_code,200)
  
    def test_statusjsona2(self):
        result = self.app.get('/a2answers.json')
        self.assertEqual(result.status_code,200)

    def test_statusjsonc1(self):
        result = self.app.get('/c1answers.json')
        self.assertEqual(result.status_code,200)

    def test_statusjsonc2(self):
        result = self.app.get('/c2answers.json')
        self.assertEqual(result.status_code,200)

    def test_statusjsonaw1(self):
        result = self.app.get('/answersw1.json')
        self.assertEqual(result.status_code,200)

    def test_statusjsonw2(self):
        result = self.app.get('/answersw2.json')
        self.assertEqual(result.status_code,200)

    def test_statuslogin(self):
        result = self.app.get('/login')
        self.assertEqual(result.status_code,200)

    def test_JsonComparedWithDatabaseA1(self):
 
            result = self.app.get("/a1answers.json")
            db = mysql.connector.connect(user="root", passwd="usbw", host="vvdsl2.xs4all.nl",database="tommyvg")
            cursor = db.cursor()
            cursor.execute("SELECT answer FROM a1;")
            check = False
            if cursor.fetchone()[0] in result.data:
                check = True
            db.close()
            self.assertTrue(check)

    def test_JsonComparedWithDatabaseA2(self):
 
            result = self.app.get("/a2answers.json")
            db = mysql.connector.connect(user="root", passwd="usbw", host="vvdsl2.xs4all.nl",database="tommyvg")
            cursor = db.cursor()
            cursor.execute("SELECT answer FROM a2;")
            check = False
            if cursor.fetchone()[0] in result.data:
                check = True
            db.close()
            self.assertTrue(check)

    def test_JsonComparedWithDatabaseC1(self):
 
            result = self.app.get("/c1answers.json")
            db = mysql.connector.connect(user="root", passwd="usbw", host="vvdsl2.xs4all.nl",database="tommyvg")
            cursor = db.cursor()
            cursor.execute("SELECT answer FROM c1;")
            check = False
            if cursor.fetchone()[0] in result.data:
                check = True
            db.close()
            self.assertTrue(check)

    def test_JsonComparedWithDatabaseC2(self):
 
            result = self.app.get("/c2answers.json")
            db = mysql.connector.connect(user="root", passwd="usbw", host="vvdsl2.xs4all.nl",database="tommyvg")
            cursor = db.cursor()
            cursor.execute("SELECT answer FROM c2;")
            check = False
            if cursor.fetchone()[0] in result.data:
                check = True
            db.close()
            self.assertTrue(check)

    def test_JsonComparedWithDatabaseW1(self):
 
            result = self.app.get("/answersw1.json")
            db = mysql.connector.connect(user="root", passwd="usbw", host="vvdsl2.xs4all.nl",database="tommyvg")
            cursor = db.cursor()
            cursor.execute("SELECT answer FROM w1;")
            check = False
            if cursor.fetchone()[0] in result.data:
                check = True
            db.close()
            self.assertTrue(check)

    def test_JsonComparedWithDatabaseW2(self):
 
            result = self.app.get("/answersw2.json")
            db = mysql.connector.connect(user="root", passwd="usbw", host="vvdsl2.xs4all.nl",database="tommyvg")
            cursor = db.cursor()
            cursor.execute("SELECT answer FROM w2;")
            check = False
            if cursor.fetchone()[0] in result.data:
                check = True
            db.close()
            self.assertTrue(check)

    def test_login(self):
          result = self.app.post("/loginauth",data=dict(user="user",passw="password"))
          self.assertEqual(json.loads(result.data)['status'], "OK")

if __name__ == '__main__':
    unittest.main()
