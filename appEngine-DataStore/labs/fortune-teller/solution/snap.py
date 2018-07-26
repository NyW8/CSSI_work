#import appengine's datastore
from google.appengine.ext import ndb
import datetime

class Users(ndb.Model):

    first_name = ndb.StringProperty(required = True)
    last_name = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = True)
    password = ndb.StringProperty(required = True)
    username = ndb.StringProperty(required = True)
    bitmoji = ndb.BooleanProperty(required = True, default = False)
    location = ndb.StringProperty(required = False)
    pickle = ndb.PickleProperty(required = False)
    phone= ndb.StringProperty(required = False)
    time = ndb.DateTimeProperty(required = True, default = datetime.datetime.now())
    #friends = ndb.StructuredProperty(Friends, repeated = True)
    #subscriptions = ndb.StructuredProperty(Subscriptions, repeated = True)


class Subscriptions(ndb.Model):
    channel = ndb.IntegerProperty(required = True)
    author = ndb.StringProperty(required = False)
    article = ndb.StringProperty(required = True)
    read = ndb.BooleanProperty(required = True, default = False)

class Stories(ndb.Model):
    time = ndb.DateTimeProperty(required = True)
    location = ndb.GeoPtProperty(required = False)
    duration = ndb.IntegerProperty(required = True)

class Bitmoji(ndb.Model):
    bitmoji = ndb.BooleanProperty(required = True, default = False)
    def __init__(self, bitmojiTrue):
        self.bitmoji = bitmojiTrue

class Friends(ndb.Model):
    user1 = ndb.StringProperty(required = True)
    user2 = ndb.StringProperty(required = True)
