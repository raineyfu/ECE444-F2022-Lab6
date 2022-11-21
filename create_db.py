# create_db.py


from project.app import db, app
from project.models import Post


# create the database and the db table

with app.app_context():
    db.create_all()

    # commit the changes
    db.session.commit()