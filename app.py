from flask import Flask
from flask import Flask, request, render_template, redirect, url_for, session, send_file

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, RadioField, DateTimeField, DateField, SelectField, TextAreaField

from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = 'myscript'

class Widgets(FlaskForm):

    name = StringField(label="Name")
    rating = SelectField(label="Rate YOurself !", choices=[("1","1"),("2","2"),("3","3")])
    choice = RadioField(label="Select Your Choice : ", choices=[("Scripting","Scripting"),("AI","AI"),("ML","ML")])
    birthday = DateField(label="Enter your DOB", format='%Y-%m-%d')
    comments = TextAreaField(label="Enter your comments here..!!!")
    submit = SubmitField(label="Submit This!")

@app.route('/', methods=["GET","POST"])
def home():
    form = Widgets()
    return render_template('home.html', form = form)

if __name__ == '__main__':
    app.run(debug=True)
