from app.app import application
from app.db import db
import app.routes
from admin.admin import admin

application.register_blueprint(admin, url_prefix='/admin')

if __name__ == "__main__":
    # application.run(host='0.0.0.0', debug=False)
    application.run(debug=True)