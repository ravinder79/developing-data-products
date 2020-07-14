from flask import Flask
import numpy as np
app = Flask(__name__)
from flask import render_template, request
from random import randint
from model import predict


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll-dice/<int:n>')
def roll_n_dice(n):
    rolls = [str(randint(1, 6)) for i in range(n)]
    return f'Your rolls are: {", ".join(rolls)}'


@app.route('/input')
def how_user_input():
    return render_template('input-form.html')


@app.route('/input', methods=['POST'])
def handle_text_submission():
    input1 = request.form['input']
    result = predict('input')
    return f'You entered: {input1}. The text you entered is {result}!'
