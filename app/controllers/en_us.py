from flask import Flask, render_template, request, redirect, url_for
from app import app, db

from app.models.tables import User
from app.models.forms import LoginForm


from viga.detalhamento_flexao import detalhamento_flexao
from viga.conversao_unidades import conversao_unidades

#model_prediction = False
@app.route("/")
def index():
    return render_template('pt/inicio.html'
     # prediction=model_prediction,
      #show_predictions_modal=True
      )
dict = {}
@app.route("/novoprojeto", methods = ["POST", "GET"])
def novoprojeto():
    if request.method == "POST":
        for info in request.form:           #retira informação dos inputs
            value = float(request.form[info])
            dict[info] = value

        Dic = conversao_unidades(dict)
        Dic = detalhamento_flexao(Dic)

        return redirect(url_for("resultados"))
    else:
        return render_template('novoprojeto.html')

@app.route("/resultados", methods = ["POST", "GET"])
def resultados():
    return render_template('pt/resultados.html', info = dict)

@app.route("/contato")
def contato():
    return render_template('pt/contato.html')



@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)
    return render_template('login.html',
                            form=form)


@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    i = User("vitorjesus", "1234", "João Vítor","jovitorsant@gmail.com")
    db.session.add(i)
    db.session.commit()

    #r = User.query.filter_by(User.username="")
    return 'ok'
