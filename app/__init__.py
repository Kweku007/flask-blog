import os
from flask import Flask, render_template, send_from_directory
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html', title="Kweku Aboagye", url=os.getenv("URL"))

@app.route('/contact')
def contact():
    return render_template('contacts.html', title="Kweku Aboagye", url=os.getenv("URL"))

@app.route('/blog')
def blog():
    return render_template('blog.html', title="Kweku Aboagye", url=os.getenv("URL"))

@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects", url=os.getenv("URL"))
