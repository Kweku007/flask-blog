import os
from flask import Flask, render_template, send_from_directory
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
from flask import request

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
	# Hardcoded projects
	robotics_projects = ['Sumo Robot', 'Line Following Robot', 'Soccer Robot', 'Fire Extinguishing Robot']
	electronics_projects = ['Cell Phone Detector', 'Mobile Jammer Circuit']
	ai_projects = ['Font Classifier Perceptron']
	misc_projects = ['Snake Video Game']
	proje = [robotics_projects, electronics_projects, ai_projects, misc_projects]
	
	page = request.args.get('page')
	if page and page.isdigit():
		page = int(page)
	else:
		page = 1
	
	return render_template('projects.html', title="Projects", url=os.getenv("URL"), projects=proje, pag = page)
