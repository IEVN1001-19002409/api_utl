from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    titulo = 'IEVN-1001'
    list = ['Juan', 'Pedro', 'Fulanito']
    return render_template("uno.html", titulo=titulo, list=list)

@app.route("/user/<string:user>")
def user(user):
    return "El usuario es: {}".format(user)

@app.route("/numero/<int:n1>")
def numero(n1):
    return "El número es: {}".format(n1)

@app.route("/user/<string:nom>/<int:id>")
def datos(nom, id):
    return "<h1>ID : {} Nombre: {}</h1>".format(id, nom)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma es: {}".format(n1 + n2)

@app.route("/default")
@app.route("/default/<string:nom>")
def nom2(nom:'kas'):
    return "<h1> el nombre es: {}</h>".format(nom)



if __name__ == "__main__":
    app.run(debug=True)
