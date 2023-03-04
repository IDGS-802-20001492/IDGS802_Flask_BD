from  wtforms import Form
from  wtforms import StringField, IntegerField, EmailField, validators

class UserForm(Form):
    id = IntegerField('Id')
    nombre = StringField('Nombre')
    apellidos = StringField('Apellidos')
    email = EmailField('Email')