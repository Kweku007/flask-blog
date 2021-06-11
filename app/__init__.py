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
	# Hardcoded projects names
	robotics_projects = ['Sumo Robot/sumo.jpg', 'Line Following Robot/line_follower.png', 'Soccer Robot/soccer_robot.jpeg', 'Fire Extinguishing Robot/fire_robot.jpg']
	electronics_projects = ['Cell Phone Detector/Cell-phone-detector.jpg', 'Mobile Jammer Circuit/Mobile-Jammer.jpg']
	ai_projects = ['Font Classifier Perceptron/robot_img_example.png']
	misc_projects = ['Snake Video Game/snake.png']
	projects_names = [robotics_projects, electronics_projects, ai_projects, misc_projects]
	
	page = request.args.get('page')
	if page and page.isdigit():
		page = int(page)
	else:
		page = 1
	
	return render_template('projects.html', title="Projects", url=os.getenv("URL"), projects=projects_names,pag = page)
