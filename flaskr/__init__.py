from flask import Flask
from os.path import dirname

print __path__
print __file__

def create_app(path=None,
               settings_override=None):
    if path is None:
        path = dirname(dirname(__file__))
    print path
    app = Flask('flaskr',instance_path=path)

    app.config.from_object(flaskr.settings)
    app.config.from_json('config/config.json', silent=True)
    app.config.from_object(settings_override)


    @app.route('/')
    def hello():
        return 'hello!'

    return app