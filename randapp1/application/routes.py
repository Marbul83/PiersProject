from flask import render_template, redirect, url_for, Response, request
import random
from application import app

@app.route('/', methods=['GET','POST'])
@app.route('/roll', methods=['GET','POST'])
def roll():
    rolls=[]

    for i in range(8):
        roll = random.randint(0, 20)
        rolls.append(roll)

    rolls.sort(reverse = True)
    bin = rolls.pop()
    bin = rolls.pop()
    return {"1":rolls[0],"2":rolls[1],"3":rolls[2],"4":rolls[3],"5":rolls[4], "6":rolls[5]}