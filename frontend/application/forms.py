from wtforms import StringField, SubmitField, IntegerField, PasswordField, SelectField BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import user, background, skill
from application import login_manager, password_hash as pw

class LoginForm(FlaskForm):
    password = PasswordField('Password: ',
        validators=[DataRequired(message=None), Length(min=5, max=30)
        ]    
    )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign in')

class NewChar1(FlaskForm):
    char_name = StringField('Character name: ',
        validators=[DataRequired(message=None), Length(min=2, max=30)
        ]    
    )
    race = SelectField(
        'Race: ',
        choices=[
            ('Human','Human'), 
            ('Elf','Elf'), 
            ('Dwarf','Dwarf'), 
            ('Halfling','Halfling'), 
            ('Gnome','Gnome'), 
            ('Half-Orc','Half-Orc'),
            ('Tiefling','Tiefling'),
            validators=[DataRequired(message=None)]
        ]
    )
    char_class = SelectField(
        'Class: ',
        choices=[
            ('Fighter','Fighter'),
            ('Wizard','Wizard'),
            ('Cleric','Cleric'),
            ('Rogue','Rogue'),
            ('Ranger','Ranger'),
            validators=[DataRequired(message=None)]
        ]
    )
    submit = SubmitField('Confirm')

class NewChar2(FlaskForm):
    strength = SelectField(
        'Strength: ',
        choices=[
            ('1','1'),
            ('2','2'),
            ('3','3'),
            ('4','4'),
            ('5','5'),
            ('6','6'),
        ]
    )
    dexterity = SelectField(
        'Dexterity: ',
        choices=[
            ('1','1'),
            ('2','2'),
            ('3','3'),
            ('4','4'),
            ('5','5'),
            ('6','6'),
        ]
    )
    constitution = SelectField(
        'Constitution: ',
        choices=[
            ('1','1'),
            ('2','2'),
            ('3','3'),
            ('4','4'),
            ('5','5'),
            ('6','6'),
        ]
    )
    intelligence = SelectField(
        'Intelligence: ',
        choices=[
            ('1','1'),
            ('2','2'),
            ('3','3'),
            ('4','4'),
            ('5','5'),
            ('6','6'),
        ]
    )
    wisdom = SelectField(
        'Wisdom: ',
        choices=[
            ('1','1'),
            ('2','2'),
            ('3','3'),
            ('4','4'),
            ('5','5'),
            ('6','6'),
        ]
    )
    charisma = SelectField(
        'Charisma: ',
        choices=[
            ('1','1'),
            ('2','2'),
            ('3','3'),
            ('4','4'),
            ('5','5'),
            ('6','6'),
        ]
    )
    submit = SubmitField('Confirm')

    def validate(self):
        result = True
        seen = set()
        for field in [self.strength, self.dexterity, self.constitution, 
            self.intelligence, self.wisdom, self.charisma]:
            if field.data in seen:
                field.errors.append('Please select six different numbers')
                result = False
            else:
                seen.add(field.data)
        return result