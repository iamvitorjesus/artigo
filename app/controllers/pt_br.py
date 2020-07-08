from flask import Flask, render_template, request, redirect, url_for, session
from app import app, db
import os


from app.models.tables import User
from app.models.forms import LoginForm

from viga.conversao_unidades import conversao_unidades
from viga.dimensionamento import dimensionar

logoufrj = os.path.join(app.config['UPLOAD_FOLDER'], 'complementar_principal_pb.png')
logomacae = os.path.join(app.config['UPLOAD_FOLDER'], 'campus_UFRJ_macae_Aloisio_Teixeira.png')
logo4 = os.path.join(app.config['UPLOAD_FOLDER'], 'ReCon4.png')
logo6 = os.path.join(app.config['UPLOAD_FOLDER'], 'ReCon6.png')

#model_prediction = False
@app.route("/")
def index():

    return render_template('pt/inicio.html',
     # prediction=model_prediction,
      #show_predictions_modal=True
      lufrj = logoufrj, lmacae = logomacae, logo6 = logo6)


@app.route("/novoprojeto", methods = ["POST", "GET"])
def novoprojeto():
    if request.method == "POST":
        dimen = {}
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

        session["dic"] = Dic
        return redirect(url_for("resultados"))
    else:
        if "user" in session:
            return redirect(url_for("resultados"))
        return render_template('pt/novoprojeto.html', logo6 = logo6)

@app.route("/erroM", methods = ["GET"])
def erroMomento():
    return render_template('pt/erroMomento.html', logo6 = logo6)

@app.route("/erroB", methods = ["GET"])
def erroBiela():
    return render_template('pt/erroBiela.html', logo6 = logo6)


from viga.detalhamento_flexao import detalhamento_flexao

@app.route("/resultados", methods = ["POST", "GET"])
def resultados():
    if 'dic' in session:
        Dic = session['dic']
        if request.method == "POST":
            for x in request.form:
                value = float(request.form[x])
                Dic[x] = value
            Dic = detalhamento_flexao(Dic)
            return render_template('pt/resultados.html', info = Dic, logo6 = logo6)
        else:
            return render_template('pt/resultados.html', info = Dic, logo6 = logo6)
    else:
        return redirect(url_for("novoprojeto"))

@app.route("/contato")
def contato():
    return render_template('pt/contato.html', logo6 = logo6)
