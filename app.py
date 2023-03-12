from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
import forms
from flask import jsonify
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db #ORM
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route("/", methods = ['GET','POST'])
def index():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(nombre = create_form.nombre.data,
                       apellidos = create_form.apellidos.data,
                       email = create_form.email.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('abc'))
    return render_template('index.html', form = create_form)

@app.route("/abc", methods = ['GET','POST'])
def abc():
    abc_Form = forms.UserForm(request.form)
    alumno = Alumnos.query.all()

    return render_template('ABCompleto.html', form = abc_Form, alumno = alumno)

@app.route("/modificar", methods = ['GET','POST'])
def modificar():
    mod_Form = forms.UserForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        mod_Form.id.data = request.args.get('id')
        mod_Form.nombre.data = alum1.nombre
        mod_Form.apellidos.data = alum1.apellidos
        mod_Form.email.data = alum1.email

    if request.method == 'POST':
        id = mod_Form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum.nombre = mod_Form.nombre.data
        alum.apelidos = mod_Form.apellidos.data
        alum.email = mod_Form.email.data
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('abc'))
        
    return render_template('modificar.html',form = mod_Form)

@app.route("/eliminar", methods = ['GET','POST'])
def eliminar():
    mod_Form = forms.UserForm(request.form)
    
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        mod_Form.id.data = request.args.get('id')
        mod_Form.nombre.data = alum1.nombre
        mod_Form.apellidos.data = alum1.apellidos
        mod_Form.email.data = alum1.email

    if request.method == 'POST':
        id = mod_Form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum.nombre = mod_Form.nombre.data
        alum.apelidos = mod_Form.apellidos.data
        alum.email = mod_Form.email.data
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('abc'))
    return render_template('eliminar.html',form = mod_Form)

csrf = CSRFProtect()

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all #Se borró los ()
    app.run(port=3000)