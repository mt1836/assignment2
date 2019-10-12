import subprocess
from flask import Flask, render_template, url_for, flash, redirect, session, g, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from forms import RegistrationForm, LoginForm, SpellCheckForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route("/")
@app.route("/results")
def results():
    global input_text
    global spellcheck_results
    return render_template('results.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        global userinfo
        userinfo = {form.username.data:{'username':form.username.data, 'password':form.password.data, 'phone_number':form.phone_number.data}}
        flash(f'Success!  Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    global userinfo
    session.pop('user', None)
    if form.validate_on_submit():
        if form.phone_number.data == userinfo[form.username.data]['phone_number'] and form.password.data == userinfo[form.username.data]['password']:
            session['user'] = form.username.data
            flash('You have been logged in!', 'success')
            return redirect(url_for('spellcheck'))
        else:
            flash('Login failure. Please check username, password or 2fa', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout", methods=['GET'])
def logout():
    session.pop('user')
    return redirect(url_for('login'))
    

@app.route("/spellcheck", methods=['GET', 'POST'])
def spellcheck():
    form = SpellCheckForm()
    global input_text
    global spellcheck_results
    if g.user:
        if form.validate_on_submit():
            input_text = form.checktext.data
            input_file = open("spellcheckfile.txt","w")
            input_file.write(input_text)
            input_file.close()
            spellcheck_results = subprocess.check_output(["./a.out", "spellcheckfile.txt", "wordlist.txt"])
            spellcheck_results = spellcheck_results.decode('utf-8')
            spellcheck_results = spellcheck_results.replace("\n",", ")
            spellcheck_results = spellcheck_results.rstrip(", ")
            spellcheck_file = open("resultsfile.txt","w")
            spellcheck_file.write(spellcheck_results)
            spellcheck_file.close()
            flash(f'Text below successfully submitted:', 'success')
            flash(f'"{input_text}"', 'success')
            return render_template('results.html', title='Spell Checker Results', spellcheck_results=spellcheck_results)
        return render_template('spellcheck.html', title='Spell Checker', form=form)
    return redirect(url_for('login'))


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

if __name__ == '__main__':
    app.run(debug=True)
