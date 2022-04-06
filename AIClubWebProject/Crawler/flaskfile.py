from flask import Flask

URL = 'https://google.com/'

app = Flask(__name__)


@app.route('/')
def home():
	result = scrape_site(URL)

	return result


if __name__ == '__main__':
	app.run(debug=False)
