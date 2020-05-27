
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import RegistrationForm, LoginForm



app = Flask(__name__)
app.config['SECRET_KEY'] = '7d37eb5a006a03a902f7f0e459d1be02'
app.config['SQLAlCHEMY_DATABASE_URI'] = 'postgresql://scott:tiger@localhost/Registration_api'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    __tablename__='sign up'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __init__(self, username, email, password, posts):
        self.username = username
        self.email = email
        self.password = password
        self.posts = posts

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default= datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

    def __init__(self, title, date_posted, content, user_id):
        self.title = title
        self.date_posted = date_posted
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

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
        if form.email.data == 'khadija.shahid1997@gmail.com' and form.password.data == 'Hello123':
            flash('you have been logged in! ', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful.','danger')
    return render_template('login.html', title='Login', form=form)


if __name__=="__main__":
    app.run(debug =True)
