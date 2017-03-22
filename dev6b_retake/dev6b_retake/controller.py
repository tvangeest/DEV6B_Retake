from flask import Flask, render_template, request

class Controller:

  def index(): 
    return render_template('index.html')

  def a1():
    if request.method == 'GET':
      return render_template('A1.html')
  
  def a2():
    if request.method == 'GET':
      return render_template('A2.html')