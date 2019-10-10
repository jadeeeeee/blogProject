from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///nossoBlog.db"
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(8), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username


@app.route("/")
@app.route("/index")
@app.route("/inicio")
def index():
    return render_template("index.html")

@app.route("/cadastro")
def cadastro():
	return render_template("cadastre-se.html")

@app.route("/login")
@app.route("/entrar")
def login():
	return render_template("login.html")

@app.route("/informacoes")
def informacoes():
	return render_template("_informacoes.html")


if __name__ == "__main__":
    app.run(debug=True)