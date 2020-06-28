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
        if Dic['As'] + Dic['Ass'] >= 0.04*Dic['bw']*Dic['h']:
            print('Erro: Redimencionar Ac')
            #print()
            #print("SUGESTÃO: Aumentar a Altura")
            return redirect(url_for("erro"))

        return redirect(url_for("resultados"))
    else:
        return render_template('pt/novoprojeto.html')

@app.route("/erro", methods = ["GET"])
def erro():
    return render_template('pt/erro.html')


@app.route("/resultados", methods = ["POST", "GET"])
def resultados():
    return render_template('pt/resultados.html', info = dict)

@app.route("/contato")
def contato():
    return render_template('pt/contato.html')
