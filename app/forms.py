from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TwitterHandleForm(FlaskForm):
    twitterhandle = StringField('Twitter Handle', validators=[DataRequired()])
    submit = SubmitField('Generate Pie Chart')
