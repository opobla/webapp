import flask
import redis
import os

# Crear el objeto que representa la aplicacion web
APP = flask.Flask(__name__)

redis_available = os.environ.get('REDIS_AVAILABLE', 'no').lower() == "yes"
if redis_available:
    redis_host = os.environ['REDIS_HOST']
    redis_port = os.environ['REDIS_PORT']
    redis_cli = redis.Redis(host=redis_host, port=redis_port)

@APP.route('/')
def index():
    userinfo_mock = {
            'username': 'Óscar',
            'photo_url': 'https://via.placeholder.com/150'
    }

    contador = redis_cli.incr("webapp.contador") if redis_available else None

    return flask.render_template('index.html', contador_visitas=contador, user=userinfo_mock)


if __name__ == '__main__':
    PORT = os.environ['PORT']
    APP.debug = True
    APP.run(host='0.0.0.0', port=PORT)
