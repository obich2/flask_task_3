from flask import Flask, url_for, render_template
app = Flask(__name__)


@app.route('/choice/<planet_name>')
def return_mars_page(planet_name):
    return render_template('index.html', planet_name=planet_name)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
