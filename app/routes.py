from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username':'Sara'}
	posts = [
		{
			'author':{'username':'John'},
			'body':'Beautiful day in Portland!'
		},
		{
			'author':{'username':'Susan'},
			'body':'I am trollllolol'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)
