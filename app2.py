from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm



app = Flask(__name__)

app.config['SECRET_KEY'] = '7d37eb5a006a03a902f7f0e459d1be02'
posts = [
    {
    'author': 'khadija shahid',
    'title': 'first post',
    'content':'first post content',
    'date_posted':'april 20,2020'
    },
    {
    'author': 'saad sohail',
    'title': 'second post',
    'content':'second post content',
    'date_posted':'april 21,2020'
    }
]


@app.route('/home')
def home():
    flash('hi')
    return render_template("home.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html", title="about")

@app.route('/register',  methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password1':
            flash('you have been logged in! ', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful.','danger')
    return render_template('login.html', title='Login', form=form)


if __name__=="__main__":
    app.run(debug =True)
