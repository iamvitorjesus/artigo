from flask import Flask, render_template, request, redirect, url_for
from app import app, db

from app.models.tables import User
from app.models.forms import LoginForm
from viga.detalhamento_flexao import detalhamento_flexao

#model_prediction = False
@app.route("/")
def index():
    return render_template('index.html'
     # prediction=model_prediction,
      #show_predictions_modal=True
      )

@app.route("/newproject", methods = ["POST", "GET"])
def newproject():
    l = ["fk", "unitfk","fyk", "unitfyk", "fywk", "unitfywk", "Es",
        "unitEs", "ot", "unitot", "ol", "unitol", "a", "Dmax", "Modelo",
        "CAA", "Mk", "unitMk", "Vk", "unitVk", "yc", "ys", "bw", "unitbw",
        "h", "unith", "l", "unitl", "t1", "unitt1", "t2", "unitt2"]
    dict = {}
    if request.method == "POST":
        for name in l:
            value = request.form[name]
            dict[name] = value
        #detalhamento_flexao(dict)
        return redirect(url_for("results", usr=dict))
    else:
        return render_template('newproject.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/results")
def results(usr):
    return ("<h1>{usr}</h1>")






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
