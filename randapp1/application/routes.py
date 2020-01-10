from flask import render_template, redirect, url_for, Response, request
import random
from application import app

@app.route('/')
@app.route('/roll', methods=['GET','POST'])
def roll():
    rolls=[]
    results={"1": "","2": "","3": "","4": "","5": "", "6": ""}

    for i in range(8):
        roll = random.randint(0, 20)
        rolls.append(roll)

    rolls.sort(reverse = True)
    bin = rolls.pop()
    bin = rolls.pop()
    for j in range(6):
        results[str(j+1)]=rolls[j]
    return results