# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template


from app import app

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

import re

@app.route('/')
@app.route('/index')
def index():
    
    arquivo = pd.read_csv('/home/wadson/wmlapp/app/static/data/data.csv')
    
    X = arquivo.drop('drop', axis=1)
    Y = arquivo['drop']
    
    x_train, x_test, y_train, y_test = train_test_split(X, Y,
                                                        test_size=0.30, 
                                                        random_state=1)
                                                        
    logmodel = LogisticRegression()
    
    logmodel.fit(x_train, y_train)
    
    pred_probs = logmodel.predict_proba(arquivo.drop('drop', axis=1))
    
    prob1 = pred_probs[:, 1]
    prob2 = pred_probs[:, 0]
    
    prob1 = list(prob1)
    
    return render_template('index.html',
                            title='index',
                            prob1=prob1,
                            prob2=prob2)
                            
@app.route('/evadir')
def evadir():
    
    arquivo = pd.read_csv('/home/wadson/wmlapp/app/static/data/data.csv')
    
    X = arquivo.drop('drop', axis=1)
    Y = arquivo['drop']
    
    x_train, x_test, y_train, y_test = train_test_split(X, Y,
                                                        test_size=0.30, 
                                                        random_state=1)
                                                        
    logmodel = LogisticRegression()
    
    logmodel.fit(x_train, y_train)
    
    pred_probs = logmodel.predict_proba(arquivo.drop('drop', axis=1))
    
    prob = pred_probs[:, 1]
    
    prob = list(prob)
    
    prob = str(prob)
    
    return prob
    
@app.route('/permanecer')
def permanecer():
    
    arquivo = pd.read_csv('/home/wadson/wmlapp/app/static/data/data.csv')
    
    X = arquivo.drop('drop', axis=1)
    Y = arquivo['drop']
    
    x_train, x_test, y_train, y_test = train_test_split(X, Y,
                                                        test_size=0.30, 
                                                        random_state=1)
                                                        
    logmodel = LogisticRegression()
    
    logmodel.fit(x_train, y_train)
    
    pred_probs = logmodel.predict_proba(arquivo.drop('drop', axis=1))
    
    prob = pred_probs[:, 0]
    
    prob = list(prob)
    
    prob = str(prob)
    
    return prob
                            
@app.route('/evadir/<int:num>')
def evadir_num(num):
    
    arquivo = pd.read_csv('/home/wadson/wmlapp/app/static/data/data.csv')
    
    X = arquivo.drop('drop', axis=1)
    Y = arquivo['drop']
    
    x_train, x_test, y_train, y_test = train_test_split(X, Y,
                                                        test_size=0.30, 
                                                        random_state=1)
                                                        
    logmodel = LogisticRegression()
    
    logmodel.fit(x_train, y_train)
    
    pred_probs = logmodel.predict_proba(arquivo.drop('drop', axis=1))
    
    prob = pred_probs[:, 1]
    
    prob = list(prob)
    
    prob = str(prob[num])
    
    return prob
    
@app.route('/permanecer/<int:num>')
def permanecer_num(num):
    
    arquivo = pd.read_csv('/home/wadson/wmlapp/app/static/data/data.csv')
    
    X = arquivo.drop('drop', axis=1)
    Y = arquivo['drop']
    
    x_train, x_test, y_train, y_test = train_test_split(X, Y,
                                                        test_size=0.30, 
                                                        random_state=1)
                                                        
    logmodel = LogisticRegression()
    
    logmodel.fit(x_train, y_train)
    
    pred_probs = logmodel.predict_proba(arquivo.drop('drop', axis=1))
    
    prob = pred_probs[:, 0]
    
    prob = list(prob)
    
    prob = str(prob[num])
    
    return prob