from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:buildablog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(120))

    def __init__(self, name):
        self.name = name


posts = []


@app.route('/blog', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        post = request.form['post']
        posts.append(post)

    return render_template('blog.html', title="Blogs!", posts=posts)


@app.route('/newpost', methods=['POST', 'GET'])
def newpost():
    posterror = ""

    if request.method == 'POST':
            
        post = request.form['post']
        posts.append(post)
        
        
        return render_template('blog.html', title="fromnewpost", posts=posts)

    return render_template("newpost.html", title="WTF", posterror=posterror)
                


if __name__ == '__main__':
    app.run()
