from flask import render_template, redirect, url_for, Response, request
import random
from application import app

@app.route('/')
@app.route('/back_end/<json>', methods=['GET','POST'])
def back_end(json):

    dice=json["Dice"]
    char=json["Char"]
    skills=[char["strength"],char["dexterity"],char["constitution"],char["intelligence"],char["wisdom"],char["charisma"]]
    sort=[]
    for skill in skills:
        for key in dice:
            if key == skill:
                sort.append(dice[key])
    char["strength"]=sort[0]
    char["dexterity"]=sort[1]
    char["constitution"]=sort[2]
    char["intelligence"]=sort[3]
    char["wisdom"]=sort[4]
    char["charisma"]=sort[5]
    return char