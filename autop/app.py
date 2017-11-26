import logging
import os

from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
from flask_paginate import Pagination, get_page_args
from sqlalchemy import exc

from autop.processor import populate, request_price
from autop.models import db, Car, init_db, drop_table

app = Flask(__name__, static_url_path='/static', root_path='/app',
            template_folder='autop/templates', static_folder='autop/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/autop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    db.init_app(app=app)
    init_db()

Bootstrap(app)



# For Debug
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    if os.environ.get('DEBUG', '0') == '1':
        logging.warning('Debugging is On')
        r.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate, public, max-age=0'
        r.headers['Pragma'] = 'no-cache'
        r.headers['Expires'] = '0'
    return r


# All GET Methods

@app.route('/', methods=['HEAD', 'OPTIONS', 'GET'])
@app.route('/Sport', methods=['HEAD', 'OPTIONS', 'GET'])
def get_trucks():
    car_type = request.args.get('car_type', 'Truck')
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    query = Car.query.filter_by(car_type=car_type).order_by(Car.title)

    try:
        cars = query.offset(offset).limit(per_page).all()
        count = query.count()
    except exc.OperationalError as e:
        logging.error(f'Exception quering cars table: {e}')
        cars = dict()
        count = 0

    pagination = Pagination(page=page, per_page=per_page, total=count,
                            record_name='cars', css_framework='bootstrap3',
                            format_total=True,  format_number=True
                            )

    return render_template('home.jinja2', cars=cars, car_type=car_type,
                           page=page, per_page=per_page, pagination=pagination)


@app.route('/price', methods=['HEAD', 'OPTIONS', 'GET'])
def get_price():
    query = request.args.get('price_query', None)

    if query is None:
        return 'Bad Request', 400

    url_prefix = 'http://www.nydailynews.com/autos/'
    price_url = url_prefix + query
    resp = request_price(price_url)

    if not resp:
        return 'Not Found', 404

    return jsonify(resp)


# All POST Methods
@app.route('/populate/', methods=['POST'])
def populate_db():
    crawl_url = {'Truck': 'http://www.nydailynews.com/autos/types/truck',
                 'Sport': 'http://www.nydailynews.com/autos/types/sports-car'}

    ret_val = populate(crawl_url)

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

    debug_flag = False
    if os.environ.get('DEBUG', '0') == '1':
        debug_flag = True

    app.run(debug=debug_flag)
