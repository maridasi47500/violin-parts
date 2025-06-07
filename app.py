from flask import Flask, render_template, request, redirect, url_for
from models import db, Post

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///violin.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/post", methods=["GET", "POST"])
def post():
    if request.method == "POST":
        content = request.form.get("content")
        difficulte = request.form.get("difficulte")
        resonnance = request.form.get("resonnance")
        if content:
            new_post = Post(content=content, difficulte=difficulte, resonnance=resonnance)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for("post_success"))
    return render_template("post_form.html")

@app.route("/post/success")
def post_success():
    return render_template('merci.html')

@app.route("/posts")
def posts():
    all_posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("posts.html", posts=all_posts)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
