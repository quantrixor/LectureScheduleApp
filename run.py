from app import create_app, db
from app import models
import logging
from flask_cors import CORS
from app.views.lecture_views import app as lecture_views_blueprint


app = create_app()
app.register_blueprint(lecture_views_blueprint)
CORS(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    handler = logging.FileHandler('flask_error.log')
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)
