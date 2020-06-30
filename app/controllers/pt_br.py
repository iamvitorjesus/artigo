from flask import Flask, render_template, request, redirect, url_for
from app import app, db

from app.models.tables import User
from app.models.forms import LoginForm

from viga.conversao_unidades import conversao_unidades
from viga.dimensionamento import dimensionar


#model_prediction = False
@app.route("/")
def index():
    return render_template('pt/inicio.html'
     # prediction=model_prediction,
      #show_predictions_modal=True
      )

dimen = {}
@app.route("/novoprojeto", methods = ["POST", "GET"])
def novoprojeto():
    if request.method == "POST":
        for info in request.form:           #retira informação dos inputs
            value = float(request.form[info])
            dimen[info] = value

        Dic = conversao_unidades(dimen)
        Dic = dimensionar(Dic)
        if Dic['As'] + Dic['Ass'] >= 0.04*Dic['bw']*Dic['h']: #Verificação da Armadura Máxima
            return redirect(url_for("erroMomento"))

        if Dic['Vsd'] >= Dic['Vrd2']: # As bielas serão esmagadas.
            #É necessário um redimencionamento ou aumento do fck''')
            return redirect(url_for("erroBiela"))


        return redirect(url_for("resultados"))
    else:
        return render_template('pt/novoprojeto.html')

@app.route("/erroM", methods = ["GET"])
def erroMomento():
    return render_template('pt/erroMomento.html')

@app.route("/erroB", methods = ["GET"])
def erroBiela():
    return render_template('pt/erroBiela.html')


from viga.detalhamento_flexao import detalhamento_flexao

@app.route("/resultados", methods = ["POST", "GET"])
def resultados():
    if request.method == "POST":
        for x in request.form:
            value = float(request.form[x])
            dimen[x] = value
        print dimen
        Dic = detalhamento_flexao(dimen)

    else:
        return render_template('pt/resultados.html', info = dimen)

@app.route("/contato")
def contato():
    return render_template('pt/contato.html')
