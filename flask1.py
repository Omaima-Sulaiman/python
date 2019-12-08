#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 09:36:35 2019

@author: omaima

"""
# =============================================================================
# from flask import Flask , render_template
# app=Flask(__name__)
# @app.route('/')
# 
# 
# def index():
#     return render_template('hello.html')
# =============================================================================
    

# =============================================================================
# if __name__ =='__main__':
# =============================================================================
# =============================================================================
#     app.run(debug = True)
# =============================================================================
    
# =============================================================================
# @app.route('/hello/<int:score>')
# def hello_name(score):
#     return render_template('hello.html',marks=score)
# if __name__ == '__main__':
#     app.run()
# =============================================================================


#Q1
    
# =============================================================================
# from flask import Flask
# app=Flask(__name__)
# @app.route('/')
# def index():
#     return 'This is the Index page'
# @app.route('/hello')
# def hello():
#     return "Hello World!"
# @app.route('/members')
# def member():
#     return "Members page"
# if __name__=='__main__':
#     app.run()
# =============================================================================

# =============================================================================
# Q2
# =============================================================================
# =============================================================================
# 
# from flask import Flask,render_template
# app=Flask(__name__)
# @app.route('/index/<int:marks>')
# def hello(marks):
#     return render_template('Index.html',marks=marks)
# if __name__=='__main__':
#     app.run()
# =============================================================================


# =============================================================================
# Q3
# =============================================================================


from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def hello(): 
    return render_template('exe2.html')
if __name__=='__main__':
     app.run()











































