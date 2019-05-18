# -*- coding: utf-8 -*-

from flask import render_template

from app import app

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title='index')


@app.route('/info')
def info():
    return render_template('data.html')

@app.route('/evadir')
def evadir():

    arquivo = pd.read_csv('/home/WadsonGarbes/wmlapp/app/static/data/data.csv')

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

    prob = prob[1:-1]

    return prob

@app.route('/permanecer')
def permanecer():

    arquivo = pd.read_csv('/home/WadsonGarbes/wmlapp/app/static/data/data.csv')

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

    prob = prob[1:-1]

    return prob

@app.route('/evadir/<int:num>')
def evadir_num(num):
    try:

        arquivo = pd.read_csv('/home/WadsonGarbes/wmlapp/app/static/data/data.csv')

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

        prob = str(prob[num]) + "\n"

        return prob

    except IndexError:

        return """list index out of range - from 0 to 400 only!\n"""

@app.route('/permanecer/<int:num>')
def permanecer_num(num):

    try:

        arquivo = pd.read_csv('/home/WadsonGarbes/wmlapp/app/static/data/data.csv')

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

        prob = str(prob[num]) + "\n"

        return prob

    except IndexError:

        return """list index out of range - from 0 to 400 only!\n"""
