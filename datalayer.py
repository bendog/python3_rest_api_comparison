from datetime import datetime

from pynamodb import models, attributes


class Topic(models.Model):
    topic = attributes.UnicodeAttribute(hash_key=True)
    last_vote = attributes.UTCDateTimeAttribute(default=datetime.now)
    votes = attributes.NumberAttribute(default=0)

    class Meta:
        table_name = 'Topic'
        region = 'ap-southeast-2'

    # def __init__(self, *args, **kwargs):
    #     if not Topic.exists():
    #         Topic.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
    #     super().__init__(*args, **kwargs)

    def add_vote(self):
        self.update({
            'votes': {
                'action': 'add',
                'value': 1,
            },
            'last_vote': {
                'action': 'put',
                'value': datetime.now()
            }
        })

    def reset_votes(self):
        self.update({
            'votes': {
                'action': 'put',
                'value': 1,
            },
            'last_vote': {
                'action': 'put',
                'value': datetime.now()
            }
        })

    def __iter__(self):
        for name, attr in self._get_attributes().items():
            yield name, attr.serialize(getattr(self, name))
