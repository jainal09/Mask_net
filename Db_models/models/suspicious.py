import mongoengine
import datetime

class Suspicious(mongoengine.Document):
    image= mongoengine.BinaryField(required=True)
    date = mongoengine.DateTimeField(default=datetime.datetime.now)
    location= mongoengine.StringField()

    meta={
        'db_alias': 'core',
        'collection': 'suspicious'
    }