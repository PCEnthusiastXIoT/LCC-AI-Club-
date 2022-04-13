from flask import Flask

from scraper import scrape_site

URL = 'https://lcc.edu/'

app = Flask(__name__)


@app.route('/')
def home():
	result = scrape_site(URL)
	return result


@app.route('/get-started')
def get_started():
	url_started = URL + "admissions-financial-aid/get-started/index.html"
	result = scrape_site(url_started)
	return result


if __name__ == '__main__':
	app.run(debug=False)
