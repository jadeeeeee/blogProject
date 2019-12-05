from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from formulario import CadastroForm, LoginForm

app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///nossoBlog.db"
app.config['SECRET_KEY'] = 'akjdshsagdgajdgmnxmch'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True, nullable=False)
    sobrenome = db.Column(db.String(80), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(20), nullable=False)
    rua = db.Column(db.String(50), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    bairro = db.Column(db.String(50), nullable=False)
    cep = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.usuario


@app.route('/')
@app.route('/index')
@app.route('/inicio')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():

    form = CadastroForm()

    if form.validate_on_submit():
        novo_user = User(usuario = form.usuario.data, sobrenome = form.sobrenome.data, idade = form.idade.data, email = form.email.data, senha = form.senha.data, rua = form.rua.data, numero = form.numero.data, bairro = form.bairro.data, cep = form.cep.data)
        db.session.add(novo_user)
        db.session.commit()

    return render_template('cadastre-se.html', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user:
            if user.email == form.email.data:
                return 'dshajdhsajh'
            else:
                print('Tchau')
                return 'osdjajdksa'

    return render_template('login.html', form=form)

@app.route('/informacoes')
def informacoes():
	return render_template('informacoes.html')

if __name__ == '__main__':
    app.run(debug=True)