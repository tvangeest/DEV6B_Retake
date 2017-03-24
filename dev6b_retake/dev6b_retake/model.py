from flask import *
class Model(object):
    def a1():
        a = []
        for x in range (0,10):
            a[x] = request.form['a' + str((x+1))]
            print(a[x])