#!/usr/bin/env python3
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

from datalayer import Topic

app = Flask(__name__)
api = Api(app)


class Votes(Resource):
    """ List topics which have been voted on """
    def get(self):
        return [dict(x) for x in Topic.scan()]


# define the parser for incoming values
parser = reqparse.RequestParser()
parser.add_argument('topic')


class Vote(Resource):
    """ List individual topics or create a new one if POST """

    def get(self):
        """ List topics which have been voted on """
        args = parser.parse_args()
        topic = args.get('topic')
        topics = Topic.scan(topic__contains=topic)
        return [dict(x) for x in topics]

    def post(self):
        """ add or vote on a topic"""
        args = parser.parse_args()
        topic = args.get('topic')
        t = Topic(topic=topic)
        t.add_vote()
        t.refresh()
        return dict(t), 201


# define the resources
api.add_resource(Votes, '/votes')
api.add_resource(Vote, '/vote')

# local running enabled
if __name__ == '__main__':
    app.run(debug=True)
