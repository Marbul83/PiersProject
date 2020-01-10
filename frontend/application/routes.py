from flask import render_template, redirect, url_for, Response, request
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, password_hash as pw
from application.forms import LoginForm, NewChar1, NewChar2, PasswordForm, CreatePasswordForm
from application.models import user, background, feat

@app.route('/')
@app.route('/home')
def home():
    query = user.query.all()
    return render_template('home.html', title='D&D Gen', users=query)


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

@app.route('/new_char', methods=['GET','POST'])
def new_char():
    form=NewChar1()

    if form.validate_on_submit():
        char_name=form.char_name.data
        race=form.race.data
        char_class=form.char_class.data
        return redirect(url_for('new_char2', char_name=char_name, race=race, char_class=char_class))

    return render_template('new_char1.html', title='New Character', form=form)

@app.route('/new_char2/<char_name>/<race>/<char_class>', methods=['GET','POST'])
def new_char2(char_name, race, char_class):
    form=NewChar2()
    new_char={}
    if form.validate_on_submit():
        strength=form.strength.data
        dexterity=form.dexterity.data
        constitution=form.constitution.data
        intelligence=form.intelligence.data
        wisdom=form.wisdom.data
        charisma=form.charisma.data

        new_char={"char_name":char_name, "race":race, "char_class":char_class,
        "strength":strength, "dexterity":dexterity, "constitution":constitution,
        "intelligence":intelligence, "wisdom":wisdom, "charisma":charisma, "feats":""} 
        return new_char
        #return redirect(url_for('feats', char=new_char))
    return render_template('new_char2.html', title='New Character', form=form)


@app.route('/feats/<char>')
def feats(char):
    query = feat.query.all()
    return render_template('feats.html', title='Feats', feats=query, character=char)

@app.route('/submit/<feat>/<character>', methods=['GET','POST'])
def submit(feat, character):
    
    character['feats']=feat
    skill_dice=request.post('http://service1:5001/') #{"1":19,"2":16,"3":10,"4":7,"5":5,"6":4}
    background=request.post('http://service2:5002/') #{"Background":"Noble"}

    request={"Char":character,"Dice":skill_dice}

    char_complete=request.post=('http://backend:5003/',json=request)

    form = CreatePasswordForm()
    if form.validate_on_submit():
        hashed = pw.hash_password(form.password.data)
        user = user(
            char_name=char_complete["char_name"],
            race=char_complete["race"],
            char_class=char_complete["char_class"],
            strength=char_complete["strength"],
            dexterity=char_complete["dexterity"],
            constitution=char_complete["constitution"],
            intelligence=char_complete["intelligence"],
            wisdom=char_complete["wisdom"],
            charisma=char_complete["charisma"],
            background=background["Background"],
            feats=char_complete["feats"],
            password=hashed,
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        print(CreatePasswordForm.errors)
        return render_template('Password.html', title='Password', form=form)
    #send to back end
    #redirect to /character

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
			return redirect(url_for('character'))
	else:
		return render_template('change_password.html', title='Change Password', form=form)