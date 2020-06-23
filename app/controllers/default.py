from flask import render_template, request
from app import app, db

from app.models.tables import User
from app.models.forms import LoginForm
from viga.detalhamento_flexao import detalhamento_flexao

#model_prediction = False
@app.route("/")
def index():
    return render_template('index.html',
     # prediction=model_prediction,
      #show_predictions_modal=True
      )

@app.route("/newproject", methods = ["POST", "GET"])
def newproject():
    if request.method == "POST":
        fk = request.form["fk"]
        fyk = request.form["fyk"]
        fywk = request.form["fywk"]
        Es = request.form["Es"]
        ot = request.form["ot"]
        ol = request.form["ol"]

    return render_template('newproject.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/results")
def results():
    return render_template('results.html')






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
