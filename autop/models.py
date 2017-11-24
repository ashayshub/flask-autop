from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(session_options={
    'autocommit': True,
    'autoflush': True
})


class Car(db.Model):
    __tablename__ = 'cars'
    __table_args__ = (
       db.UniqueConstraint('title', 'car_type', name='uix_1'),
    )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120))
    car_type = db.Column(db.String(20))
    car_make = db.Column(db.String(120))
    car_model = db.Column(db.String(120))
    year = db.Column(db.String(120))
    summary = db.Column(db.String(255))
    image = db.Column(db.String(255))

    def __init__(self, title=None, summary=None, car_type=None, image=None, car_make=None, car_model=None, year=None):
        self.title = title
        self.car_type = car_type
        self.car_make = car_make
        self.car_model = car_model
        self.year = year
        self.summary = summary
        self.image = image

    def __repr__(self):
        return f'<Car {self.title}>'


def init_db():
    db.create_all()


def db_insert(data):
    db.session.bulk_insert_mappings(Car, data)
    return True


def drop_table():
    return Car.__table__.drop(bind=db.engine, checkfirst=True)
