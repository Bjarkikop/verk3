from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Flask er flottast</h1>'

"""
@app.route('/biography')
def Biography():
	return '<h1>Þetta er Biography síða</h1>  <a href="/home">Home</a>'

@app.route('/about')
def about():
	return '<h1>Þetta er about síðan </h1>  <a href="/home">Home</a>'
@app.route("/home", methods=['GET', 'POST'])
def home():
	links = ['https://www.youtube.com', 'https://www.bing.com', 'https://www.python.org']
	return render_template('example.html', myvar="flask example", links=links)
"""
if __name__ == "__main__":
	app.run(debug=True)
	