"""!DOCTYPE python"""

import pickle
from flask import Flask, render_template, redirect, url_for
from forms import RegistrationForm
from sheets import newTeam

app = Flask(__name__)
app.app_context().push()

@app.route("/", methods=['GET', 'POST'])
def home():
    form = RegistrationForm()
    if form.validate_on_submit():
        openRow = pickle.load(open("openRow.dat", "rb"))
        print('data submitted')
        newTeam(openRow, form.teamNum.data, form.teamName.data)
        openRow = pickle.dump(openRow+1, open("openRow.dat", "wb"))
        return redirect(url_for('home'))
    return render_template('home.html', form=form)

