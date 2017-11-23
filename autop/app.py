from flask import Flask, send_from_directory, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['GET'])
def home():
    cars= [
        {
            'title': '2017 Chevrolet Colorado',
            'summary': 'The Chevrolet Colorado places its gaze squarely'
                       ' on off-road adventurers with the rollout of the new ZR2',
        }
    ]
    return render_template('home.jinja2', car_list=cars)


@app.route('/static/<path:path>', methods=['GET'])
def send_js(path):
    return send_from_directory('static', path)


if __name__ == '__main__':

    app.run(debug=True)
