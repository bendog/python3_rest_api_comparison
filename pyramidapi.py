from wsgiref.simple_server import make_server
import json
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

from datalayer import Topic


@view_config(renderer='json')
def votes(request):
    """ List topics which have been voted on """
    return Response(json.dumps([dict(x) for x in Topic.scan()]))
    # return [dict(x) for x in Topic.scan()]


# config
config = Configurator()
config.add_route('votes', '/votes')
config.add_view(votes, route_name='votes')


# wsgi for zappa
def generate_wsgi_app(app, environ):
    wsgi_app = config.make_wsgi_app()
    return wsgi_app(app, environ)


# run locally
if __name__ == '__main__':
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
