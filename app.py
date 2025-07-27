# Required Libraries
from flask import Flask, session, redirect, request,Response, url_for, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired , Length, Email

# Initialize Flask App

app = Flask(__name__)
app.secret_key = "superkey"
#---------------------
# Flask-WTF Form Class
#---------------------

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(),Email() ])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Register")

#------------------------------
#  Routes
#------------------------------

@app.route("/")
def home():
    return render_template('home.html')

# Manual Form

@app.route('/manual-form', methods=['GET', 'POST'])
def manual_form():
    error = None
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')

        # Manual Validation
        if not name or not email:
            error = "All Feilds are Required"
        elif "@" not in email:
            error = "Enter Valid Email address"
        else:
            flash(f"Manual Form Submitted successfully by the {name} with a specific  Email address {email} ", "success")
            return redirect(url_for('home'))
    return render_template('manual_form.html', error=error)

# Flask WTF Form Route

@app.route('/wtf-form', methods=["GET","POST"])
def wtf_form():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f"WTForm Submitted Successfully by {form.username.data} with a specific Email address {form.email.data}  ", "info")
        return redirect(url_for('home'))
    return render_template('wtf_form.html', form=form)

# Main app
if __name__=="__main__":
    app.run(debug=True)


