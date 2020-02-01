import connexion
import os


def create_app(): 
    abs_file_path = os.path.abspath(os.path.dirname(__file__))
    
    openapi_path = os.path.join(abs_file_path, "openapi/")
    app = connexion.FlaskApp(__name__, specification_dir=openapi_path)
    app.add_api('api.yaml')
    flask_app = app.app
    return flask_app