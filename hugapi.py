#!/usr/bin/env python3
import hug
from datalayer import Topic


@hug.get()
@hug.local()
def votes():
    """ List topics which have been voted on """
    return [dict(x) for x in Topic.scan()]


@hug.get(examples='topic=rest')
@hug.local()
def vote(topic: hug.types.text):
    """ List topics which have been voted on """
    topics = Topic.scan(topic__contains=topic)
    return [dict(x) for x in topics]


@hug.post()
@hug.local()
def vote(topic: hug.types.text, response):
    """Add your voice to the list of topics PDPD should discuss"""
    t = Topic(topic=topic)
    t.add_vote()
    t.refresh()
    response.status = hug.HTTP_201
    return dict(t)
