from flask import Flask, render_template, url_for
app = Flask(__name__)
frettir = [
		[0,"0bla", "0bla blablablabla", "0@gmail"], [ 1, "1bla", "1bla blalbald", "1@gamil"]
		]
myndir = [
		['glasses.jpg'], ['frost.jpg']
	]

@app.route('/')
def index():
	return render_template('index.tpl', frettir=frettir)
@app.errorhandler(404)
def error404(error):
	return '<h1>Þessi síða er ekki til</h1>', 404

@app.route("/home/<int:nr>")
def home(nr):
	return render_template('example.html', frett=frettir[nr], myndir=myndir[nr], listi=frettir)

if __name__ == "__main__":
	app.run(debug=True)
	