from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email, Length

class CadastroForm(FlaskForm):
    usuario = StringField('Usuário:', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome:', validators=[DataRequired()])
    idade = IntegerField('Idade:', validators=[DataRequired()])
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha:', validators=[DataRequired()])
    rua = StringField('Rua:', validators=[DataRequired()])
    numero = IntegerField('Número:', validators=[DataRequired()])
    bairro = StringField('Bairro:', validators=[DataRequired()])
    cep = IntegerField('CEP:', validators=[DataRequired()])

    botao = SubmitField('Cadastrar')

class LoginForm(FlaskForm):
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha:', validators=[DataRequired()])

    botao = SubmitField('Entrar')