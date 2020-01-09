from flask import render_template, redirect, url_for, Response, request
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, password_hash as pw
from application.forms import LoginForm, NewChar1, NewChar2, PasswordForm
from application.models import user, background, feat

@app.route('/')
@app.route('/home')
def home():
    query = user.query.filter_by(char_name).all()
	return render_template('home.html', title='D&D Gen', char_names=query)

@app.route('/login/<char_name>', methods=['GET','POST'])
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
    form=NewChar1
    new_char={}
    if form.validate_on_submit():
        char_name=form.char_name
        race=form.race
        char_class=form.char_class
        form2=NewChar2
        if form2.validate_on_submit():
            strength=form2.strength
            dexterity=form2.dexterity
            constitution=form2.constitution
            intelligence=form2.intelligence
            wisdom=form2.wisdom
            charisma=form2.charisma

            new_char={"char_name"=char_name, "race"=race, "char_class"=char_class,
            "strength"=strength, "dexterity"=dexterity, "constitution"=constitution,
            "intelligence"=intelligence, "wisdom"=wisdom, "charisma"=charisma, "feats"=""}

            return redirect(url_for('feats', char=new_char))
        return render_template('new_char2.html', title='New Character', form=form2)
    return render_template('new_char1.html', title='New Character', form=form)

@app.route('/feats/<char>')
def feats(char):
    query = feat.query.filter_by(id, name, effects).all()
    return render_template('feats.html', title='Feats', feats=query, character=char)

@app.route('/submit/<feat>/<character>', methods=['GET','POST'])
def submit():
    character.feats=feat

    #random roll apps
    #send to back end

@app.route('/character', methods=['GET','POST'])
@login_required
def display_char():
    return render_template('DisplayChar.html', title=current_user.char_name, user=current_user)

@app.route("/change_password", methods=['GET','POST'])
@login_required
def change_password():
	form = PasswordForm()
	if form.validate_on_submit():
		if pw.verify_password(current_user.password, form.current_password.data):
			hash = pw.hash_password(form.password.data)
			current_user.password = hash
			db.session.commit()
			return redirect(url_for('account'))
	else:
		return render_template('change_password.html', title='Change Password', form=form)