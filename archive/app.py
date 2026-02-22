from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']='abcdf'
todos =["Learn Flask","Setup venv", "Build a cool app" ]
class TodoForm(FlaskForm):
    todo = StringField("Todo",validators=[DataRequired()])
    submit = SubmitField("Add Todo")

@app.route('/',methods = ['GET','POST'])
def index():
    if "todo" in request.form:
        todos.append(request.form['todo']) #параметр, который находится в класе, который уже представлен в виде атрибута имени тега 

    return render_template('index.html',todos=todos,template_form = TodoForm())
