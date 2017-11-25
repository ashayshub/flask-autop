import logging
from flask import Flask, send_from_directory, render_template, request
from flask_bootstrap import Bootstrap
from flask_paginate import Pagination, get_page_args

from autop.processor import Crawler
from autop.models import db, Car, init_db, drop_table

app = Flask(__name__, static_url_path='/static', root_path='/app',
            template_folder='autop/templates', static_folder='autop/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/autop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Bootstrap(app)
db.init_app(app=app)


# For Debug
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r


# All GET Methods

@app.route('/', methods=['HEAD', 'GET'])
@app.route('/Sport', methods=['HEAD', 'GET'])
def get_trucks():
    init_db()
    car_type = request.args.get('car_type', 'Truck')
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    query = Car.query.filter_by(car_type=car_type).order_by(Car.title)
    cars = query.offset(offset).limit(per_page).all()
    count = query.count()

    pagination = Pagination(page=page, per_page=per_page, total=count,
                            record_name='cars', css_framework='bootstrap3',
                            format_total=True,  format_number=True
                            )

    return render_template('home.jinja2', cars=cars, car_type=car_type,
                           page=page, per_page=per_page, pagination=pagination)


# All POST Methods
@app.route('/populate/', methods=['POST'])
def populate_db():
    init_db()
    crawl_url = {'Truck': 'http://www.nydailynews.com/autos/types/truck',
                 'Sport': 'http://www.nydailynews.com/autos/types/sports-car'}
    crawl = Crawler()
    ret_val = crawl.populate(crawl_url)

    if ret_val is None:
        return 'Could not find any car list', 404
    elif ret_val is False:
        return 'Error inserting data in database', 500

    return 'Populated the data into database'


# All DELETE Methods
@app.route('/teardown/', methods=['DELETE'])
def teardown_db_table():
    if drop_table() is False:
        return 'Error Dropping the database table', 500
    return 'Tore down the structure'


if __name__ == '__main__':
    app.run(debug=True)
