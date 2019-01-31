from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config, view_defaults

from datalayer import Topic


# noinspection PyUnusedLocal
@view_config(route_name='votes')
def votes(request):
    """ List topics which have been voted on """
    return Response(json=[dict(x) for x in Topic.scan()])
    # return [dict(x) for x in Topic.scan()]
    # return Response("some text", json=True)


@view_defaults(route_name='vote')
class TutorialViews(object):
    def __init__(self, request):
        self.request = request

    @view_config(request_method='GET')
    def vote(self):
        """ Show topic passed as param """
        topic = self.request.params.get('topic')
        if topic:
            topics = Topic.scan(topic__contains=topic)
            return Response(json=[dict(x) for x in topics])
        return Response("%s(%s)" % ("Bad Request", "Filtering Votes requires a topic argument"), status_code=400)

    @view_config(request_method='POST')
    def vote_post(self):
        """ vote on topic passed as value """
        try:
            topic = self.request.json_body.get('topic')
            t = Topic(topic=topic)
            t.add_vote()
            t.refresh()
            return Response(json=dict(t), status_code=201)
        except Exception as e:
            return Response("%s(%s)" % (type(e).__name__, e), status_code=500)


# config
config = Configurator()
config.add_route('votes', '/votes')
config.add_route('vote', '/vote')
config.scan()


# wsgi for zappa
# noinspection PyShadowingNames
def generate_wsgi_app(app, environ):
    wsgi_app = config.make_wsgi_app()
    return wsgi_app(app, environ)


# run locally
if __name__ == '__main__':
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
