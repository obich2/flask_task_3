from flask import Flask, url_for, render_template
app = Flask(__name__)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def return_mars_page(nickname, level, rating):
    return render_template('index.html', planet_name=nickname, level=level, rating=rating)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
