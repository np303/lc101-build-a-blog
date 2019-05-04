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
    post = db.Column(db.String(120))

    def __init__(self, title, post):
        self.title = title
        self.post =  post

posts = []


@app.route('/blog', methods=['POST', 'GET'])
def index():

    #Query database for all blog posts
    allblogposts = Blog.query.all()
    post_id = request.args.get('id')
    
    if (post_id):
        blogpost = Blog.query.get(post_id)
        return render_template('blogpost.html', blogpost=blogpost)

    return render_template('blog.html', title="Blogs!", posts=allblogposts)



@app.route('/newpost', methods=['POST', 'GET'])
def newpost():
    
    posterror = ""
    allblogposts = Blog.query.all()

    if request.method == 'POST':

        #look inside the html form for user data    
        title = request.form['title']
        post = request.form['post']
        
        #creat a newpost reference 
        newpost = Blog(title, post)
                       

        db.session.add(newpost)
        db.session.commit()

        #creat a link to go to the new post when use clicks submit
        postlink = "/blog?id=" + str(newpost.id)

        return redirect(postlink)

    return render_template('newpost.html', title="WTF", posterror=posterror)
                


if __name__ == '__main__':
    app.run()
