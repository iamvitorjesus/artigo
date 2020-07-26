from flask import Flask, render_template, request, redirect, url_for, session
from app import app, db
import os


from app.models.tables import User
from app.models.forms import LoginForm

from viga.conversao_unidades import conversao_unidades
from viga.dimensionamento import dimensionar

logoufrj = os.path.join(app.config['UPLOAD_FOLDER'], 'complementar_principal_pb.png')
logomacae = os.path.join(app.config['UPLOAD_FOLDER'], 'campus_UFRJ_macae_Aloisio_Teixeira.png')
logo = os.path.join(app.config['UPLOAD_FOLDER'], 'ReCon8.png')
logocilamce = os.path.join(app.config['UPLOAD_FOLDER'], 'logocilamce2020_online.png')
distribuicao = os.path.join(app.config['UPLOAD_FOLDER'], 'distrib.jpeg')

def virgula(value):

    if value.count('-') != 0:
        value = value.split('-')
        value = value[1]
        if value.find(',') != -1:
            value = value.replace(',','.')
        value = (-1)*float(value)

    else:
        x = value
        if x.count(',') != 0:
            value = value.replace(',','.')
            value = float(value)
        elif value.count('.') != 0:
            value = float(value)
        else:
            if value.isnumeric() == True:
                value = float(value)


#model_prediction = False
@app.route("/")
def inicio():
    return render_template('pt/inicio.html',
     # prediction=model_prediction,
      #show_predictions_modal=True
      lufrj = logoufrj, lmacae = logomacae, logo = logo, cilamce = logocilamce)


@app.route("/novoprojeto", methods = ["POST", "GET"])
def novoprojeto():
    if request.method == "POST":
        dimen = {}
        for info in request.form:           #retira informação dos inputs
            value = request.form[info]

            if value.count('-') != 0:
                value = value.split('-')
                value = value[1]
                if value.find(',') != -1:
                    value = value.replace(',','.')
                value = (-1)*float(value)

            else:
                x = value
                if x.count(',') != 0:
                    value = value.replace(',','.')
                    value = float(value)
                elif value.count('.') != 0:
                    value = float(value)
                else:
                    if value.isnumeric() == True:
                        value = float(value)

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
        return render_template('pt/novoprojeto.html', logo = logo)



@app.route("/exemplo1", methods = ["POST", "GET"])
def exemplo1():
    if request.method == "POST":
        dimen = {}
        for info in request.form:           #retira informação dos inputs
            value = request.form[info]

            if value.count('-') != 0:
                value = value.split('-')
                value = value[1]
                if value.find(',') != -1:
                    value = value.replace(',','.')
                value = (-1)*float(value)

            else:
                x = value
                if x.count(',') != 0:
                    value = value.replace(',','.')
                    value = float(value)
                elif value.count('.') != 0:
                    value = float(value)
                else:
                    if value.isnumeric() == True:
                        value = float(value)

            dimen[info] = value
        print(dimen)
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
        return render_template('pt/exemplo1.html', logo = logo)


@app.route("/exemplo2", methods = ["POST", "GET"])
def exemplo2():
    if request.method == "POST":
        dimen = {}
        for info in request.form:           #retira informação dos inputs
            value = request.form[info]

            if value.count('-') != 0:
                value = value.split('-')
                value = value[1]
                if value.find(',') != -1:
                    value = value.replace(',','.')
                value = (-1)*float(value)

            else:
                x = value
                if x.count(',') != 0:
                    value = value.replace(',','.')
                    value = float(value)
                elif value.count('.') != 0:
                    value = float(value)
                else:
                    if value.isnumeric() == True:
                        value = float(value)

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
        return render_template('pt/exemplo2.html', logo = logo)


@app.route("/exemplo3", methods = ["POST", "GET"])
def exemplo3():
    if request.method == "POST":
        dimen = {}
        for info in request.form:           #retira informação dos inputs
            value = request.form[info]

            if value.count('-') != 0:
                value = value.split('-')
                value = value[1]
                if value.find(',') != -1:
                    value = value.replace(',','.')
                value = (-1)*float(value)

            else:
                x = value
                if x.count(',') != 0:
                    value = value.replace(',','.')
                    value = float(value)
                elif value.count('.') != 0:
                    value = float(value)
                else:
                    if value.isnumeric() == True:
                        value = float(value)

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
        return render_template('pt/exemplo3.html', logo = logo)


@app.route("/exemplo4", methods = ["POST", "GET"])
def exemplo4():
    if request.method == "POST":
        dimen = {}
        for info in request.form:           #retira informação dos inputs
            value = request.form[info]

            if value.count('-') != 0:
                value = value.split('-')
                value = value[1]
                if value.find(',') != -1:
                    value = value.replace(',','.')
                value = (-1)*float(value)

            else:
                x = value
                if x.count(',') != 0:
                    value = value.replace(',','.')
                    value = float(value)
                elif value.count('.') != 0:
                    value = float(value)
                else:
                    if value.isnumeric() == True:
                        value = float(value)

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
        return render_template('pt/exemplo4.html', logo = logo)


@app.route("/exemplo5", methods = ["POST", "GET"])
def exemplo5():
    if request.method == "POST":
        dimen = {}
        for info in request.form:           #retira informação dos inputs
            value = request.form[info]

            if value.count('-') != 0:
                value = value.split('-')
                value = value[1]
                if value.find(',') != -1:
                    value = value.replace(',','.')
                value = (-1)*float(value)

            else:
                x = value
                if x.count(',') != 0:
                    value = value.replace(',','.')
                    value = float(value)
                elif value.count('.') != 0:
                    value = float(value)
                else:
                    if value.isnumeric() == True:
                        value = float(value)

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
        return render_template('pt/exemplo5.html', logo = logo)


@app.route("/exemplo6", methods = ["POST", "GET"])
def exemplo6():
    if request.method == "POST":
        dimen = {}
        for info in request.form:           #retira informação dos inputs
            value = request.form[info]

            if value.count('-') != 0:
                value = value.split('-')
                value = value[1]
                if value.find(',') != -1:
                    value = value.replace(',','.')
                value = (-1)*float(value)

            else:
                x = value
                if x.count(',') != 0:
                    value = value.replace(',','.')
                    value = float(value)
                elif value.count('.') != 0:
                    value = float(value)
                else:
                    if value.isnumeric() == True:
                        value = float(value)

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
        return render_template('pt/exemplo6.html', logo = logo)



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
            print(Dic)
            return render_template('pt/resultados.html', info = Dic, logo = logo, distribuicao = distribuicao)
        else:
            return render_template('pt/resultados.html', info = Dic, logo = logo, distribuicao = distribuicao)
    else:
        return redirect(url_for("novoprojeto"))


@app.route("/contato")
def contato():
    return render_template('pt/contato.html', logo = logo)


@app.route("/menu", methods = ["GET"])
def menu():
    return render_template('pt/menu.html', logo = logo)


@app.route("/erroM", methods = ["GET"])
def erroMomento():
    return render_template('pt/erroMomento.html', logo = logo)


@app.route("/erroB", methods = ["GET"])
def erroBiela():
    return render_template('pt/erroBiela.html', logo = logo)
