from flask import Flask, render_template
app = Flask(__name__)
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

if __name__=="__main__":
    app.run(debug =True)
