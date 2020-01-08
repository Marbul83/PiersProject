from flask import render_template, redirect, url_for, Response, request
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, password_hash as pw
from application.forms import LoginForm
from application.models import user, background, feat

@app.route('/')
@app.route('/home')
def home():
    query = user.query.filter_by(char_name).all()
	return render_template('home.html', title='D&D Gen', char_names=query)

@app.route('/login', methods=['GET','POST'])
def login(char_name):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = user.query.filter_by(char_name=char_name).first()
        if user and pw.verify_password(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('character'))
    return render_template('login.html', title='Login', form=form, character=char_name)

@app.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route('/new-character', methods=['GET','POST'])
def new_char():


@app.route('/character', methods=['GET','POST'])
@login_required
def display_char():
    current_user.char_name
    current_user.health
    current_user.strength
    current_user.dexterity
    current_user.constitution
    current_user.intelligence
    current_user.wisdom
    current_user.charisma
    current_user.background
