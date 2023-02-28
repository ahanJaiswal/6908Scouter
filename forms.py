from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    class Meta():
        csrf = False
    teamNum = IntegerField('Enter new Team Number', validators=[DataRequired()])
    teamName = StringField('Enter new Team Name')
    newDataSubmit = SubmitField('Submit New Team Entry')